'''List
   (1) Working with lists
   (2) List methods
   (3) Lambda function
   (4) enumarate, map and filter
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