from read_members import format_members_table, read_members


def main() -> None:
    """Print a greeting, then list the first members from members.csv."""
    print("Hello from claudecode-freecodecamp!")
    try:
        members = read_members()
    except FileNotFoundError:
        print("Error: members.csv file not found.")
        return

    if members:
        print(format_members_table(members))


if __name__ == "__main__":
    main()
