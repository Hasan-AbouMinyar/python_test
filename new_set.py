collaction = {"painapple", "banana", "orange", "mongo"}

# The for loop to loop through the set items
print("Looping through the set:")
for item in collaction:
    print(item)

# To join two or more sets in Python:
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "kiwi", "grape"}

# The union() method or | operator joins all items from two sets or more.
union_set = set1.union(set2)
union_set_operator = set1 | set2  # Define union_set_operator here
print("Union using union():", union_set)
print("-" * 20)
print("Union using | operator:", union_set_operator)
print("-" * 20)

# The update() method joins all items from both sets.
set1.update(set2)
print("After update():", set1)
print("-" * 20)

# The intersection() method or & operator keeps ONLY the duplicates.
intersection_set = set1.intersection(set2)
intersection_set_operator = set1 & set2  # Define intersection_set_operator here
print("Intersection using intersection():", intersection_set)
print("-" * 20)
print("Intersection using & operator:", intersection_set_operator)
print("-" * 20)

# The difference() method or - operator keeps the items from the first set
# that are not in the other set(s).
difference_set = set1.difference(set2)
difference_set_operator = set1 - set2  # Define difference_set_operator here
print("Difference using difference():", difference_set)
print("-" * 20)
print("Difference using - operator:", difference_set_operator)
print("-" * 20)

# The symmetric_difference() method or ^ operator keeps all items
# EXCEPT the duplicates.
symmetric_difference_set = set1.symmetric_difference(set2)
symmetric_difference_set_operator = set1 ^ set2  # Define symmetric_difference_set_operator here
print("Symmetric difference using symmetric_difference():", symmetric_difference_set)
print("-" * 20)
print("Symmetric difference using ^ operator:", symmetric_difference_set_operator)
print("-" * 20)

# Note:
# All operators only allow joining sets with sets, and not with other data types.
# The update() changes the original set, and does not return a new set.
# Both union() and update() will exclude any duplicate items.
