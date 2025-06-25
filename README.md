# CODEX

This repository contains a lightweight Python implementation of a Codex-like CLI.
It draws inspiration from the official [CODEX-CLI](https://github.com/SYSTEMS-OPERATOR/CODEX-CLI)
project but is intentionally minimal and easy to extend.

## Quick start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set `OPENAI_API_KEY` in your environment.
3. Run the CLI with a prompt:
   ```bash
   python codex_cli.py "Write a short poem about the sea"
   ```
4. To generate default configuration and instructions files run:
   ```bash
   python codex_cli.py --init
   ```

The CLI will automatically load any `AGENTS.md` (or `codex.md`) file found in the
current project directory or its Git root and include it as additional context
for the model.

## Files

- `codex_cli.py` – CLI entry point.
- `requirements.txt` – Python dependencies (currently just `openai`).
- `AGENTS-GUIDE.md` – Guidance on creating `AGENTS.md` files.
- `AGENTS-EXAMPLE-*` – Example agent configurations.

Feel free to build on top of this codebase and adapt it to your needs.
