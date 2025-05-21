import json
import os


def load_data(filepath):
    if not os.path.exists(filepath):
        return []
    with open(filepath, 'r') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return []


def save_data(filepath, data):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def create_record(name, email):
    return {"name": name, "email": email}


def main():
    name = input("Enter name: ")
    email = input("Enter email: ")
    filepath = input("Enter filepath: ")

    db = load_data(filepath)
    db.append(create_record(name, email))
    save_data(filepath, db)

    print(f"Record for {name} saved successfully!")


if __name__ == "__main__":
    main()
