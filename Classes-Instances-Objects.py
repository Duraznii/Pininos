import random

class Dog:
    info = "Humans best friend"

    def __init__(self, name):
        print("I am a dog")
        print(random.randint(1, 100))
        self.lucky_number = random.randint(1, 100)
        self.name = name

print(Dog.info)

dog1 = Dog("Nikki")
dog2 = Dog("Charlie")

print(dog1.name)
print(dog2.name)

class Cat:
    def __init__(self, name):
        self.name = name

    def meow(self):
        print("Meow")


cat1 = Cat("Whiskers")
cat1.meow()
print(cat1.name)

class Animal:
    amount = 25

my_pets = Animal()
my_pets.race = "Dog"
