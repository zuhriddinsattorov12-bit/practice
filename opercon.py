'''
Operators
Conditions
Logical Operations
'''

print(" ==== Operators ====")
# + _ >= < <= * /.  //  %  +=  **

a = 19
b = 5 
steve =("steve")

print("a > b", a > b)
print("a * b", a * b)
print("a / b", a / b)

print(a / b)
result = a // b # butun> bo'lib beradi, nechta shu son borligi chiqyapti
left = a %  b # qoldig'ini chiqarib beradi
print(f"the result: {result} and left: {left}")


#a = a + 100
a += 100
print("a:", a)


print("b", b**2)
print("b", b**3)

#string
print("="*5)
print("steve:", steve *2)


# == >ikkita variableni o'zaro solishtiruvchi operator
c = dict(name="Martin", age=35)
d = dict(name="Martin", age=35)
e = c

print("c==d", c == d) # faqat object qiymatlari solishtiriladi


# id
print(id(c), id(d))


#  is > referance.ini tekshirish 
data = c is d 
print("c is d", data)

print("c is e", c is e)



print(" ==== Conditions ====") # conditionlar truthy yoki falsy qiymatni tekshiradi
x = 5

if x > 50:
    print("Case A")
elif x > 10:
    print("Case B")
else:
    print("Case C")


print("-----"*5)


print(" ==== Logical Operators ====")


age = 28
person = None

if age > 16:
    person = "Adult"
else:
    person = "child"

print("person:", person)


# Logical > Ternary Operator
person = "adult" if age > 18 else "minor"
print("person", person)


# and & or

is_student = True
is_admin = False
is_guest = True
is_parent = True

if not is_student:   # not > bo'lmasa ishlaydi
    print("Wellcome here, do you want to be student!")
elif is_admin:
    print("Please go to the Office!")
elif is_guest or is_parent:
    print("Waiting room is over there!")
else:
    print("other cases")