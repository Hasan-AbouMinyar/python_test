class up : 
    def __init__(self,name):
        self.name = name

class down(up):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")


sh = down("Hasan", 25)
print(sh.show())