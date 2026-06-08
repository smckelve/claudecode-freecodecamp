from read_members import read_members


def main() -> None:
    """Print a greeting, then list the first members from members.csv."""
    print("Hello from claudecode-freecodecamp!")
    try:
        for member in read_members():
            print(member["first_name"], member["last_name"], member["email"])
    except FileNotFoundError:
        print("Error: members.csv file not found.")


if __name__ == "__main__":
    main()
