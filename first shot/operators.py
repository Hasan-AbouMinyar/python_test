a =10
b = 3
c = a + b
d = a - b
e = a * b
f = a / b
g = a % b
h = a ** b
i = a // b

print("Addition:", c)
print("Subtraction:", d)
print("Multiplication:", e)
print("Division:", f)
print("Modulus:", g)
print("Exponentiation:", h)
print("Floor Division:", i)

age = 25
pas= True

if age >= 18 and pas:
    print("You are an adult and have a passport.")
if age < 18 or not pas:
    print("You are either a minor or do not have a passport.")


aa = [1,2,3]
bb = aa
cc = [1,2,3]
print(aa is bb)  # True, same object
print (aa is cc)  # False, different objects
print (aa is not cc)