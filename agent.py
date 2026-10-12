import os
from typing import Dict, List

from litellm import completion

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError(
        "OPENAI_API_KEY is not set. "
        "Run: export OPENAI_API_KEY='sk-...'"
    )


def generate_response(messages: List[Dict[str, str]]) -> str:
    response = completion(
        model="openai/gpt-4o",
        messages=messages,
        max_tokens=1024,
    )
    return response.choices[0].message.content


messages = [
    {
        "role": "system",
        "content": "You are an expert software engineer that prefers functional programming.",
    },
    {
        "role": "user",
        "content": "Write a function to swap the keys and values in a dictionary.",
    },
]

print(generate_response(messages))