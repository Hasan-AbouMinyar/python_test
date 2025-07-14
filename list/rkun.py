inventory = ["shoes", "shirts", "pants", "hats"]
for item in inventory:
    print(item)

new_items = ["jackets", "belts", "gloves"]

for item in new_items:
    print(item)


inventory.extend(new_items)

print("Updated Inventory:")
for item in inventory:
    print(item)

inventory.sort(reverse=True)

print("Sorted Inventory (Descending):")
for item in inventory:
    print(item)

inventory.remove("pants")
print("Inventory after removing 'pants':")
for item in inventory:
    print(item)
