
class Employee:
    """
      Represents an employee in an organization.
      """
    _id_counter = 0

    def __init__(self, name, department, age, emp_type, manager=None):
        """
        Initializes an Employee instance.

        :param name: Name of the employee
        :param department: Department of the employee
        :param age: Age of the employee
        :param emp_type: Type of the employee (from EmployeeType Enum)
        :param manager: Manager of the employee (if any)
        """
        self.id = Employee._id_counter
        Employee._id_counter += 1
        self.name = name
        self.department = department
        self.age = age
        self.type = emp_type
        self.manager = manager
        self.workers = []

        if manager:
            manager.add_worker(self)

    def add_worker(self, employee):
        """
        Adds a worker (direct report) to this employee.

        :param employee: Employee instance to be added as a worker
        """
        self.workers.append(employee)

    def remove_worker(self, employee):
        """
        Removes a worker (direct report) from this employee.

        :param employee: Employee instance to be removed
        """
        self.workers.remove(employee)

    def __str__(self):
        """
         Returns a string representation of the employee.
         """
        return f"{self.type.name} | {self.department} | {self.id} | {self.name} - {self.age}"
