
# AGENTS Example 2

This example demonstrates a more involved configuration.

- Lint the project with `flake8`.
- Run `pytest --cov` for test coverage.
- Execute `./scripts/update_readme.sh` after tests pass.
- Commit messages should reference an issue number, e.g., `Fix #12: short description`.
- Summaries for pull requests must include a list of the commands executed.

# Advanced AGENTS.md Example

This example showcases more complex instructions and placeholders.

## Build Steps
- Run `make lint` to check code style.
- Run `make test` to execute the test suite.

## Fallback Behavior
- If `make test` fails due to missing dependencies, include the disclaimer
  provided in the AGENTS guide in the PR.

## PR Message Guidelines
- Begin the PR body with a one-sentence summary.
- Provide a bullet list of major changes.
- Attach test output or note why tests could not run.

