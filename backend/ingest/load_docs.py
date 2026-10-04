"""Day 2: read the TanStack Query docs into data/docs.json.

Run from inside backend/:  uv run python -m ingest.load_docs
"""

import json
from pathlib import Path

REPO = Path("data/query-repo")
# The React docs, plus the shared reference pages (QueryClient, QueryCache, ...) that React users read too.
DOC_FOLDERS = [REPO / "docs" / "framework" / "react", REPO / "docs" / "reference"]
BASE_URL = "https://tanstack.com/query/latest/"


def split_frontmatter(raw):
    """Separate the '---' header block at the top of a docs file from the page text."""
    meta = {}
    body = raw
    if raw.startswith("---"):
        end = raw.find("\n---", 3)
        if end != -1:
            header = raw[3:end]
            body = raw[end + 4 :]
            for line in header.strip().splitlines():
                if ":" in line:
                    key, value = line.split(":", 1)
                    meta[key.strip()] = value.strip().strip("'\"")
    return meta, body.strip()


def page_url(path):
    """docs/framework/react/guides/queries.md -> https://tanstack.com/query/latest/docs/framework/react/guides/queries"""
    relative = path.relative_to(REPO).with_suffix("")
    return BASE_URL + relative.as_posix()


def main():
    docs = []
    for folder in DOC_FOLDERS:
        for path in sorted(folder.rglob("*.md")):
            meta, body = split_frontmatter(path.read_text(encoding="utf-8"))
            if "ref" in meta:
                # Some pages borrow their text from another file. Follow the reference.
                ref_path = REPO / meta["ref"]
                if ref_path.exists():
                    _, body = split_frontmatter(ref_path.read_text(encoding="utf-8"))
            if not body:
                print(f"Skipping empty page: {path}")
                continue
            docs.append(
                {
                    "title": meta.get("title", path.stem),
                    "url": page_url(path),
                    "text": body,
                }
            )

    Path("data/docs.json").write_text(json.dumps(docs, indent=2), encoding="utf-8")
    print(f"Saved {len(docs)} pages to data/docs.json")


if __name__ == "__main__":
    main()
