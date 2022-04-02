class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity=60):
        return f"Seating capacity is {capacity} seats"

class Bus(Vehicle):
    def seating_capacity2(self, capacity):
        return  super().seating_capacity(capacity)


school_bus = Bus("Ashoka Layland", 30, 10)
print(school_bus.seating_capacity())