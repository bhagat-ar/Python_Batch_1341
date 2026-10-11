class Student:
    def __init__(self, name, rollno, course):
        self.name = name
        self.rollno = rollno
        self.course = course

    def display_student(self):
        print("Name : ",self.name )
        print("Roll No : ",self.rollno )
        print("Course Name : ",self.course )

# create three students object
s1 = Student("Arti", 101, "Python full stack")
s2 = Student("malini", 102, "Java full stack")
s3 = Student("priti", 103, "Data Science")

# display student details
s1.display_student()
print()
s2.display_student()
print()
s3.display_student()
