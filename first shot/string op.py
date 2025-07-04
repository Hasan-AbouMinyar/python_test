m = "  Python is Awesome!  "
print(f"Original string: '{m}'")

# دوال النصوص المدمجة
print(f" {m.upper()}")
print(f"{m.lower()}")
print(f" '{m.strip()}'")
print(f" {m.replace('Awesome', 'Fun')}")
# دالة split تقسم النص إلى قائمة.
print(f" {m.split(' ')}")
# ملاحظة: دوال النصوص لا تغير النص الأصلي، بل تعيد قيمة جديدة.
print(f"{m}'")

# طول النص وفهرسته
print(f"{len(m)}")
print(f" {m.strip()[0]}")

# F-Strings لدمج المتغيرات مع النصوص.
a = "ITSE305"
print(f"I am studying the course {a} at the Faculty of IT.")

# محارف الهروب (Escape Characters)
print("This is the first line.\nAnd this is a new line.") # \n لسطر جديد
print("Column 1\tColumn 2") # \t لعمل مسافة جدولة\\


s = "    Hasan Ahmed Abouminyar.     "

print (f"this is a {s.split()}")
print (f"the is a {s.strip()}")

c = s.replace("Hasan", "Hasona")
print(f"the is a {c}")