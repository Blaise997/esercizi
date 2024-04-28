def reverse_words_order(sentence):
    words = sentence.split()  # Split the sentence into words
    reversed_sentence = ' '.join(reversed(words))  # Join the words in reversed order
    return reversed_sentence

# Ask the user for input
user_input = input("Enter a long string containing multiple words: ")

# Call the function and print the result
reversed_string = reverse_words_order(user_input)
print("Reversed string with words in backwards order:", reversed_string)
