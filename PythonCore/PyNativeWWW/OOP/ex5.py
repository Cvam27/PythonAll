class Vehicle:

    def __init__(self, name, max_speed, mileage, color="White"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color
    def vehicle_details(self):
        return print(f"Color is {self.color}, Vehicle name {self.name}, speed {self.max_speed} and mileage {self.mileage}")

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

object_bus = Bus("Volvo", 110, 7, "Black")
object_car = Car("Porsche", 250, 4)

object_bus.vehicle_details()
object_car.vehicle_details()

