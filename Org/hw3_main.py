from organization import Organization
from employee_type import EmployeeType

company = Organization()

while True:
    command = input("Please enter a command:\n").strip().split()
    if not command:
        continue

    com = command[0]

    if com == "welcome":
        print("WELCOME!")
        print("submitter1: Dolev Atik dolev5454@gmail.com 206576555")
        print("submitter2: Yahav Vituri yahav78988@gmail.com 211521554")
    elif com == "add_employee":
        """
        Adds a new employee to the organization.
        Expected format: add_employee name department age type [manager_id]
        """
        if len(command) < 5:
            print("Wrong format for add employee command.\nExpected:\nadd_employee name department age type [manager_id]")
            continue
        name = command[1]
        department = command[2]
        age = command[3]
        work_type = command[4]

        if work_type not in EmployeeType.__members__:
            print("Wrong format for add employee command.\nExpected:\nadd_employee name department age type [manager_id]")
            continue

        employee_type = EmployeeType[work_type]
        manager_id = int(command[5]) if len(command) == 6 else None
        company.add_employee(name, department, age, employee_type, manager_id)

    elif com == "delete_employee":
        """
        Deletes an employee from the organization by ID.
        Expected format: delete_employee employee_id
        """
        if len(command) != 2 or not command[1].isdigit():
            print("Wrong format for delete_employee command.")
            continue
        company.delete_employee(int(command[1]))

    elif com == "assign_manager":
        """
        Assigns a new manager to an employee.
        Expected format: assign_manager employee_id manager_id
        """
        if len(command) != 3 or not command[1].isdigit() or not command[2].isdigit():
            print("Wrong format for assign_manager command.")
            continue
        company.assign_manager(int(command[1]), int(command[2]))

    elif com == "print_org":
        """
        Prints the full organization hierarchy.
        """
        company.print_org()

    elif com == "print_dep":
        """
        Prints employees grouped by department.
        """
        company.print_dep()

    elif com == "quit":
        break

    else:
        print(f"The command {com} is unknown.")
