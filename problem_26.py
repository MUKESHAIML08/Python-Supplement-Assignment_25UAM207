# Problem 26: Add item to a list
# Find and fix the error

def add_item(lst, item):
    lst = lst + [item]
    return lst

my_list = [1, 2, 3]
my_list = add_item(my_list, 4)
print(f"List after adding: {my_list}")
