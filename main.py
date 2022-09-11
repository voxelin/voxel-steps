class Dog:
    def __init__(self, name,age,weight):
        self.name = name
        self.age = age
        self.weight = weight
    def bark(self):
        print("Woof!")
    def eat(self,food):
        print("Yum!")
    def chase_cat(self):
        print("I got the cat!")
    def __str__(self):
        return " Name: " + self.name + "\n Age: " + str(self.age) + "\n Weight: " + str(self.weight)

dog = Dog("Fido", 3, 60)
print(dog)
