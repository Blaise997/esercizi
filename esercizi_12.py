def first_and_last(input_list):
    # Check if the input list is not empty
    if input_list:
        return [input_list[0], input_list[-1]]  # Return a new list containing the first and last elements
    else:
        return "Input list is empty"

# Example usage
a = [5, 10, 15, 20, 25]
result = first_and_last(a)
print("New list:", result)


