# Problem 22: Flatten a nested list
# Find and fix the error

nested_list = [[1, 2], [3, 4], [5, 6]]
flat_list = []

for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)
print(f"Flattened list: {flat_list}")
