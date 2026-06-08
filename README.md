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

## Tests

Tests are written with [pytest](https://docs.pytest.org/):

```sh
uv run pytest
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

Command-line options:

```sh
uv run read_members.py --path members.csv --limit 25 --search ada
```

- `--path`: path to the CSV file (default: `members.csv`)
- `--limit`: maximum number of records to read (default: `10`)
- `--search`: only show members whose `first_name`, `last_name`, or `email` contains this substring (case-insensitive)

Or import the functions in your own code:

```python
from read_members import read_members

members = read_members("members.csv", limit=5)
for member in members:
    print(member["first_name"], member["last_name"], member["country"])
```

`read_members(path="members.csv", limit=10)` returns a list of dicts, one per
row, mapping each CSV column name to its value, and raises
`FileNotFoundError` if `path` does not exist.

`search_members(members, query)` filters a list of member dicts (as returned
by `read_members`) down to those whose `first_name`, `last_name`, or `email`
contains `query`, matching case-insensitively.

`format_members_table(members, fields=("first_name", "last_name", "email"))`
formats member dicts as an aligned table (header row, separator, and one row
per member, with each column padded to its widest value) and returns it as a
string. Both `read_members.py` and `main.py` print members this way.

### `main`

Prints a greeting, then lists the first members from `members.csv` via `read_members`:

```sh
uv run main.py
```
