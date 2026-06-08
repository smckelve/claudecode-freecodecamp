# claudecode-freecodecamp

A small collection of Python exercises (CS50P / freeCodeCamp), managed with [uv](https://docs.astral.sh/uv/). Requires Python >= 3.14.

## Setup

```sh
git clone https://github.com/smckelve/claudecode-freecodecamp.git
cd claudecode-freecodecamp
uv sync
```

## Type checking

This project is type-hinted and checked with [mypy](https://mypy-lang.org/) in strict mode (configured in `pyproject.toml`):

```sh
uv run mypy main.py read_members.py
```

## Usage

### `read_members`

Reads member records from a CSV file. `members.csv` has columns `id`,
`first_name`, `last_name`, `email`, `gender`, `ip_address`, `member_id`,
`age`, `country`, `postal_code`, `favorite_color`, and `membership_status`.

Run it from the command line — prints the first 10 members from `members.csv`:

```sh
uv run read_members.py
```

Or import it as a function in your own code:

```python
from read_members import read_members

members = read_members("members.csv", limit=5)
for member in members:
    print(member["first_name"], member["last_name"], member["country"])
```

`read_members(path="members.csv", limit=10)` returns a list of dicts, one per
row, mapping each CSV column name to its value, and raises
`FileNotFoundError` if `path` does not exist.

### `main`

Prints a greeting, then lists the first members from `members.csv` via `read_members`:

```sh
uv run main.py
```
