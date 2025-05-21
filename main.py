import json
import os


def create_record(name, email):
    return json.dumps({"name": name, "email": email}, indent=4)


def main():
    name = input("Enter name: ")
    email = input("Enter email: ")
    
    filepath = input("Enter filepath: ")
    
    if not os.path.exists(filepath):
        print("No DB found. Creating new DB.")
        with open(filepath, 'w') as file:
            file.write(create_record(name, email))
    else:
        with open(filepath, 'a') as file:
            file.write(create_record(name, email))

if __name__ == "__main__":
    main()