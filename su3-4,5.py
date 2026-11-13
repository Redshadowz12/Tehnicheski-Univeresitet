class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    def print(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}")

class Manager(Employee):
    def __init__(self, name, position, salary, department):
        super().__init__(name, position, salary)
        self.department = department
    def print(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}, Department: {self.department}")

e1 = Employee("Martin Tonev", "Junior Dev", 2000)
e2 = Employee("Maria Petrova", "Designer", 2800)
e3 = Employee("Georgi Dimitrov", "Marketing Agent", 2100)
e1.print()
e2.print()
e3.print()

m1 = Manager("Nikola Baliev", "Sales Manager", 4800, "Sales Department")
m2 = Manager("Nikola Drinkov", "IT Manager", 5500, "IT Department")
m1.print()
m2.print()