class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        self.salary += amount
        print(f"{self.name}'s new salary after a raise of ${amount} is ${self.salary}.")

    def display_employee(self):
        print(f"Employee Name: {self.name}, Position: {self.position}, Salary: ${self.salary}")

employee = Employee("Michael Brown", "Project Manager", 80000)
employee.display_employee()
employee.give_raise(10000)
employee.display_employee()
