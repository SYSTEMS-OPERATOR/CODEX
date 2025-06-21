# CODEX Agents Guide

This guide explains how to use `AGENTS.md` files with the CODEX
system. An `AGENTS.md` file contains instructions that influence how
CODEX behaves when modifying a repository. These instructions can cover
coding conventions, testing steps, or even how pull request messages
should look.

## 1. Purpose

The primary goal of an `AGENTS.md` file is to give repository-specific
rules to the CODEX agent. It allows project maintainers to specify
what checks the agent should run, how code should be formatted, or any
other task that needs to occur automatically during an update.

## 2. Placement and Scope

`AGENTS.md` files can appear anywhere in a repository. The file affects
the directory that contains it and all subdirectories. If multiple
`AGENTS.md` files exist at different levels, the deepest one takes
precedence for files under its directory.

## 3. Format

`AGENTS.md` is written in standard Markdown. You can organize
instructions with headings, bullet lists, or code blocks. Keep the
content clear and concise so the agent can interpret it easily.

```
# Example Layout
- Use bullet points for step lists
- Provide short explanations
- Include commands in fenced code blocks
```

## 4. Standard Prompting Techniques

Below are common ways to guide the agent using an `AGENTS.md` file:

- **Testing**: List commands the agent should run after making changes.
- **Formatting**: Specify formatting tools, such as `black` or
  `prettier`, to enforce style rules.
- **Commit Messages**: Describe how commit messages should be
  structured, including any prefixes or maximum lengths.
- **Pull Request Notes**: If special instructions are needed for pull
  request summaries, include them here.

## 5. Advanced Techniques

For more complex workflows, you can provide additional details:

- **Custom Scripts**: Instruct the agent to run project-specific
  scripts. Example: `./scripts/update_docs.sh`.
- **Environment Setup**: If tests require a setup step, explain the
  necessary commands.
- **Selective Behavior**: Mention when certain instructions should be
  skipped or overridden, such as disabling tests for documentation-only
  changes.
- **Nested Rules**: Use separate `AGENTS.md` files in subdirectories to
  override or extend behavior for specific parts of the project.
- **Message Templates**: Define how commit messages or pull request
  summaries should be structured.
- **Error Handling**: Tell the agent what to do if a command fails, such
  as noting that tests could not run due to environment limitations.

## 6. Example Files

The repository includes example files (`AGENTS-EXAMPLE-1.md` and
`AGENTS-EXAMPLE-2.md`) that demonstrate how an `AGENTS.md` might look
in practice. These samples showcase both basic and advanced features.
Additional examples (`AGENTS-EXAMPLE-3.md` and `AGENTS-EXAMPLE-4.md`)
highlight message templates, environment setup, and conditional rules.

Use these examples as a starting point when creating your own
`AGENTS.md` to guide CODEX in your projects.
