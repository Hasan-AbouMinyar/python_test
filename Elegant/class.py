class Me:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
        

i = Me("Hasan", 25)

i.greet()
# print(i.greet())
print(i)