'''
Class deep diving
(1) ENCAPSULATION
(2) INHERITANCE
(3) POLIMORHPISM

'''
print(" ==== ENCAPSULATION =====")
# ENCAPSULATION > public __private _protected


class Account():
    #state
    description = "the class makes bank accounts"

    #constructor
    def __init__(self, owner, amount):
        self.__owner = owner
        self.__amount = amount

    #method
    def get_balance(self):
        print(f"the owner {self.__owner} has {self.__amount} usd")

    def deposit(self, amount): 
        print("deposit", amount)
        self.__amount += amount

    def withdraw(self, amount):
        print("withdraw:", amount) 
        self.__amount -= amount

    @property
    def holder(self):
        return self.__owner  


my_account = Account("Shawn", 10000)
my_account.get_balance()

print("=====")
my_account.deposit(3500)
my_account.withdraw(400)
my_account.get_balance()

print("=====")
my_account.amount = 10000000
my_account.owner = "steve"
my_account.amount = 10000000
my_account.get_balance()


print("=====")

try:
    result = my_account.__amount
    print("result:", result)
except Exception as err:
    print("NO target state", err)


# holder

account_owner = my_account.holder 
print("account_owner:", account_owner)