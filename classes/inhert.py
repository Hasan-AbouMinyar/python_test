class father:
    def __init__(slif,name ):
        slif.name = name



class son(father):
    def __init__(slif, name, addres):
        super().__init__(name)
        slif.addres = addres
    
    def __str__ (silf):
        return f"Name: {silf.name}, Address: {silf.addres}"


f = son("Abouminyar", "Libya")

print(f)
    
