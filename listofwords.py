# List of words
words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]

# Using list comprehension to create a new list with words having an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Display the results
print("Original list of words:", words)
print("Words with an odd number of characters:", odd_length_words)
