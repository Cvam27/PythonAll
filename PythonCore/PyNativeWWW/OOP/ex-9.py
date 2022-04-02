class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        peri = 2*(self.length + self.width)
        return peri

    def area(self):
        ar = self.length * self.width
        return ar

    def display(self):
        print(self.length, self.width, self.perimeter(), self.area())

class Parallel(Rectangle):
    def __init__(self, height, length, width):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        vol = self.length * self.height * self.width
        return vol

obj = Parallel(20, 30, 40)
print(obj.volume())
obj.display()
