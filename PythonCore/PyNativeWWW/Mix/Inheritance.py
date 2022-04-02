class vehicle:
    def __init__(self, mileage, cost):
        self.mileage = mileage
        self.cost = cost

    def show_vehicle_details(self):
        print("cost is ", self.cost)
        print("Mileage is ", self.mileage)


class car(vehicle):
    def __init__(self, mileage, cost, tyre, hp):
        super().__init__(mileage,cost)
        self.tyre = tyre
        self.hp = hp

    def show_car_details(self):
        print("cost", self.cost)
        print("mileage", self.mileage)
        print("tyre", self.tyre)
        print("hp", self.hp)


c1 = car(12, 450000, 4, 700)
c1.show_car_details()




