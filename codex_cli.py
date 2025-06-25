import argparse
import json
import os
import subprocess
from pathlib import Path

CONFIG_DIR = Path.home() / '.codex'
CONFIG_FILE = CONFIG_DIR / 'config.json'
INSTRUCTIONS_FILE = CONFIG_DIR / 'instructions.md'
DEFAULT_MODEL = 'codex-mini-latest'


def load_config() -> dict:
    """Load the CLI configuration from ~/.codex/config.json."""
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text())
        except Exception:
            return {}
    return {}


def get_api_key(provider: str = 'openai') -> str:
    """Retrieve the API key for a provider from the environment."""
    env_key = f'{provider.upper()}_API_KEY'
    return os.getenv(env_key, '')


def open_instructions_file() -> None:
    """Open the instructions file in the user's preferred editor."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if not INSTRUCTIONS_FILE.exists():
        INSTRUCTIONS_FILE.write_text('# Add your custom instructions here\n')
    editor = os.getenv('EDITOR', 'vi')
    subprocess.run([editor, str(INSTRUCTIONS_FILE)])


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description='Simple Codex CLI prototype')
    parser.add_argument('prompt', nargs='?', help='prompt to send to the model')
    parser.add_argument('-m', '--model', help='model to use')
    parser.add_argument('-p', '--provider', default='openai', help='completion provider')
    parser.add_argument('-c', '--config', action='store_true', help='edit instructions file and exit')

    args = parser.parse_args(argv)

    if args.config:
        open_instructions_file()
        return 0

    config = load_config()
    model = args.model or config.get('model', DEFAULT_MODEL)
    provider = args.provider or config.get('provider', 'openai')

    api_key = get_api_key(provider)
    if not api_key:
        print(f'Missing API key for provider {provider}. Set {provider.upper()}_API_KEY.')
        return 1

    prompt = args.prompt
    if not prompt:
        print('No prompt provided.')
        return 1

    print('--- Codex CLI Prototype ---')
    print(f'Provider: {provider}')
    print(f'Model: {model}')
    print(f'Prompt: {prompt}')
    print('This is a placeholder implementation.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
