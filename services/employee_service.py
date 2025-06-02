from models.employee import Employee as employee
import os
import json
import csv

employees = []

def add_employee(emp_id,name,age,department,salary):
    emp = employee(emp_id,name,age,department,salary)
    employees.append(emp)
    
def list_employees():
    return [emp.to_dict() for emp in employees]

def delete_employee(emp_id):
   global employees
   employees = [emp for emp in employees if emp.emp_id != emp_id]

def filter_employee(salary,department):
    results = employees

    if salary is not None:
        results = [emp for emp in results if emp.salary >= salary]

    if department is not None:
        results = [emp for emp in results if emp.department.lower() == department.lower()]

    return results

def export_employees(file_type="json", filename=None):
    if not os.path.exists("data"):
        os.makedirs("data")

    if file_type not in ["json", "csv"]:
        print("❌ Supported file types: json or csv")
        return

    # Default filenames
    if not filename:
        filename = f"employees.{file_type}"

    filepath = os.path.join("data", filename)

    # Convert all employees to list of dictionaries
    data = [emp.to_dict() for emp in employees]

    if file_type == "json":
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        print(f"✅ Exported to {filepath}")

    elif file_type == "csv":
        with open(filepath, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        print(f"✅ Exported to {filepath}")
