''' Comprehention
    (1) What is comprehension & list comp.
    (2) set and dictionary comp.
'''

print("===== What is comprehension & list comp. =====")
# Comprehension acts like spread operator!

''' Comprehension general syntax:
    a) *iterable  > 
    b) <expression> for item in iterable               > 
    c) <expression> for item in iterable <condition>   > filter 
'''

# list comp.
numbers = [1, 2, 4, 2, 1, 20]  # a version
list_numbers = [*numbers]      # [*numbers]  > comprehension
print("list_numbers:", list_numbers)
print(numbers is list_numbers)  # is > ....mi ?
print(id(numbers), id(list_numbers)) # id

print("========")
people = [("Robert", 20), ("Steve", 19), ("Joseph", 25)]
list_people = [person[0]for person in people] # b version
print("list_people:", list_people)

print("====== C version >= Filter =====")
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]
list_cars = [car[0] for car in cars if car[1] > 80]      # c version
print("list_cars:", list_cars)


print("===== Set and comprehension  =====")
numbs = [1, 5, 4, 20, 4, 5, 1, 4]
set_numbers = {*numbs}

dict_people = {person[0]: person[1] for person in people}
print("dict_people:", dict_people)