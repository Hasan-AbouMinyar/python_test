class Str:
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"



o = Str("lana", 18)

print(o)  # This will call the __str__ method and print the formatted string