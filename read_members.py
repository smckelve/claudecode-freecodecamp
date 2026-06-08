import csv
import itertools

def read_members():
    try:
        with open("members.csv", newline="") as file:
            reader = csv.DictReader(file)
            for row in itertools.islice(reader, 10):
                print(row["first_name"], row["last_name"], row["email"])
    except FileNotFoundError:
        print("Error: members.csv file not found.")
    except Exception:
        print("Error: reading file: {e}")
        
if __name__ == "__main__":
    read_members()
