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

This repository hosts a collection of small experiments and tooling.

## codex CLI

Welcome to CODEX, an empty repository that now serves as a new home.
This repo can be a playground for experiments, tests, or any kind of
project you might want to build. Feel free to expand it as needed.


We provide a simple `codex` command that can send a prompt to the OpenAI API.
Install dependencies with `npm install` and run the script like so:


```bash
node bin/codex.js "Hello"
```

Set the `OPENAI_API_KEY` environment variable before use.

Check out `AGENTS-GUIDE.md` and the `AGENTS-EXAMPLE-*` files for tips on customizing the Codex agent. :sparkles:

## Tools

The repository now includes a simple prototype command line interface in
`codex_cli.py`. The script reads a configuration file from
`~/.codex/config.json`, looks up API keys from environment variables and
prints the chosen provider, model and prompt. Use `-c` to edit the
instructions file used by Codex.


The CLI will automatically load any `AGENTS.md` (or `codex.md`) file found in the
current project directory or its Git root and include it as additional context
for the model.

## Files

- `codex_cli.py` – CLI entry point.
- `requirements.txt` – Python dependencies (currently just `openai`).
- `AGENTS-GUIDE.md` – Guidance on creating `AGENTS.md` files.
- `AGENTS-EXAMPLE-*` – Example agent configurations.

Feel free to build on top of this codebase and adapt it to your needs.

## Tools

A minimal Python implementation of the Codex CLI lives in `codex_cli/`. It is inspired by the original [CODEX-CLI project](https://github.com/SYSTEMS-OPERATOR/CODEX-CLI) but greatly simplified.

```bash
pip install openai python-dotenv
python -m codex_cli --help
```

