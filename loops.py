'''
Loop Operators
(1) for
(2) break/else
(3) while
'''

print("==== Loop Operators =====")
# Iterable objects > string, dict, tuple, list, map, filter
text = "MIT"
numbs = [10, 7, 3, 4]
cars_obj = dict(brand="Ferrari", year=2025)
range_obj = range(5)

for letter in text:
    print(f"the letter: {letter}")

    print("--------------")

for number in numbs:
    print(f"the numbers: {numbs}")

    print("--------------")
for x in range_obj:
    print(f"the element: {x}")


# key yordamida objectdagi keylarni,  get orqali valuelarni olishimiz mumkin ekan
    print("--------------")
for key in cars_obj:
    print(f"the keys:{key} => value: {cars_obj.get(key)}")


    print("------- break & else -------")
for x in range(1, 20, 5):
    print(f"the x: {x}")
    if x > 10:
        print("reached break")
        break
else:
    print("Looped Successfully!")


    print("------ while operator --------")
nuss = 40
while nuss > 0:
    nuss -= 10
    print(f"the nuss equals: {nuss}")


    # Pythonda > while True = (do while) in  JS, C++  ...
    print("--------------")
count = 0
while True:
    count += 1
    x = int(input("find number"))

    if x == 41:
        print(f"you found number in {count} steps")
        break
    else:
        print("wrong, please try again!")