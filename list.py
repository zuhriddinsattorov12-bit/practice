'''List
   (1) Working with lists
   (2) List methods > mutable: append()  insert() pop()  remove()  clear()  sort()  del()  clear()
    immutable: index() sorted
   (3) Lambda function > Anonym function (boshqa tillarda)
   (4) enumerate, map and filter
'''

# Java/PHP/NodeJS > array.  & Python: List]

# literal 
person = {"name": "Justin", "age": 25}  # dictionary
people = ("Andrew", "John", "Michael")  # tuple
groups = ["MIT", "FLEXY", "DEVEX", "MG"]  # list 
for team in groups:
    print(f"the team: {team}")

# constructor
result = list("Hello World!")
print(f"the result : {result } and size: {len(result )}")



print("-----")
fruits = ["apple", "orange", "lemon", "kivi"]

a = fruits[0]    # 0 - indexni olib beradi
b = fruits[0:2] # [0,2]  0 dan 2gacha indexni olib beradi, 2ni emas
c = fruits[::3] # ::3 boshidagi va oxiridagi indexni olib beradi
d = fruits[::-1] # ::-1 hamma indexni olib beradi


print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)


print("==== List methods ====")
#  mutable:

#  append() 
#  insert()
#  pop() 
#  remove() 
#  clear() 
#  sort()   
#  del() 
#  clear()

#  immutable:

#  index()
#  sorted

letter = ["a", "d", "b"]

# append > index oxiriga qo'shib beradi
letter.append("c")  
print(f"the append result: {letter}")


# insert > index boshiga qo'shib beradi, nechanchi indexga qo'yishini yozish kerak!
letter.insert(0, "z")
print(f"the insert result: {letter}")


#  len > hajmini bilib beradi 
#  pop > oxiridagi indexni olib tashlaydi
size = len(letter) - 1
result = letter.pop(size)
print(f"the  pop result: {letter}")


print("=========")
animals = ["dog", "cat", "capybara", "fish", "lion"]
print("animals:", animals)

# remove > indexni o'chirib tashlaydi
animals.remove("lion")
print("remove:", animals)

# del > indexni olib tashlaydi & structurasi biroz boshqacha
del animals[2:4]
print("del:", animals)

# index > listdagi biror value bor yoki yo'qligi haqida ma'lumot beradi
exist = animals.index("cat")
print("cat exist:", exist)

# clear > listdagi barcha ma'lumotlarni o'chirib yuboradi
animals.clear()
print("the clear result:", animals)

if "cat" in animals:
    print("index of cat:", animals.index("cat"))
else:
    print("cat does not exist")


    # sort > indexlarni tartiblaydi
print("======")
numbers = [2, 20, 12, 8, 57]
numbers.sort()
print("sorted nembers:", numbers)

# sort(reverse=True) > katta sonlarni oldiga olib tartiblaydi
numbers.sort(reverse=True)
print("sort reverse:", numbers)

# immutable sorted > indexni o'zgartirib yubormaydi, faqat yangi functionni o'zgartiradi
numbs = [2, 20, 12, 100]
new_numbs = sorted(numbs)
print(f"the sorted numbs: {numbs} and new_numbs: {new_numbs}")


# Lambda Function > small anonymous function
def calculate(x, y): return x * y


result = calculate(3, 5)
print("result:", result)

# lambdaning asosiy kuchi > ikkala valueni ham alohida chiqarib beradi
people = [
    ("Robert", 20),
    ("Steve", 19),
    ("Joseph", 25),
    ("Michael", 30),
    ("Ali", 40)
]  # ismlarni bosh harfi bo'yicha sort qiladi
people.sort()
print("people(1)", people)

# sort by age via lambda
people.sort(key=lambda person: person[1])
print("people2", people)


print("==== enumerate, map, filter ==== ")
# enumerate > valuelarni indexi bilan tuple ko'rinishida olib beradi
animals = ["dog", "cat", "fish"]
for element in enumerate(animals):
    print("elements:", element)

print("--------")
for (index, value) in enumerate(animals):
    print(f"the index: {index} and value: {value}")


# similar in dictionaries 
# items yordamida listdagidek amaliyotni dictionary uchun ham qilish mumkin
car_obj = dict(brand="Ferrari", year=2025) # dict
result = car_obj.items()
for (key, value) in result:
    print(f"the key: {key} and the value: {value} ",)


print("======")
# map 
# cars = [
#     ("Ferrari", 78),
#     ("Toyota", 87),
#     ("Audi", 116),
#     ("BMW", 109),
#     ("Pagani", 33)
# ]

# new_cars = []
# for car in cars:
#     new_cars.append(car[0])
# print("new car1:", new_cars)

# result_map = map(lambda car: car[0], cars)
# print(f"the result1: {result_map} and type: {type(result_map)}")

# new_cars = list(result_map)
# print("new_cars2", new_cars)


print("====== Filter =====")
cars = [
    ("Ferrari", 78),
    ("Toyota", 87),
    ("Audi", 116),
    ("BMW", 109),
    ("Pagani", 33)
]



result_map = map(lambda car: car[0], cars)
print(f"the result_map: {result_map} and type: {type(result_map)}")
new_cars = list(result_map)
print("new_cars2", new_cars)

print("=======")
# filter
result_filter = filter(lambda car: car[1] > 80, cars)
print(f"the result filter: {result_filter} and type: {type(result_filter)}")