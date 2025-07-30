# Q:-Write a python program to create a (calculator) that can perform atleast five different
# mathematical operations such as addition, subtraction, multiplication, division, and average
# ensure that the program is user-friendly, prompting, for input and displaying the result clearly.

# Solution:-
# Python program to create a simple Calculator :

# Three steps to build Calculator.
# 1. Function for operations
# 2. User Input
# 3. print sesult

# Step-1:
# Function to add two numbers:
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers:
def sub(num1, num2):
    return num1 - num2

# Function to multiply two numbers:
def mul(num1, num2):
    return num1 * num2

# Function to divide two numbers:
def divide(num1, num2):
    return num1 / num2

# Function to average of two numbers:
def avg(num1, num2):
    return (num1 + num2)/2

# Step-2:
# User Input:

print("Please select operaton:\n " \
        "1. Addition\n" \
        "2. Subtraction\n" \
        "3. Multiplication\n" \
        "4. Division\n" \
        "5. Average\n")

select = int(input("Select a operation from 1,2,3,4,5: "))
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

# Step-3:
# Print the result:

# if select == 1:
#     print(number1, "+", number2, "= ", \
#           add(number1,number2))
    
# elif select == 2:
#     print(number1, "-", number2, "= ", \
#           sub(number1,number2))
    
# elif select == 3:
#     print(number1, "*", number2, "= ", \
#           mul(number1,number2))

# elif select == 4:
#     print(number1, "/", number2, "= ", \
#           divide(number1,number2))

# elif select == 5:
#     print("(",number1, "+", number2, ")", "/", "2", "= ", \
#           avg(number1,number2))
    

# <****************************** OR **********************************>

if select == 1:
    print("Addition of two numbers: =", add(number1,number2))

elif select == 2:
    print("Subtraction of two numbers: =", sub(number1,number2))


elif select == 3:
    print("Multiplication of two numbers: =", mul(number1,number2))

elif select == 4:
    print("Division of two numbers: =", divide(number1,number2))    

elif select == 5:
    print("Average of two numbers: =", avg(number1,number2))    

else:
    print("Invalid Operation! Plesae Select again")    
