import random

class Pet:
    info = "Pets are animals that humans keep for companionship"

    def __init__(self):
        print("I am a cute pet")

class Dog(Pet):
    info = "Humans best friend"

    def __init__(self, name):
        super().__init__()
        print("I am a cute dog")
        self.lucky_number = random.randint(1, 100)
        self.name = name

    def bark(self):
        print(f"Woof my name is {self.name} and my lucky number is {self.lucky_number}")


dog1 = Dog("Nikki")
dog2 = Dog("Charlie")

dog1.bark()
dog2.bark()

class Animal:
    amount = 25
    
    def __init__(self, race):
        self.race = race
        self.lucky_number = random.randint(1, 10)

    def introduce(self):
        print(f"I am a {self.race} and my age is {self.lucky_number}")

Animal1 = Animal("Dog")
Animal2 = Animal("Cat")

Animal1.introduce()
Animal2.introduce()

print(dog1.info)


#New example

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old")

class Student(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

    def introduce(self):
        super().introduce()
        print(f"I am a student and my grade is {self.grade}")

class Bad_student(Student):
    def introduce(self):
        super().introduce()
        print("I am a bad student")

class Good_student(Student):
    def introduce(self):
        super().introduce()
        print("I am a good student")

student1 = Bad_student("Jane", 20, "sophomore")
student2 = Good_student("John", 21, "junior")

student1.introduce()

student2.introduce()

