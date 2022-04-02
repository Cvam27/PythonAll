class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage= mileage

    def show_vehicle_data(self):
        print("Vehicle name:", self.name )
        print("Max Speed is: ", self.max_speed)
        print("Mileage is : ", self.mileage)

class Bus(Vehicle):
    pass

schhol_bus = Bus("Ferrari ki sawari", 1000, 100)
schhol_bus.show_vehicle_data()



