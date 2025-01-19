class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

students = [Student("Cecilia", 20, 100), Student("Luis", 21, 90), Student("Carlos", 19, 85), Student("Ana", 20, 95), Student("Tini", 18, 65)]

students_records = []
for each in students:
    #if each.grade >= 90:
     #   students_records.append(f"{each.name} is {each.age} and had an outstanding performance")
    #elif each.grade >= 80:
     #   students_records.append(f"{each.name} is {each.age} and had an ok performance")
    #else:
      #  students_records.append(f"{each.name} is {each.age} and had a poor performance")

    students_records.append(f"{each.name} is {each.age} and had an outstanding performance") if each.grade >= 90 else students_records.append(f"{each.name} is {each.age} and had an ok performance") if each.grade >= 80 else students_records.append(f"{each.name} is {each.age} and had a poor performance")

print(students_records)

#map_records = list(map(lambda each: each.name, students))

map_records = list(map(lambda each: f"{each.name} is {each.age} and had an outstanding performance" if each.grade >= 90 else f"{each.name} is {each.age} and had an ok performance" if each.grade >= 80 else f"{each.name} is {each.age} and had a poor performance", students))

print(map_records)

#Exercise

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Double_numbers = list(map(lambda each: each * 2, numbers))

print(Double_numbers)
