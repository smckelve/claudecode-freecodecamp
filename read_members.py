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


def main() -> None:
    try:
        for member in read_members():
            print(member["first_name"], member["last_name"], member["email"])
    except FileNotFoundError:
        print("Error: members.csv file not found.")


if __name__ == "__main__":
    main()
