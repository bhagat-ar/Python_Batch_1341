class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary= salary

    def display_employee(self):
        print("Name :", self.name)
        print("Salary :", self.salary)

class Developer(Employee):

    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

    def display_developer_details(self):
        self.display_employee()
        print("Programming Language :", self.programming_language)

# create object of developer
d1= Developer("Aman",67000, "Java")
d2= Developer("Kriti", 34000, "Python")
d3= Developer("Yogesh", 57000, "Python")

d1.display_developer_details()
print()
d2.display_developer_details()
print()
d3.display_developer_details()