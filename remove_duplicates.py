def find_duplicates(lst):
    duplicates = []
    for i in lst:
        if lst.count(i) > 1 and i not in duplicates:
            duplicates.append(i)
    return duplicates

# Example
my_list = [1, 2, 3, 2, 4, 5, 1, 6, 4]
duplicate_values = find_duplicates(my_list)
print(f"Duplicate values are: {duplicate_values}")
