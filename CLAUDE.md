# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

A small Python learning project (CS50P / freeCodeCamp exercises) managed with `uv`. Requires Python >= 3.14, no external dependencies.

## Commands

- Run the main script: `uv run main.py`
- Run a specific script: `uv run read_members.py`
- Sync/install the environment: `uv sync`

There are no configured lint, build, or test commands/frameworks in this repo.

## Structure

- `main.py` — entry point with a `main()` function (currently a placeholder).
- `read_members.py` — standalone script that reads `members.csv` (a CSV of member records with `first_name`, `last_name`, `email` columns) and prints the first 10 rows using `csv.DictReader`.
- `members.csv` — sample data file used by `read_members.py`.

Each `.py` file is an independent, runnable script (guarded by `if __name__ == "__main__":`) rather than parts of a single application — there is no shared module structure to track across files yet.
