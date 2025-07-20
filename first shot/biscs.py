# دالة لتحديد الفئة العمرية
def classify_age(age):
    if age >= 60:
        return "a senior citizen"
    elif age >= 18:
        return "an adult"
    elif age >= 13:
        return "a teenager"
    elif age >= 3:
        return "a child"
    else:
        return "a baby"

# أخذ الاسم والعمر من المستخدم
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# طباعة معلومات الشخص
print(f"{name} is {age} years old.")

# طباعة الفئة العمرية
category = classify_age(age)
print(f"{name} is {category}.")
