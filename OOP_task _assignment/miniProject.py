class Employee:
    def __init__(self,emp_id, name, salary):
        self.emp_id= emp_id
        self.name = name
        self.salary= salary

    def display_info(self):
        print("Employee ID: ", self.emp_id)
        print("Name :", self.name)
        print("Salary :", self.salary)

class Developer(Employee):

    def __init__(self,emp_id, name, salary, programming_language):
        super().__init__(emp_id, name, salary)
        self.programming_language = programming_language

    def display_info(self):
        super().display_info()
        print("Role : Developer")
        print("Programming Language :", self.programming_language)

class Tester(Employee):
    def __init__(self,emp_id, name, salary, testing_tool):
        super().__init__(emp_id, name, salary)
        self.testing_tool = testing_tool

    def display_info(self):
        super().display_info()
        print("Testing tool :", self.testing_tool)

# create two object of developer
d1= Developer("D101","Aman",67000, "Java")
d2= Developer("D102","Kriti", 34000, "Python")
d3= Developer("D103","Yogesh", 57000, "Python")

# create two object of tester
t1= Tester("T101","Arush",65000,"Selenium")
t2= Tester("T102","kajal",39000,"Pytest")

# store all employees in a list
employees=[d1, d2, d3, t1, t2]

# display all employee details
for employee in employees:
    employee.display_info()
    print("< ------------------------------------------------- > ") 