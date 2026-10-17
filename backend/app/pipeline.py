"""The whole assistant in one function: the librarian finds chunks, the friend writes the answer."""

import time

from app.clients import RETRIEVAL_MODE, USE_RERANKER
from app.generate import generate
from app.retrieve import retrieve


def answer_question(question, mode=None, use_reranker=None, model=None):
    start = time.perf_counter()
    chunks = retrieve(
        question,
        mode=mode or RETRIEVAL_MODE,
        use_reranker=USE_RERANKER if use_reranker is None else use_reranker,
    )
    result = generate(question, chunks, model=model)
    return {
        "answer": result["text"],
        "chunks": chunks,
        "input_tokens": result["input_tokens"],
        "output_tokens": result["output_tokens"],
        "latency_s": round(time.perf_counter() - start, 2),
    }
