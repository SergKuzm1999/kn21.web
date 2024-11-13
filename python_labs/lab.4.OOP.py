class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def input_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)  
        self.battery_capacity = battery_capacity  

class HybridCar(Car):
    def __init__(self, brand, model, year, fuel_type, battery_capacity):
        super().__init__(brand, model, year)
        self.fuel_type = fuel_type
        self.battery_capacity = battery_capacity


generic_car = Car("Toyota", "Corolla", 2020)
electric_car = ElectricCar("Tesla", "Model S", 2022, 100)
hybrid_car = HybridCar("Toyota", "Prius", 2021, "Petrol", 50)

generic_car.input_info()
electric_car.input_info()
hybrid_car.input_info()