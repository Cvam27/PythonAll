class calc():
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self,a,b):
        return a * b

    def div(self,a,b):
        return a / b


a = int(input("Enter 1st value"))
b = int(input("Enter second value"))
real_calc = calc()

print("Addition is ", real_calc.sum(a, b))
print("Subtraction is ", real_calc.sub(a, b))
