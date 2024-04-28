def remove_duplicates_loop(input_list):
    unique_elements = []
    for element in input_list:
        if element not in unique_elements:
            unique_elements.append(element)
    return unique_elements

# Example usage:
original_list = [1, 2, 3, 3, 4, 5, 6, 6, 7]
result_loop = remove_duplicates_loop(original_list)
print("List after removing duplicates (using loop):", result_loop)

def remove_duplicates_set(input_list):
    return list(set(input_list))

# Example usage:
original_list = [1, 2, 3, 3, 4, 5, 6, 6, 7]
result_set = remove_duplicates_set(original_list)
print("List after removing duplicates (using sets):", result_set)

