from employee import Employee
from employee_type import EmployeeType

class Organization:
    """
    Class representing the organization and its employee management system.
    """
    def __init__(self):
        self.employees = {}
        self.ceo = None

    def add_employee(self, name, department, age, employee_type, manager_id=None):
        """
        Adds a new employee to the organization.

        :param name: Name of the employee
        :param department: Department of the employee
        :param age: Age of the employee
        :param employee_type: Type of the employee (from EmployeeType Enum)
        :param manager_id: ID of the manager (if any)
        """
        if employee_type == EmployeeType.CEO and self.ceo:
            print("Organization can have only a single CEO")
            return

        if not age.isdigit():
            print("Wrong format for add employee command.\n\tage must be a number")
            return

        age = int(age)
        manager = self.employees.get(manager_id) if manager_id is not None else None

        if manager_id and not manager:
            print(
                "Wrong format for add employee command.\nExpected:\nadd_employee name department age type [manager_id]")
            return

        if not manager and employee_type != EmployeeType.CEO:
            print("Only CEO can have no manager.")
            return

        new_employee = Employee(name, department, age, employee_type, manager)
        self.employees[new_employee.id] = new_employee
        if employee_type == EmployeeType.CEO:
            self.ceo = new_employee

        print(f"Employee added successfully and was assigned id {new_employee.id}")

    def delete_employee(self, worker_id):
        """
        Deletes an employee from the organization by ID.

        :param worker_id: ID of the employee to be deleted
        """
        employee = self.employees.get(worker_id)
        if not employee:
            print("Employee with this id was not found.")
            return
        if employee.workers:
            print("Employee has reporters = can't delete")
            return
        if employee.manager:
            employee.manager.remove_worker(employee)
        del self.employees[worker_id]
        print(f"Employee with id {worker_id} deleted successfully")

    def assign_manager(self, worker_id, manager_id):
        """
        Assigns a new manager to an employee.

        :param worker_id: ID of the employee
        :param manager_id: ID of the new manager
        """
        employee = self.employees.get(worker_id)
        manager = self.employees.get(manager_id)

        if not employee or not manager:
            print("Wrong format for assign_manager command.")
            return

        if employee.manager:
            employee.manager.remove_worker(employee)

        employee.manager = manager
        manager.add_worker(employee)
        print(f"Assigned employee {worker_id} to manager {manager_id}")

    def print_org(self):
        """
        Prints the organization hierarchy from the CEO downward.
        """
        if not self.ceo:
            print("No employees in the organization.")
            return
        self._print_all(self.ceo, 0)
        """
        Recursively prints employees in a hierarchical structure.
        """
    def _print_all(self, employee, level):
        print("\t" * level + f"|--{employee}")
        for sub in employee.workers:
            self._print_all(sub, level + 1)

    def print_dep(self):
        """
        Prints employees grouped by department with count.
        """
        department = {}
        for worker in self.employees.values():
            if worker.department not in department:
                department[worker.department] = []
            department[worker.department].append(worker)

        print(f"Total number of employees = {len(self.employees)}")
        for key , value in department.items():
            print(f"{key} | number of employees = {len(value)}")
            for worker in value:
                print(f"\t|--{worker}")
