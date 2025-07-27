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
#     print("You are an adult")


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


#     temperature = int(input("Enter the temperature: "))
# if temperature >=30:
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

# age = 17
# status = "Major" if age >= 18 else "Minor"
# print(status)

# Home Work :

# value = None
# if value == None:
#     print("Value is true.")
# else:
#     print("Value is false.")


year = int(input("Enter the Year: "))
result = "Leap Year" if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)) else "Not a leap Year"
print(result)