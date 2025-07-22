
class car:
    def __init__(self, name, model, year, color, num_doors, price):
        self.name = name
        self.model = model
        self.year = year
        self.color = color
        self.num_doors = num_doors
        self.price = price

    def display_info(self):
        print(f"Car Name: {self.name}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Color: {self.color}")
        print(f"Number of Doors: {self.num_doors}")
        print(f"Price: ${self.price}")

    def change_color(self, new_color):
        self.color = new_color
        print(f"Color changed to: {self.color}")


c1 = car("Toyota", "Corolla", 2020, "Red", 4, 20000)
c1.display_info()
c1.change_color("Blue")