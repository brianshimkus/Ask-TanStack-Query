"""The librarian: finds the chunks most likely to answer a question."""

from app.clients import EMBEDDING_MODEL, openai_client, supabase


def embed_query(question):
    """Turn the question into meaning-numbers, using the SAME model as the chunks."""
    resp = openai_client.embeddings.create(model=EMBEDDING_MODEL, input=question)
    return resp.data[0].embedding


def vector_search(question, vector, k):
    res = supabase.rpc(
        "match_chunks", {"query_embedding": vector, "match_count": k}
    ).execute()
    return res.data


def retrieve(question, k=5, mode="vector", use_reranker=False):
    if mode != "vector" or use_reranker:
        raise ValueError(
            "Only vector search exists so far. Hybrid search arrives on Day 9, reranking on Day 10."
        )
    vector = embed_query(question)
    chunks = vector_search(question, vector, k)
    return [
        {
            "id": c["id"],
            "doc_url": c["doc_url"],
            "doc_title": c["doc_title"],
            "content": c["content"],
        }
        for c in chunks
    ]
