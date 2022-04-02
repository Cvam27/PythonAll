class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"capacity of {self.name} is {capacity}"


class bus(vehicle):
    def bus_detail(self, capacity=50):
        return super().seating_capacity(capacity=50)


b1 = bus("Tata", 30, 100)
print(b1.bus_detail())
