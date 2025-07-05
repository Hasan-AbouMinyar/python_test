List = ["hasan","ahmed" ,"Abouminyar","Ali","Mohamed"]
num = [1,2,3,4,5]
bool = [True,False,True,False,True]
print (List)

print (List[2])

print (len(List))

print(List)
print (num)
print (bool)

difval = [1,"ahmed",True,3.14]
print (difval)

print(type(List))

fs = list(("hasan","ahmed" ,"Abouminyar","Ali","Mohamed"))
print(fs)


print (List[1:3])

if "hasan" in List:
    print("true")
else: 
    print ("false")

fs[3]= "AbouAqasim"

print(fs)

fs.insert(1,"The king")
print(fs)
q= ["orange","banana","apple"]

print(q)

for i in q:
    print(i)

for i in range(len(q)):
    print(q[i])

hlist = ["one Hasan","two Hasan","three Hasan","one Abouminyar","two Abouminyar","three Abouminyar","for Hasan","for Abouminyar"]

hasan = []
abouminyar = []

for i in hlist:
    if "Hasan" in i:
        hasan.append(i)
    else:
        abouminyar.append(i)

print (hasan)
print (abouminyar)

cars = ["BMW","Mercedes","Toyota","Honda","Ford","Chevrolet","Nissan","Volkswagen","Hyundai","Kia"  ]
cars.sort()

print(cars)
for i in cars:
    print(i)

cars.sort(reverse=True)
print(cars)
print(count(cars)))
print(cars.index("Toyota"))
print(cars)