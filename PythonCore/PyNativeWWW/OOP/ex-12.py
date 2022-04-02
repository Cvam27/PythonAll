class Circle:
    def __init__(self, a, b, r):
        self.a = a
        self.b = b
        self.r = r

    def area(self):
        return 3.14 *(self.r**2)

    def perimeter(self):
        return 2*3.14*self.r

    def testBelong(self,x,y):
        formula = (x-self.a)**2 +(y-self.b)**2 - self.r**2
        if (formula==0):
            print("Belongs")
        else:
            print("Does not belong")

cercle = Circle(77,55,10)

cercle.testBelong(77,54)

