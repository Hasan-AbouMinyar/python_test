from car import car


class ElectricCar(car):
    def __init__(self, name, model, year, color, num_doors, price, battery_capacity):
        super().__init__(name, model, year, color, num_doors, price)
        self.battery_capacity = battery_capacity

    def display_info(self):
        super().display_info()
        print(f"Battery Capacity: {self.battery_capacity} kWh")