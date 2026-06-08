import argparse
import csv


def read_members(path: str = "members.csv", limit: int = 10) -> list[dict[str, str]]:
    """Read member records from a CSV file.

    Args:
        path: Path to a CSV file. Each row's columns become dict keys.
        limit: Maximum number of records to return.

    Returns:
        A list of dicts, one per row, mapping each column name to its value.

    Raises:
        FileNotFoundError: If `path` does not exist.
    """
    with open(path, newline="") as file:
        reader = csv.DictReader(file)
        return [dict(row) for _, row in zip(range(limit), reader)]


def search_members(members: list[dict[str, str]], query: str) -> list[dict[str, str]]:
    """Filter members whose name or email contains `query` (case-insensitive).

    Args:
        members: Member records as returned by `read_members`.
        query: Substring to search for in `first_name`, `last_name`, and `email`.

    Returns:
        The subset of `members` with a case-insensitive match in any of those fields.
    """
    needle = query.casefold()
    return [
        member
        for member in members
        if needle in member.get("first_name", "").casefold()
        or needle in member.get("last_name", "").casefold()
        or needle in member.get("email", "").casefold()
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Read and search member records from a CSV file.")
    parser.add_argument("--path", default="members.csv", help="Path to the CSV file (default: members.csv)")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of records to read (default: 10)")
    parser.add_argument("--search", help="Only show members whose name or email contains this substring")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    try:
        members = read_members(args.path, args.limit)
    except FileNotFoundError:
        print(f"Error: {args.path} file not found.")
        return

    if args.search:
        members = search_members(members, args.search)

    for member in members:
        print(member["first_name"], member["last_name"], member["email"])


if __name__ == "__main__":
    main()
