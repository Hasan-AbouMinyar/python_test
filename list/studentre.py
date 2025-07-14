students = ["Alice", "Bob", "Charlie", "David"]
for student in students:
    print(student)

new_students = ["Eva", "Frank", "Grace"]

for student in new_students:
    print(student)

students.extend(new_students)

print("Updated Student List:")
for student in students:
    print(student)

students.sort(reverse=True)

print("Sorted Student List (Descending):")
for student in students:
    print(student)

students.remove("Charlie")
print("Student List after removing 'Charlie':")
for student in students:
    print(student)
