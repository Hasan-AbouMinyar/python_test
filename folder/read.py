file = open("json.txt", "r")
me = file.read(25)
print(me)


so = file.readline()
print("Next line:")

print(so)

file.close()