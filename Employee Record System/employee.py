import json
import os

FILE_PATH = "employees.json"

# --------- File Handling Utilities ---------

def load_data():
    """Loads employee data from a JSON file safely."""
    if not os.path.exists(FILE_PATH):
        return []
    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            else:
                return []
    except json.JSONDecodeError:
        return []

def save_data(data):
    """Saves employee data to a JSON file."""
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)

def generate_id(data):
    """Generates a unique employee ID."""
    if not data:
        return 1
    return max(emp["id"] for emp in data) + 1

# --------- Core Operations ---------

def add_employee():
    data = load_data()
    print("\n--- Add Employee ---")
    name = input("Enter name: ").strip()
    age = input("Enter age: ").strip()
    dept = input("Enter department: ").strip()

    if not name or not age.isdigit() or not dept:
        print("❌ Invalid input. Please try again.\n")
        return

    employee = {
        "id": generate_id(data),
        "name": name,
        "age": int(age),
        "department": dept
    }
    data.append(employee)
    save_data(data)
    print("✅ Employee added.\n")

def list_employees():
    data = load_data()
    if not data:
        print("⚠️ No employees found.\n")
        return
    print("\n--- Employee List ---")
    for emp in data:
        print(f"ID: {emp['id']} | Name: {emp['name']} | Age: {emp['age']} | Department: {emp['department']}")
    print()

def update_employee():
    data = load_data()
    emp_id = input("Enter employee ID to update: ").strip()
    if not emp_id.isdigit():
        print("❌ Invalid ID.\n")
        return

    emp_id = int(emp_id)
    for emp in data:
        if emp["id"] == emp_id:
            print(f"Editing employee: {emp['name']}")

            name = input(f"New name (leave blank to keep '{emp['name']}'): ").strip()
            age = input(f"New age (leave blank to keep '{emp['age']}'): ").strip()
            dept = input(f"New department (leave blank to keep '{emp['department']}'): ").strip()

            if name:
                emp["name"] = name
            if age.isdigit():
                emp["age"] = int(age)
            if dept:
                emp["department"] = dept

            save_data(data)
            print("✅ Employee updated.\n")
            return

    print("❌ Employee not found.\n")

def delete_employee():
    data = load_data()
    emp_id = input("Enter employee ID to delete: ").strip()
    if not emp_id.isdigit():
        print("❌ Invalid ID.\n")
        return

    emp_id = int(emp_id)
    new_data = [emp for emp in data if emp["id"] != emp_id]
    if len(new_data) == len(data):
        print("❌ Employee not found.\n")
    else:
        save_data(new_data)
        print("✅ Employee deleted.\n")

# --------- Main Menu ---------

def main():
    while True:
        print("=== Employee Record System ===")
        print("1. Add Employee")
        print("2. List Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")
        choice = input("Choose an option (1–5): ").strip()

        if choice == "1":
            add_employee()
        elif choice == "2":
            list_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
