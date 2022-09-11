class Group:
    def __init__(self, name, students):
        self.name = name
        self.students = students

    def add_student(self, student):
        self.students.append(student)

    def __iter__(self):
        return iter(self.students)

    def __len__(self):
        return len(self.students)

    def __getitem__(self, item):
        return self.students[item]

    def __contains__(self, item):
        return item in self.students

    def __str__(self):
        return "Group " + self.name + " with students " + str(', '.join([i.name for i in self.students]))

class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.age = age
        self.surname = surname

    def get_grade(self):
        return self.grade

    def __str__(self):
        return '''Name: {}
Surname: {}
Age: {}'''.format(self.name, self.surname, self.age)


group = Group("Python", [Student("John", "Smith", 20), Student("Bob", "Dylan", 21)])
group.add_student(Student("Alice", "Cooper", 19))
print(group)