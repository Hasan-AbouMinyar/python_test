# Example 1: Without Inheritance

# --- Defining Classes Separately ---

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

# --- Creating Objects ---
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# --- Loop to call the move() method on each object ---
print("--- Output from Example 1 ---")
for x in (car1, boat1, plane1):
    x.move()