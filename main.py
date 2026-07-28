import argparse
import json
import os
import sys

from dotenv import load_dotenv
from openai import OpenAI

from functions.call_function import available_functions, call_function
from prompts import system_prompt


def _arg_parsin() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User promp")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    return args


def returning_response(client: OpenAI, model, args):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
    ]
    response = client.chat.completions.create(
        model=model, messages=messages, tools=available_functions
    )
    for _ in range(20):
        if args.verbose:
            print(f"User prompt: {args.user_prompt}")
            if response.usage is not None:
                print(f"Prompt tokens: {response.usage.prompt_tokens}")
                print(f"Response tokens: {response.usage.completion_tokens}")
        print(f"Response:\n {response.choices[0].message.content}")
        message = response.choices[0].message
        messages.append(message)
        if message.tool_calls == None:
            return
        for tool_call in message.tool_calls or []:
            # function_args = json.loads(tool_call.function.arguments or "{}")
            result_message = call_function(tool_call, args.verbose)
            # if result_message["content"] == "":
            #    raise Exception("Empty content")
            if args.verbose:
                print(f"-> {result_message['content']}")
            else:
                print(result_message["content"])
            messages.append(result_message)
        response = client.chat.completions.create(
            model=model, messages=messages, tools=available_functions
        )

    sys.exit(1)


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
