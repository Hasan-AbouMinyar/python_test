# Example 2: With Inheritance

# --- Defining a Parent Class ---
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Move!")

# --- Defining Child Classes that inherit from Vehicle ---

class Car(Vehicle):
    pass  # The Car class will inherit everything from Vehicle without changes

class Boat(Vehicle):
    # This class overrides the move() method from the parent
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    # This class also overrides the move() method
    def move(self):
        print("Fly!")

# --- Creating Objects ---
car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

# --- Loop to print attributes and call the move() method ---
print("\n--- Output from Example 2 ---")
for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()