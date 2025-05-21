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


def get_next_id(data):
    if not data:
        return 1
    return max(record.get("id", 0) for record in data) + 1


def create_record(record_id, name, email):
    return {"id": record_id, "name": name, "email": email}


def main():
    name = input("Enter name: ")
    email = input("Enter email: ")
    filepath = input("Enter filepath: ")

    db = load_data(filepath)
    next_id = get_next_id(db)

    db.append(create_record(next_id, name, email))
    save_data(filepath, db)

    print(f"Record #{next_id} for {name} saved successfully!")


if __name__ == "__main__":
    main()
