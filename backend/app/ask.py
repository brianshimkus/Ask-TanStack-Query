"""Ask a question from the terminal.

Run from inside backend/:  uv run python -m app.ask "How do I refetch when the window regains focus?"
"""

import sys

from app.pipeline import answer_question


def main():
    if len(sys.argv) < 2:
        print('Usage: uv run python -m app.ask "your question"')
        sys.exit(1)

    question = " ".join(sys.argv[1:])
    result = answer_question(question)

    print(result["answer"])
    print("\nSources:")
    for i, chunk in enumerate(result["chunks"], start=1):
        print(f"  [{i}] {chunk['doc_title']} - {chunk['doc_url']}")
    print(
        f"\n({result['latency_s']}s, {result['input_tokens']} tokens in, {result['output_tokens']} tokens out)"
    )


if __name__ == "__main__":
    main()
