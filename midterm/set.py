collaction = {"painapple", "banana", "orange", "mongo"}

collaction.add("apple")
print("After add:", collaction)

# The remove() method (the item to be removed must exist)
collaction.remove("banana")
print("After remove:", collaction)

# The discard() method (does not raise an error if the item does not exist)
collaction.discard("nonexistent_item")
print("After discard:", collaction)

# The pop() method (removes and returns an arbitrary item)
removed_item = collaction.pop()
print("After pop:", collaction, "| Removed item:", removed_item)

# The clear() method (removes all items from the set)
collaction.clear()
print("After clear:", collaction)

# The del keyword (deletes the set entirely)
# del collaction
# print(collaction)  # This will raise an error as collaction no longer exists