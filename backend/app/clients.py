"""Shared setup. Loads your .env file once and creates the API clients every other file uses."""

import os

from dotenv import load_dotenv
from openai import OpenAI
from supabase import create_client

load_dotenv()

# Model names live in .env so you can switch models without touching code.
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
ANSWER_MODEL = os.environ["ANSWER_MODEL"]
JUDGE_MODEL = os.getenv("JUDGE_MODEL", ANSWER_MODEL)
RERANK_MODEL = os.getenv("RERANK_MODEL", "rerank-v4.0-fast")

# Which retrieval setup the app uses by default (you'll change these on Days 9 and 10).
RETRIEVAL_MODE = os.getenv("RETRIEVAL_MODE", "vector")  # "vector" or "hybrid"
USE_RERANKER = os.getenv("USE_RERANKER", "false").lower() == "true"

openai_client = OpenAI()  # finds OPENAI_API_KEY automatically
supabase = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_SECRET_KEY"])
