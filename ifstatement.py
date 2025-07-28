# Conditional statement in Python

# 1. if statement

# a = 26
# b = 108
# if b > a:                          # Condition is True
#     print("b is greater than a")


# a = 26
# b = 108
# if a > b:                            # Condition is False
#     print("a is greater than b")


# age = int(input("Enter your age: "))
# if age > 17:                             # For true condition
    # print("You are an adult")


# 2. if-else statement
# else handle false condition

# age = int(input("Enter your age: "))
# if age > 17:
#     print("You are an adult")
# else:
#     print("you are not an adult")


# temperature = 30
# if temperature < 32:
#     print("Its a cool day !")
# else:
#     print("Its a hot day !")

# temperature = 30
# temperature = int(input("Enter the temperature: "))
# if temperature <= 30:
#     print("Its a cool day !")
# else:
#     print("Its a hot day !")


# 3. if-elif-else statement
# multiple conditions

# marks = int(input("Enter your marks out of-100: "))
# if marks >= 90:
#     print("Grade: A+")
# elif marks >= 80:
#     print("Grade: A")
# elif marks >= 70:
#     print("Grade: B")
# elif marks >= 60:
#     print("Grade: C")
# else:
#     print("Grade: D")


# 4. Nested if-else condition statement
# if-else inside if-else statement
# multiple condition depend on each other

# number = int(input("Enter a number: "))
# if number > 0:
#     if number % 2 == 0:
#         print("The number is positive and even.")
#     else:
#         print("The number is positive and odd.")
# else:
#     if number == 0:
#         print("The number is zero.")
#     else:
#         print("The number is negative number.")


# 5. Condition Expressions (Ternary operator)

# age = 16
# status = "Major" if age >= 18 else "Minor"
# print(status)

# Home Work :
# (Q.1)  What is expected output and reason ?
# value = None
# if value:
#     print("Value is true.")
# else:
#     print("Value is false.")

# (Answer:1) 
# Value is False
# Reason: In python, the following values are considered as False in a boolean context:
#- None,False,0,0.0,'' (Empty string), [],{},(),(Empty list, dict, tuple)

# (Q.2) "Leap Year" Write a simple program to determine if a given year is a leap year using user input.
 # Note: Leap year occurs every 4 years
# A year is a leap year if it is divisible by 4, but not if it is dividible by 100, unless it is also divsible by 400.
# (Answer:2)

# User input:
# using if-else statement
# year = int(input("Enter the Year: "))
# if (year % 4 == 0 and (year % 100 != 0) or (year % 400 == 0)):
#     print(f"{year} is a Leap Year")
# else:
#     print(f"{year} is Not a Leap Year")
    

# using conditional expression (ternary operator)
# year = int(input("Enter the Year: "))
# result = "Leap Year" if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else "Not a leap Year"
# print(result)

# (Q.3) Login Authentication using condtional statement.
# Assume you have a predefined username and password.
# Write a program that prompts the user to enter a username
# Both username and password are correct.
# Username is correct but password is incorrect.
# Username is incorrect.

# (Answer: 3)

# Predefined Username and Password.
# predefined_username = 'Nihal' 
# predefined_password = 'Pass0008'

# # prompts the user to enter a username and password.
username = input("Enter Your username: ")
password = input("Enter Your password: ")

# # username and password match:
if username == predefined_username:
    if password == predefined_password:
        print("Welcome! You are Successfully Login")
    else:
        print("Incorrect Password")
else:
    print("Invalid username")        























    




    
