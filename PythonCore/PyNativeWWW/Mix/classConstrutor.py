class cars:
    def __init__(self, brand, typ, price):
        self.objBrand = brand
        self.objType = typ
        self.objPrice = price

    def print_car_details(self):
        print(self.objPrice)
        print(self.objType)
        print(self.objBrand)


c1 = cars("Honda", "Sedan", 1000000)
c1.print_car_details()
