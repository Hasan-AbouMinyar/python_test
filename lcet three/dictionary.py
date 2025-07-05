dk = {
    'name': 'hasan',
    'age': 25,
    'city': 'Tripoli',
    'is_engineer': True,
}

print(dk)  
# 🖨️ {'name': 'hasan', 'age': 25, 'city': 'Tripoli', 'is_engineer': True}
for key in dk:
    print( dk[key])

me = dict(name = "Abouminyar", age = 30, city = "Tripoli", is_engineer = False)
print(me)

print (me['name'])  # 🖨️ Abouminyar


my_dict = {
    "name": "Hasan",
    "age": 22,
    "city": "Tripoli"
}
print(my_dict)
print(my_dict.get("name",'nothere'))  # 🖨️ Hasan
print(my_dict.get("country", "غير موجود"))  # 🖨️ غير موجود
print(my_dict.keys())  # dict_keys(['name', 'age', 'city'])
print(my_dict.keys())  # dict_keys(['name', 'age', 'city'])
print(my_dict.items())
# dict_items([('name', 'Hasan'), ('age', 22), ('city', 'Tripoli')])
my_dict = {"name": "Hasan", "age": 22, "city": "Tripoli"}

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)
