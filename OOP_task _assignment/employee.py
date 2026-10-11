class Employee:
    def __init__(self, emp_id, emp_name, emp_department, emp_salary):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_department = emp_department
        self.emp_salary = emp_salary

    def display_employee_details(self):
        print("Employee id :", self.emp_id)
        print("Employee Name :", self.emp_name)
        print("Employee Department :", self.emp_department)
        print("Employee Salary :", self.emp_salary)

# create employee objects
e1 = Employee(101, "Arti", "IT", 60000)
e2 = Employee(102, "Ketan", "HR", 64000)
e3 = Employee(103, "Revati", "Finance", 50000)
e4 = Employee(104, "Karan", "Sales", 45000)

# display employee details
e1.display_employee_details()
print()
e2.display_employee_details()
print()
e3.display_employee_details()
print()
e4.display_employee_details()
print()      