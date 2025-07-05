# الكلاس الأب (Parent class)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# الكلاس الابن (Child class) يرث من Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# استخدام الكلاسات:
a = Animal("Generic Animal")
print(a.speak())  # Generic Animal makes a sound.

d = Dog("Buddy")
print(d.speak())  # Buddy says Woof!
