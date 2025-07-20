# استيراد الوحدات اللازمة
from datetime import date
from typing import List

# تعريف فئة لتنظيم بيانات ووظائف الشخص
class Person:
    """
    فئة تمثل شخصًا، مع خصائص للاسم والعمر والوظائف المرتبطة بهما.
    """
    def __init__(self, name: str, birth_year: int):
        """
        المنشئ لإنشاء كائن شخص جديد.
        - name: اسم الشخص
        - birth_year: سنة ميلاد الشخص
        """
        if not name or not isinstance(name, str):
            raise ValueError("يجب أن يكون الاسم سلسلة نصية غير فارغة.")
        if not isinstance(birth_year, int) or birth_year > date.today().year:
            raise ValueError("سنة الميلاد يجب أن تكون رقمًا صحيحًا صالحًا.")
            
        self.name = name
        self.birth_year = birth_year
        self.age = self.calculate_age()

    def calculate_age(self) -> int:
        """يحسب العمر الحالي بناءً على سنة الميلاد."""
        current_year = date.today().year
        return current_year - self.birth_year

    @property
    def age_category(self) -> str:
        """يحدد الفئة العمرية للشخص بناءً على عمره."""
        if self.age >= 65:
            return "مواطن متقاعد"
        elif self.age >= 18:
            return "بالغ"
        elif self.age >= 13:
            return "مراهق"
        elif self.age >= 3:
            return "طفل"
        else:
            return "رضيع"

    def years_until_100(self) -> int:
        """يحسب عدد السنوات المتبقية حتى يبلغ الشخص 100 عام."""
        return 100 - self.age

    def display_info(self):
        """يعرض جميع معلومات الشخص بطريقة منسقة."""
        print("-" * 35)
        print(f"👤 الاسم: {self.name}")
        print(f"📅 العمر: {self.age} عامًا (مواليد {self.birth_year})")
        print(f"📊 الفئة العمرية: {self.age_category}")
        
        years_to_100 = self.years_until_100()
        if years_to_100 > 0:
            print(f"⏳ سيبلغ {self.name} 100 عام بعد {years_to_100} سنة.")
        else:
            print(f"🎉 {self.name} قد بلغ بالفعل 100 عام أو أكثر!")

# --- التنفيذ الرئيسي للبرنامج ---
def main():
    """
    الوظيفة الرئيسية لتشغيل البرنامج.
    """
    # قائمة الأشخاص (اسم + سنة ميلاد)
    people_data = {
        "حسن": 2003,      # 22 years old in 2025
        "سارة": 2010,     # 15 years old in 2025
        "علي": 1960,       # 65 years old in 2025
        "منى": 2023,       # 2 years old in 2025
        "خالد": 1988      # 37 years old in 2025
    }

    # إنشاء قائمة من كائنات الأشخاص
    try:
        people_objects: List[Person] = [Person(name, year) for name, year in people_data.items()]
    except ValueError as e:
        print(f"خطأ في البيانات: {e}")
        return

    # معالجة وعرض معلومات كل شخص
    print("🚀 بدء معالجة بيانات الأشخاص...\n")
    for person in people_objects:
        person.display_info()
    
    print("-" * 35)
    print("\n✅ تم الانتهاء من معالجة جميع الأشخاص بنجاح!")

# التأكد من تشغيل الكود فقط عند استدعاء الملف مباشرة
if __name__ == "__main__":
    main()
