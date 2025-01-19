class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"{self.name} is {self.age} and had a grade of {self.grade}"

students = [Student("Cecilia", 20, 100), Student("Luis", 21, 90), Student("Carlos", 19, 85), Student("Ana", 20, 95), Student("Tini", 18, 65)]

poor_performance = []
for each in students:
    if each.grade < 70:
        poor_performance.append(each)

filter_poor = list(filter(lambda each: each.grade < 70, students))

filter_outstanding = list(filter(lambda each: each.grade >= 90, students))

filter_ok = list(filter(lambda each: each.grade >= 80 and each.grade < 90, students))

print(poor_performance)
print(filter_poor)
print(filter_outstanding)
print(filter_ok)

#exercise

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filter_even = list(filter(lambda each: each % 2 == 0, numbers))

print(filter_even)