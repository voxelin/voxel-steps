import statistics


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

    def get_students(self):
        for i in self.students:
            print('''Name: {}
Surname: {}
Age: {}
Grades: {}
Avg: {}
'''.format(i.name, i.surname, i.age, ','.join([str(i) for i in i.grades]), round(statistics.mean(i.grades))))
class Student:
    def __init__(self, name, surname, age, grades):
        self.name = name
        self.age = age
        self.surname = surname
        self.grades = grades
    


group = Group("Python", [Student("John", "Smith", 20, [11,12,12,3,4,5,6]), Student("Bob", "Dylan", 21,[1,2,3,4,5])])
group.add_student(Student("Alice", "Cooper", 19,[10,12,12,3,4,5,6]))
print(group.get_students())