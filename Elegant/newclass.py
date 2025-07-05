class bild:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def good(self):
        print(f"your name is {self.name} and your age is {self.age}")


c = bild("ahmed",62)
c.good()