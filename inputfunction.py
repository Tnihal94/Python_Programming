# # Input function in python

a = input()
print(a)

a = input()
print(a+a)

a = input()
print(int(a)+int(a))

name = input("Enter Your Name: ")
print(f"Welcome {name} to the Python Tutorial series")

age = input("Enter yor age: ")
print(f"I'm {age} years old now & next year i will be {int(age)+1} years old.")
 
x = input("Enter first number: ")
y = input("Enter second number: ")
print(f"Sum of {x} & {y} is {int(x) + int(y)}")

# # Home Work, W.A.P to input student name & marks of 3 subjects.
# # print name & percentage in output.

print("Percentage Calculator")
student_name = input("Enter Student's Name: ")
physics = input("Enter Physics marks: ")
chemistry = input("Enter chemistry marks: ")
maths = input("Enter Maths marks: ")
percentage = (int(physics)+int(chemistry)+int(maths))/300*100
print(f"Student name is {student_name} & the percentage is {int(percentage)} % ")


# #Optimizing solution :

print("Percentage Calculator")
student_name = input("Enter Student's Name: ")
physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter chemistry marks: "))
maths = int(input("Enter Maths marks: "))
percentage = ((physics+chemistry+maths)/300)*100
print(f"Student name is {student_name} & the percentage is {int(percentage)} % ")


# # Q.2 W.A.P that collects multiples types of data (e.g name,age,height, and student status)
# # from user input, store, them in  a dictionary.

user_data = {}

user_data['name'] = input("Enter Your Name: ")
user_data['age'] = int(input("Enter Your Age: "))
user_data['height'] = float(input("Enter Your Height: "))
user_data['Staus'] = input("Are you a student (Yes/No): ")
print(user_data)


num1 = input("Enter your first number: ")
num2 = input("Enter your second number: ")
num1_int = int(num1)
num2_int = int(num2)
sum = num1_int + num2_int
print("The sum of", num1_int, "and", num2_int, "is:",sum)

print(f"The sum of {num1_int} and {num2_int} is: {sum}")