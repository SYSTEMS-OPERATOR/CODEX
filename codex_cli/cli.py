#!/usr/bin/env python3
"""Minimal Codex command line interface."""

import argparse
import os
from typing import List

try:
    from dotenv import load_dotenv
except ImportError:  # pragma: no cover - dependency optional
    load_dotenv = lambda: None

try:
    import openai
except ImportError:  # pragma: no cover - openai optional
    openai = None


def _create_completion(prompt: str, model: str) -> str:
    if openai is None:
        raise RuntimeError("openai package not installed")

    result = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    return result.choices[0].message["content"].strip()


def main(argv: List[str] | None = None) -> None:
    load_dotenv()

    parser = argparse.ArgumentParser(description="Interact with the Codex API")
    parser.add_argument("prompt", nargs="+", help="Prompt to send to Codex")
    parser.add_argument(
        "--model",
        default="gpt-4",
        help="Model name to use with the OpenAI Chat Completions API",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the prompt without sending a request",
    )

    args = parser.parse_args(argv)
    prompt = " ".join(args.prompt)

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY environment variable is not set")

    if args.dry_run:
        print(prompt)
        return

    openai.api_key = api_key
    try:
        output = _create_completion(prompt, args.model)
    except Exception as exc:  # pragma: no cover - network dependent
        raise SystemExit(f"Failed to call OpenAI API: {exc}") from exc

    print(output)


if __name__ == "__main__":  # pragma: no cover
    main()
