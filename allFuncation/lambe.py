names = ["Alice", "Bob", "Charlie",
          "David", "Eve", "Frank", 
          "Grace", "Heidi", "Ivan",
            "Judy"]
ages = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]

# استخدم map مع lambda لإنتاج tuples (name, age)
results = map(lambda name, age: (name, age), names, ages)

# حول النتائج إلى dict
result_dict = dict(results)
print(result_dict)
