def remove_duplicates_with_loop(lst):
    result = []
    for item in lst:
        if item not in result:
            result.append(item)
    return result


def remove_duplicates_with_set(lst):
    return list(set(lst))

my_list = [1, 2, 2, 3, 4, 1, 5]

print(remove_duplicates_with_loop(my_list))  # [1, 2, 3, 4, 5]
print(remove_duplicates_with_set(my_list))   # ممكن تطلع: [1, 2, 3, 4, 5] أو [5, 1, 2, 3, 4] حسب ترتيب الـ set

def find_maximum(num1, num2, num3):
    """Finds the maximum of three numbers without using the max() function."""
    maximum = num1
    if num2 > maximum:
        maximum = num2
    if num3 > maximum:
        maximum = num3
    return maximum

# Example usage:
num1 = 10
num2 = 25
num3 = 15
result = find_maximum(num1, num2, num3)

# Using f-string to print the result
print(f"The largest number between {num1}, {num2}, and {num3} is: {result}")
