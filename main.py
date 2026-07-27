import argparse
import os
from pydoc import cli

from dotenv import load_dotenv
from openai import OpenAI


def _arg_parsin() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User promp")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    return args


def returning_response(client, model, args):
    messages = [{"role": "user", "content": args.user_prompt}]
    response = client.chat.completions.create(model=model, messages=messages)
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        if response.usage is not None:
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
    print(f"Response:\n {response.choices[0].message.content}")


def main():
    load_dotenv()
    args = _arg_parsin()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )
    model = "openrouter/free"
    returning_response(client, model, args)


if __name__ == "__main__":
    main()
