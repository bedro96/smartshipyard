"""
Smart Shipyard Chat Agent
Foundry Local orchestration + MLX LLM backend via OpenAI-compatible API.
"""

import sys

from openai import OpenAI

# ANSI color codes
ORANGE = "\033[38;5;208m"
WHITE = "\033[97m"
GREEN = "\033[32m"
RESET = "\033[0m"

BASE_URL = "http://127.0.0.1:8080"
MODEL = "mlx-community/Qwen3-0.6B-MLX-4bit"

SYSTEM_PROMPT = (
    "You are a helpful Smart Shipyard assistant. "
    "You help users with shipyard operations, vessel construction, "
    "IoT sensors, workforce management, and manufacturing processes."
)


def main() -> None:
    client = OpenAI(base_url=BASE_URL, api_key="not-needed")

    messages: list[dict[str, str]] = [
        {"role": "system", "content": SYSTEM_PROMPT},
    ]

    print(f"{GREEN}Smart Shipyard Agent ready. Type 'exit' to quit.{RESET}\n")

    while True:
        try:
            user_input = input(f"{ORANGE}You > {WHITE}")
        except (EOFError, KeyboardInterrupt):
            print(f"\n{GREEN}Goodbye!{RESET}")
            break

        print(RESET, end="")

        if user_input.strip().lower() in {"exit", "quit"}:
            print(f"{GREEN}Goodbye!{RESET}")
            break

        if not user_input.strip():
            continue

        messages.append({"role": "user", "content": user_input})

        try:
            stream = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                stream=True,
            )

            print(f"{GREEN}Agent > ", end="", flush=True)

            assistant_reply = []
            for chunk in stream:
                delta = chunk.choices[0].delta
                if delta.content:
                    print(delta.content, end="", flush=True)
                    assistant_reply.append(delta.content)

            print(RESET)

            full_reply = "".join(assistant_reply)
            messages.append({"role": "assistant", "content": full_reply})

        except Exception as exc:
            print(f"{RESET}\n\033[31mError: {exc}\033[0m")


if __name__ == "__main__":
    main()