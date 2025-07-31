# # Arguments in Functions:

# # 1. Required arguments (single / multiple arguments)
# # (i)

def greetings(name):                 # name is a parameter(variable)
    print("Hello, " + name + "!")
greetings("Nihal")                   # Nihal is arguments(Value)
# # (ii) greetings()                 # Required an argument to run code   

# # (iii)

def intro(course_name, instructor_name):
    print("Welcome to ", course_name, "course_by", instructor_name)
intro("Python", "Mr. Nihal")

# 2. Default Arguments: 
def greetings(name = "world"):       # defaul value
    print("Hello, " + name + "!")   
greetings()                          # no arguments passed. runs without error using default value.  
greetings("Nihal")                   # overwrite on default value.


# 3. Keyword Arguments (named argument):

def divide (a,b):                      # a, b are 2 parameters                     
     return a/b

result = divide(100,20)                # positional arguments
print(result)


result2 = divide(a = 100,b = 20)       
print(result2)


# 4.(i) Arbitrary positional Arguments (*args):
# stores arguments as tuple.
# (i)
def add_numbers(a,b):
    return a+b
result = add_numbers(10,11)
print(result)

def add_3numbers(a,b,c):
    return a+b+c
result1 = add_3numbers(10,11,1)
print(result1)

# (ii)
def add_numbers(*args):
    print(type(args))
    return sum(args)

op = add_numbers(1,2,3,4)
print(op)

# (iii)
def greetings2(*names):
    for name in names:
        print(f"Hello, {name}!")

greetings2("Nihal",'Sharma', 'Yadav')


# 4. (ii) Arbitrary keyword Arguments (**kwargs):
# Note: stores arguments as dictionary (key value) format.

def print_details(**kwargs):
    print(type(kwargs))
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_details(name ="Nihal", age = 28, city = "Palwal")        