class Parent:
    def get_name(self, name):
        self.name = name

    def show_name(self):
        return self.name

class child(Parent):
    def get_age(self, age):
        self.age = age

    def show_age(self):
        return self.age

class grandchild(child):
    def get_gender(self, gender):
        self.gender = gender

    def show_gender(self):
        return self.gender


family = grandchild()
family.get_age(15)
family.get_gender("Male")
family.get_name("Tester")
print(family.show_gender())

