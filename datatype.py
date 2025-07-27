# # Data types in python
 
a = 1
b = 1
print(a+b)
print(type(a))  # checking data type: integer

c = "1"
d = "1"
print(c+d)
print(type(c))  # # checking data type: string

# # Basics data types in Python:
# # 1. Numeric
a1 = 1 # integer type
a2 = 1.5 # float type
print(type(a2))
a3 = complex(3,5)  # complex type
print(type(a3))

# # 2. Sequence
b1 = "Nihal"   # string type
print(type(b1))
b2 = [1,4,7,26,108,'Nihal']  # List type
print(type(b2))
b3 = (1,4,7,26,108,'Nihal')  # Tuple type
print(type(b3))

# # 3. Dicionary
my_dictionary = {'name': 'Tekchand', 'age': 30, 'City': 'Palwal'}   # dictionary type
print(type(my_dictionary))

# # 4. Sets
my_sets = {1,4,7,26,108,'Nihal'} # Set type
print(type(my_sets))

# # 5. Boolean
bool1 = True
print(type(bool1)) # Booleab type

# # 6. Binary
byte1 = b"Nihal"
print(type(byte1))

print("Python is fun.")
print('''"Quote" and 'Single quotes' can be tricky''')
print("\"Quote\" and 'Single quotes' can be tricky")

print("\"Quote\" and 'Single quotes' can be tricky")


print("Python is fun.\n\"Quote\" and 'Single quotes' can be tricky")

name = "Tekchand Nihal"
age = 26
city = "Palwal"
print("My name is", name, "from", city, "& I'm", age)
print(f"My name is {name} from {city} & I'm {age}")