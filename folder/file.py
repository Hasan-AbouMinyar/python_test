file = open("json.txt", "a")
file.write("Hi there what in the world this is a test.\n")
file.close()

file = open("json.txt", "r")
me = file.read()
print(me)
file.close()