array = ["Hasan", "Ahmed", "Abouminyar"]

print(list(enumerate(array)))

print("  ")


for index , value in enumerate(array, start = 1):
    print(f"FR{index}  {value}")


pro = ["Python", "Java", "C++", "JavaScript"]

for num , sum in enumerate(pro, start = -4):
    print (f"{num} {sum}")



