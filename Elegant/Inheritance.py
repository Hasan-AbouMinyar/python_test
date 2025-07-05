class father:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Father's name is {self.name}")
    
class son(father):
    pass

o = son("John")
o.show()