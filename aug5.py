# 1)float datatype
f= 10.0
print(type(f))

# 2)input - build-in function
num = input("enter the num = ")
print(num)
print(type(num))
print(id(num))
print("*********************************************")

# TASK1 : Identity card: Accept data for your id card from console
Name = input("enter the name : ")
Age = input("enter the age :")
City =input("enter the city :")
DOB = input("enter the date of birth :")
College =input("enter the name of college :")
Blood_Group = input("enter the blood group :")

print("*********************************************")
print("---------------MY ID CARD------------------")
print("Name :", Name )
print("Age :" , Age)
print("City :", City)
print("DOB :",DOB)
print("College :",College)
print("Blood_Group :", Blood_Group)
print("*********************************************")


# TASK2 : MEMORY DETECTIVE : Accept data for id card from console
print("*********************************************")

Name = input("enter the name : ")
Age = input("enter the age :")
City =input("enter the city :")
DOB = input("enter the date of birth :")
College =input("enter the name of college :")
Blood_Group = input("enter the blood group :")

print(id(Name))
print(id(Age))
print(id(City))
print(id(DOB))
print(id(College))
print(id(Blood_Group))


