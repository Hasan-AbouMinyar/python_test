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

# قائمة الأشخاص (اسم + عمر)
people = {
    "Hasan": 22,
    "Sarah": 15,
    "Ali": 65,
    "Mona": 2,
    "Khalid": 37
}

# معالجة كل شخص في القائمة
for name, age in people.items():
    print("-" * 30)
    print(f"{name} is {age} years old.")

    # تحديد الفئة العمرية
    category = classify_age(age)
    print(f"{name} is {category}.")

    # حساب السنوات المتبقية ليبلغ 100 سنة
    years_to_100 = 100 - age
    if years_to_100 > 0:
        print(f"{name} will turn 100 years old in {years_to_100} years.")
    else:
        print(f"{name} is already 100 years old or older!")

print("-" * 30)
print("Finished processing all people!")
