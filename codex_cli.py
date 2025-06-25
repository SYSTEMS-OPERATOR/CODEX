#!/usr/bin/env python3
"""Simplified Codex CLI inspired by the CODEX-CLI project.

This tool demonstrates how to load user instructions and optional project
documentation before sending a prompt to the OpenAI API. It is intentionally
minimal and serves as a starting point for our own tooling.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Optional

try:
    import openai  # type: ignore
except ImportError:  # pragma: no cover - dependency might be missing
    openai = None

CONFIG_DIR = Path.home() / ".codex"
CONFIG_PATH = CONFIG_DIR / "config.json"
INSTRUCTIONS_PATH = CONFIG_DIR / "instructions.md"

DEFAULT_MODEL = "gpt-4"
DEFAULT_INSTRUCTIONS = """# Codex instructions
Add any persistent instructions for the assistant here.
"""

PROJECT_DOC_FILENAMES = ["AGENTS.md", "codex.md", ".codex.md", "CODEX.md"]


def discover_project_doc(start_dir: Path) -> Optional[Path]:
    """Return path to project documentation if found."""
    dir_path = start_dir.resolve()
    while True:
        for name in PROJECT_DOC_FILENAMES:
            candidate = dir_path / name
            if candidate.exists():
                return candidate
        if (dir_path / ".git").exists():
            break
        if dir_path.parent == dir_path:
            break
        dir_path = dir_path.parent
    return None


def load_project_doc(cwd: Path) -> str:
    path = discover_project_doc(cwd)
    if not path:
        return ""
    try:
        return path.read_text("utf-8")
    except Exception:
        return ""


def load_config() -> dict:
    if not CONFIG_PATH.exists():
        return {"model": DEFAULT_MODEL}
    try:
        return json.loads(CONFIG_PATH.read_text("utf-8"))
    except Exception:
        return {"model": DEFAULT_MODEL}


def save_defaults() -> None:
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if not CONFIG_PATH.exists():
        CONFIG_PATH.write_text(json.dumps({"model": DEFAULT_MODEL}, indent=2))
    if not INSTRUCTIONS_PATH.exists():
        INSTRUCTIONS_PATH.write_text(DEFAULT_INSTRUCTIONS)


def call_openai(model: str, messages: list[dict]) -> str:
    if openai is None:
        raise RuntimeError("openai package is not installed")
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY environment variable not set")
    openai.api_key = api_key
    resp = openai.chat.completions.create(model=model, messages=messages)
    return resp.choices[0].message.content.strip()


def run_prompt(prompt: str, cwd: Path) -> None:
    cfg = load_config()
    save_defaults()
    instructions = INSTRUCTIONS_PATH.read_text("utf-8")
    project_doc = load_project_doc(cwd)
    system_message = "\n\n".join(
        [part for part in [instructions, project_doc] if part.strip()]
    )
    if system_message:
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt},
        ]
    else:
        messages = [{"role": "user", "content": prompt}]
    try:
        output = call_openai(cfg.get("model", DEFAULT_MODEL), messages)
    except Exception as exc:  # pragma: no cover - network errors
        sys.stderr.write(f"Error contacting OpenAI API: {exc}\n")
        sys.exit(1)
    print(output)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Minimal Codex CLI")
    parser.add_argument("prompt", nargs="?", help="Prompt for the assistant")
    parser.add_argument(
        "--init",
        action="store_true",
        help="Initialise configuration files and exit",
    )
    args = parser.parse_args(argv)

    if args.init:
        save_defaults()
        print(f"Configuration written to {CONFIG_PATH}")
        return 0

    if not args.prompt:
        parser.error("prompt argument required unless --init is used")

    run_prompt(args.prompt, Path.cwd())
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main(sys.argv[1:]))
