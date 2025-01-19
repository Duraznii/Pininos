class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        #return f"{self.name} is {self.age} and had a grade of {self.grade}"
        return f"{self.name}"
    
students = [Student("Cecilia", 20, 100), Student("Luis", 21, 90), Student("Carlos", 19, 85), Student("Ana", 20, 95), Student("Tini", 18, 65)]

grades_total = 0
for each in students:
    grades_total += each.grade

print(grades_total)

from functools import reduce

grades_total_r = reduce(lambda total, each: total + each.grade, students, 0)

print(grades_total_r)
print(grades_total_r / len(students))   
print(round(grades_total_r / len(students)))

#exercise

numbers = [1, 2, 3, 4, 5]

numbers_product = reduce(lambda total, each: total * each, numbers, 1)

print(numbers_product)

numbers_product = reduce(lambda total, each: total * each, numbers)

print(numbers_product)

#CODE CHALLENGE!

#filter_m = list(filter(lambda each: each.name % 2 == 0, numbers))




filtered_names = list(filter(lambda each: each.name.startswith('C'), students))

print(filtered_names)