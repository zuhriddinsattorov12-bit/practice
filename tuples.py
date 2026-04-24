''' Tuples
    (1) What is tuple: tuple vs list
    (2) Unpacking arguments
    (3) Zip
'''

print("====== What is tuple: tuple  vs list ======")
# Java/PHP/NodeJS > array.  & Python: List

# List > immutable
# literal
numbs = [3, 5, 1, 2]
car_dict = {"brand": "Ferrari", "year": 1995}

# constructor
letter = list("Hello World!")

fruits = ["apple", "lemon", "banana", "kivi"]
print("before fruits:", fruits)

fruits[2] = "melon"
print("after fruits:", fruits)


# tuple > mutable
animals = ("dog", "cat", "fish", "lion")
tuple_obj = ("MIT", 100, True, None)

print("animals:", animals)
# tuple o'z qiymatini o'zgartirmaydi
# animals[0] = "bird"


# Pythonda argumentlarni yoyishni tuplelar orqali amalga oshiramiz
print("====== Unpacking arguments ======")
groups = ["MIT", "Flexy", "DEVEX", "MG"]
# * yordamida bir nechta valuelarni olishimiz mumkin
(x, y, *z) = groups
print(f"the x: {x} and y: {y}")


# Pythonda tuplelarni qavssiz ham ishlatish mumkin
people = "Andrew", "John"
animals = "dog",


# *args > tuple
def calculate(*args):
    print("args >", args)
    total = 1
    for x in args:
        total *= x
    print(f"the total value: {total}")
    return total


# Call
calculate(1, 7, 2, 3)
print("=========")
calculate(0, 2, 300)
print("=========")
calculate(5, 7)


# **kwargs > dictionary orqali argumentlarni yoyish usuli
def introduce(**kwargs):
    print(f"the type(**kwargs) value: {type(kwargs)}")
    print(f"Hi, I am {kwargs["name"]} and I am {kwargs["age"]} years old!")


# foydalanayotgan argumentlarimizni miqdori nomalum bo'lsa dictionary unpacking kerak bo'ladi
# Call
introduce(name="Justin", age=28)
introduce(name="Shawn", age=38, single=True)