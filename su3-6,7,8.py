class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    def print(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors
    def print(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Doors: {self.doors}")

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, engine_capacity):
        super().__init__(brand, model, year)
        self.engine_capacity = engine_capacity
    def print(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Engine capacity: {self.engine_capacity}")

print("--- Vehicles ---")
veh1 = Vehicle("Ford", "Transit", 2015)
veh2 = Vehicle("Volvo", "FH16", 2020)
veh1.print()
veh2.print()

print("\n--- Cars ---")
car1 = Car("Toyota", "Corolla", 2022, 4)
car2 = Car("BMW", "M3", 2023, 2)
car1.print()
car2.print()

print("\n--- Motorcycles ---")
moto1 = Motorcycle("Yamaha", "R1", 2021, 998)
moto2 = Motorcycle("Honda", "CBR600RR", 2019, 599)
moto1.print()
moto2.print()