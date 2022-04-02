class Vehicle:
    def __init__(self, seating_capacity, type):
        self.seating_capactiy = seating_capacity
        self.type = type

    def default_fare(self):
        default_fare1 = self.seating_capactiy*100
        return default_fare1

class Bus(Vehicle):
    def bus_fare(self):
        a = super().default_fare()
        for_bus = int(a + a/10)
        return for_bus

class Car(Vehicle):
    pass

vh1 = Bus(50, "bus")
vh2 = Car(4, "car")


type = (input("Please enter type of vehicle either Bus/Car: "))
if type == "bus" or "BUS":
    print(vh1.bus_fare())
else:
    print(vh2.default_fare())

