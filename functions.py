'''
Functions 
(1) Define vs Call
(2) Parametr vs Argument
(3) Keyworc & default arguments
(4) Scope

'''

print("======= Define vs Call =======")
# built in function > print() type()
# Function - reusable block of code
# Instead of block {} in Java, Python uses indentation!


# define 
def greet(a):
    print(f"how do you do, {a}")


# call - execute
result1 =  greet('Martin')
print("result1", result1)


print("====== Keyword & default arguments =======")


# define
def give_greet(name, age=28):
    print("give_greet is executed")
    return f"Hi {name}, you are {age} years old!"


# call
result3 = give_greet(name="Justin")
print("result3:", result3)