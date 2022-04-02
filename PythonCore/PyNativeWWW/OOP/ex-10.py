class Person:
    def __init__(self, name, age):
        self.name= name
        self.age = age

    def display(self):
        print(f"Name is {self.name}, Age is {self.age}")

class Student(Person):
    def __init__(self, name, age, section):
        Person.__init__(self, name, age)
        self.section = section

    def display_student(self):
        print(f"Name is {self.name}, Age is {self.age} and Section is {self.section}")


human = Person("Manas", 28)
human.display()
student = Student("Shivangi", 50, "A")
student.display_student()