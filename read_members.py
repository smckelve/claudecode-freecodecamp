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


def format_members_table(
    members: list[dict[str, str]],
    fields: tuple[str, ...] = ("first_name", "last_name", "email"),
) -> str:
    """Format members as an aligned table with a header row.

    Args:
        members: Member records as returned by `read_members`.
        fields: Which columns to include, and in what order.

    Returns:
        A multi-line string with a header row, separator, and one row per member.
        Each column is left-aligned and padded to the width of its longest value.
    """
    headers = [field.replace("_", " ").title() for field in fields]
    rows = [[member.get(field, "") for field in fields] for member in members]
    widths = [max([len(header)] + [len(row[i]) for row in rows]) for i, header in enumerate(headers)]

    def format_row(values: list[str]) -> str:
        padded = [value.ljust(width) for value, width in zip(values[:-1], widths[:-1])]
        return "  ".join(padded + [values[-1]])

    lines = [format_row(headers), "  ".join("-" * width for width in widths)]
    lines.extend(format_row(row) for row in rows)
    return "\n".join(lines)


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

    if members:
        print(format_members_table(members))


if __name__ == "__main__":
    main()
