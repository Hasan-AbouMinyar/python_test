x = 10
y = 5
if x > y:
    # هذا السطر يقع داخل كتلة if بسبب المسافة البادئة.
    print(f"{x} is greater than {y} (This is an example of correct indentation)")
    print (x,"is greater than",y, "(This is another example of correct indentation)")


x = 10
y = 5

print(x, "is greater than", y)                  # أبسط
print(f"{x} is greater than {y}")                # أنظف وقابل للتنسيق
print(f"{x} is greater than {y} (checked)")     # مثال مع نص إضافي داخل السلسلة

print ( f"fucking {x} is the greater than {y} (checked)")