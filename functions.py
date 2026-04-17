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