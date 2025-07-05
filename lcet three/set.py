

m = {"apple", "banana", "cherry","cherry"}
print(m)
m.add("orange")
print(m)
m.update(["kiwi", "melon", "mango"])
print(m)  # 🖨️ {'kiwi', 'banana', 'cherry

s = {True, 1, 2}
print(s)  # 🖨️ {True, 2} ✅


for i in m: 
    print(i)

set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)
print(set1)  # 🖨️ {1, 2, 3,