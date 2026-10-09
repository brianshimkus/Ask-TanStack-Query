"""Ways to cut a docs page into chunks (index cards)."""


def chunk_fixed(text, size=1500, overlap=200):
    """Day 3 baseline: cut every `size` characters, overlapping by `overlap` so edges aren't lost."""
    if not text:
        return []
    chunks = []
    start = 0
    while True:
        chunks.append(text[start : start + size])
        if start + size >= len(text):
            break
        start += size - overlap
    return chunks
