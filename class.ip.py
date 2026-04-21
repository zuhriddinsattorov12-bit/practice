'''
Class deep diving
(1) ENCAPSULATION
(2) INHERITANCE
(3) POLIMORHPISM

'''
print(" ==== INHERITANCE =====")
# Parent > Child

class Animal:  #parent
     #state
    description = "The class creates animals"

    # constructor
    def __init__(self, voice):
        self.status = "animal is alive"
        self.voice = voice



        # method
    def make_voice(self):
        print(f"the animal can make voice: {self.voice}")


class Dog(Animal):   # Child
      # state


      # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)


      # method
    def introduce(self):
        print(f"{self.name} says {self.sound}-{self.sound}")

    def protect(self):
        print("yes, i can protect you")

#---------------------------------------------

class Cat(Animal):   # Child
      # state


      # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)


      # method
    def introduce(self):
        print(f"{self.name} says {self.sound}-{self.sound}")

    def play(self):
        print("Meow, Meow")


#-------------------------------------------

class Fish(Animal):   # Child
      # state


      # constructor
    def __init__(self, name, sound, voice):
        self.name = name
        self.sound = sound
        super().__init__(voice)


      # method
    def introduce(self):
        print(f"{self.name} says {self.sound}-{self.sound}")

    def swim(self):
        print("yes, i can swim")


dog = Dog("Rex", "wow", True)
cat = Cat("Tom", "meow", True)
fish = Fish("Nemo", "ZzZ ZzZ", True)  


dog.introduce()
cat.introduce()
fish.introduce()

print("=========")

print(dog.voice, fish.voice)

# status
print("dog.status:", dog.status)
print("cat.status:", cat.status)