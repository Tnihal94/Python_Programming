# # Example:(1)
# # Function Without Parameter :

# # Create or define function.
# def greetings():
#     print("Welcome to Python Course")
# # call function (use function).
# greetings()

# # Example:(2)
# # Create a function to add 2 numbers.
# # Function With Parameter :
# def add2numbers(a,b):  # parameter (a,b)
#     result = a+b
#     print("The sum is: ", result)
# # call above sum function.
# add2numbers(5,3) # arguments (5,3)

# # Example:(3)
# # Create function with return statement :
# def add(a,b):
#     return a+b
#    # return a-b  after return statement function end.
# result = add(15,5)
# print(result)

# Example:(4)
# # function to convert celsius to Fahrenheit:- with return statement
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     return fahrenheit

# # call function.
# temp_f = celsius_to_fahrenheit(25)
# print(temp_f)
# print("with return: ", type(temp_f))

# # Example:(5)
# # function to convert celsius to Fahrenheit:- without return statement
# def celsius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9/5) + 32
#     print(fahrenheit)

# # call function.
# temp_f2 = celsius_to_fahrenheit(50)
# print("without return: ", type(temp_f2))

# # Example:(6)
# # Pass statement:
# def dfskdfklsdfk():
#     pass
# def kdkdmvkdmvdd(): # code to be updated later
#     pass
# print("Hello!")
 

user_input1 = int(input("Enter your first Number: "))
user_input2 = int(input("Enter your Second Number: "))

sum = (user_input1+user_input2)
print(sum)


