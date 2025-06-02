import argparse
from services import employee_service as es

def run_cli():
    print("👋 Welcome to Employee Management CLI!")
    print("Type 'help' to see commands or 'exit' to quit.\n")

    while True:
        user_input = input("Enter command: ").strip()
        print(user_input,"before checking input")
        if user_input.lower() == "exit":
            print("👋 Goodbye!")
            break

        if user_input.lower() == "help":
            print("""
Commands:
  add <ID> <Name> <Age> <Dept> <Salary>    Add an employee
  delete <ID>                              Delete employee by ID
  filter [--salary <salary>] [--department <dept>]   Filter employees
  list                                    List all employees
  export <json|csv>                        Export employees to file
  exit                                    Exit the program
""")
            continue
        print(user_input.split(),"after checking input")
        # Split input into args like a shell
        args = user_input.split()

        if not args:
            continue

        cmd = args[0].lower()

        try:
            if cmd == "add" and len(args) == 6:
                emp_id, name, age, dept, salary = args[1:]
                es.add_employee(int(emp_id), name, int(age), dept, int(salary))
                print("✅ Employee added.")

            elif cmd == "delete" and len(args) == 2:
                es.delete_employee(int(args[1]))
                print(f"✅ Deleted employee with ID {args[1]}.")

            elif cmd == "filter":
                # Parse optional filters
                salary = None
                department = None
                i = 1
                while i < len(args):
                    if args[i] == "--salary" and i+1 < len(args):
                        salary = int(args[i+1])
                        i += 2
                    elif args[i] == "--department" and i+1 < len(args):
                        department = args[i+1]
                        i += 2
                    else:
                        i += 1

                filtered = es.filter_employee(salary, department)
                if filtered:
                    for emp in filtered:
                        print(emp)
                else:
                    print("⚠️ No employees matched the filter.")

            elif cmd == "list":
                all_emps = es.list_employees()
                if all_emps:
                    for e in all_emps:
                        print(e)
                else:
                    print("⚠️ No employees found.")

            elif cmd == "export" and len(args) >= 2:
                file_type = args[1].lower()
                filename = args[2] if len(args) > 2 else None
                es.export_employees(file_type, filename)

            else:
                print("❌ Invalid command or wrong arguments. Type 'help' for commands.")

        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    # Load existing employees from file (optional if you add load function)
    # es.load_employees()

    run_cli()
