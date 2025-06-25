# CODEX


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

## Tools

A minimal Python implementation of the Codex CLI lives in `codex_cli/`. It is inspired by the original [CODEX-CLI project](https://github.com/SYSTEMS-OPERATOR/CODEX-CLI) but greatly simplified.

```bash
pip install openai python-dotenv
python -m codex_cli --help
```
