amg = ("good", "bad", "ugly","beautiful","bad")

so = len(amg)

print(so)

print (amg[0])
print (amg[1:3])
print (amg[-1])
print (amg[1:])

if "good" in amg:
    print ("yesss")

e = list(amg)
e.append("new item")

amg = tuple(e)

print(amg)
my_list = [10, 20, 30, 20, 40, 20]

# إزالة كل 20
my_list = [item for item in my_list if item != 20]

print(my_list)

