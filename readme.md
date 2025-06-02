
# 🧑‍💼 Employee Management CLI (Python)

A command-line application built in Python to manage employees using object-oriented programming and core Python modules.

---

## 🚀 Features

- Add, delete, and list employees
- Filter employees by salary and department
- Export employee data to JSON or CSV
- Interactive CLI with command-based interface
- Uses OOP (inheritance, `__repr__`, `to_dict` methods)
- File handling with `os`, `json`, and `csv`

---

## 📁 Project Structure

ini-py/
│
├── main.py # CLI interface
├── data/ # Exported files (JSON/CSV)
├── models/
│ ├── person.py # Base class Person
│ └── employee.py # Employee inherits from Person
│
└── services/
└── employee_service.py # Business logic for employee actions



---

## 🛠️ How to Run

```bash
python main.py
This will open an interactive CLI. You can type commands like:



add <ID> <Name> <Age> <Dept> <Salary>       Add an employee
delete <ID>                                 Delete by employee ID
list                                        List all employees
filter --salary <val> --department <dept>   Filter employees
export <json|csv>                           Export employees
help                                        Show commands
exit                                        Exit CLI
📦 Dependencies
Python 3.8+

No external libraries (uses standard library only)

💡 Example Commands
bash

add 101 Alice 30 HR 60000
add 102 Bob 25 IT 75000
list
filter --salary 65000
export json
📂 Sample Output
json

[
    {
        "emp_id": 101,
        "name": "Alice",
        "age": 30,
        "department": "HR",
        "salary": 60000
    }
]
🧠 Concepts Covered
Python OOP: classes, inheritance, __init__, __repr__

File I/O: JSON and CSV

Functional programming: list comprehensions, filters

CLI interaction with input() and command parsing

Directory handling with os

🧹 Future Improvements
Load from file on startup

Save after each change

Pagination or sorting

Better error handling

🙌 Author
Swapnil Nanavati
Built in a week to master Python for backend interviews.