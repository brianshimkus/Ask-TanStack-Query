"""Day 3: cut the docs into chunks, embed each chunk, and save them to Supabase.

Run from inside backend/:  uv run python -m ingest.embed
"""

import json

from app.clients import EMBEDDING_MODEL, openai_client, supabase

from ingest.chunking import chunk_fixed

BATCH_SIZE = 50


def build_rows(docs):
    rows = []
    for doc in docs:
        for piece in chunk_fixed(doc["text"]):
            rows.append(
                {"doc_url": doc["url"], "doc_title": doc["title"], "content": piece}
            )
    return rows


def main():
    with open("data/docs.json", encoding="utf-8") as f:
        docs = json.load(f)
    rows = build_rows(docs)
    print(f"{len(docs)} pages -> {len(rows)} chunks")

    # Empty the table first so old chunks don't mix with new ones.
    supabase.table("chunks").delete().gte("id", 0).execute()

    for i in range(0, len(rows), BATCH_SIZE):
        batch = rows[i : i + BATCH_SIZE]
        resp = openai_client.embeddings.create(
            model=EMBEDDING_MODEL, input=[r["content"] for r in batch]
        )
        for row, item in zip(batch, resp.data):
            row["embedding"] = item.embedding
        supabase.table("chunks").insert(batch).execute()
        print(f"  saved {i + len(batch)} of {len(rows)} chunks")

    print("Done! Open the Table Editor in Supabase to look at your chunks.")


if __name__ == "__main__":
    main()
