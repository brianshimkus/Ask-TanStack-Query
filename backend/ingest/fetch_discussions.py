"""Day 2: download answered Q&A discussions from GitHub into data/discussions.json.

Run from inside backend/:  uv run python -m ingest.fetch_discussions
"""

import json
import os
from pathlib import Path

import httpx
from dotenv import load_dotenv

load_dotenv()

OWNER, NAME = "TanStack", "query"
API_URL = "https://api.github.com/graphql"
HEADERS = {"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"}

CATEGORIES_QUERY = """
query($owner: String!, $name: String!) {
  repository(owner: $owner, name: $name) {
    discussionCategories(first: 25) {
      nodes { id name isAnswerable }
    }
  }
}
"""

DISCUSSIONS_QUERY = """
query($owner: String!, $name: String!, $categoryId: ID!, $cursor: String) {
  repository(owner: $owner, name: $name) {
    discussions(first: 50, after: $cursor, answered: true, categoryId: $categoryId,
                orderBy: {field: CREATED_AT, direction: DESC}) {
      pageInfo { hasNextPage endCursor }
      nodes {
        number
        title
        body
        url
        createdAt
        answer { body }
      }
    }
  }
}
"""


def graphql(query, variables):
    """Send one GraphQL request to GitHub and return the 'data' part of the reply."""
    resp = httpx.post(
        API_URL,
        headers=HEADERS,
        json={"query": query, "variables": variables},
        timeout=60,
    )
    resp.raise_for_status()
    payload = resp.json()
    if payload.get("errors"):
        raise RuntimeError(f"GitHub returned errors: {payload['errors']}")
    return payload["data"]


def find_qa_category_id():
    data = graphql(CATEGORIES_QUERY, {"owner": OWNER, "name": NAME})
    categories = data["repository"]["discussionCategories"]["nodes"]
    for category in categories:
        if category["isAnswerable"] and "q&a" in category["name"].lower():
            return category["id"]
    raise RuntimeError(
        f"No Q&A category found. Categories were: {[c['name'] for c in categories]}"
    )


def main():
    category_id = find_qa_category_id()
    print(f"Found the Q&A category: {category_id}")

    results = []
    cursor = None
    while True:
        data = graphql(
            DISCUSSIONS_QUERY,
            {"owner": OWNER, "name": NAME, "categoryId": category_id, "cursor": cursor},
        )
        page = data["repository"]["discussions"]
        results.extend(page["nodes"])
        print(f"Fetched {len(results)} discussions so far...")
        if not page["pageInfo"]["hasNextPage"]:
            break
        cursor = page["pageInfo"]["endCursor"]  # the bookmark for the next page

    Path("data/discussions.json").write_text(
        json.dumps(results, indent=2), encoding="utf-8"
    )
    print(f"Saved {len(results)} answered discussions to data/discussions.json")


if __name__ == "__main__":
    main()
