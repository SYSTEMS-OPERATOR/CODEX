# Codex CLI

A lightweight command line interface inspired by OpenAI's `codex` tool. This version focuses on simplicity and is implemented in Python.

## Quickstart

Install the optional dependencies and run the CLI with a prompt:

```bash
pip install openai python-dotenv
python -m codex_cli "generate hello world in python"
```

Set your `OPENAI_API_KEY` environment variable or create a `.env` file with the variable defined. Use `--model` to target a specific model or `--dry-run` to print the prompt without contacting the API.
