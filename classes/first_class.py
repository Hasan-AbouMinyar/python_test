class car:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")


c1 = car("Toyota", "Corolla", 2020)
c1.name = "Honda"
c1.display_info()