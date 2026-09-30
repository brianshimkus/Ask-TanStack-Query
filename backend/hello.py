import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

question = " ".join(sys.argv[1:]) or "In one sentence, what does TanStack Query do?"

response = client.responses.create(
    model=os.environ["ANSWER_MODEL"],
    input=question,
)

print(response.output_text)
print(
    f"\n(used {response.usage.input_tokens} tokens in, {response.usage.output_tokens} tokens out)"
)
