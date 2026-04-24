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