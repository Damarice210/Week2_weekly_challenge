# Initialize an empty list to store the integers
numbers = []

# Ask the user how many numbers they want to enter
num_count = int(input("How many numbers would you like to add to the list? "))

# Get each integer from the user and add it to the list
for i in range(num_count):
    number = int(input(f"Enter number {i + 1}: "))
    numbers.append(number)

# Calculate the sum of all integers in the list
total_sum = sum(numbers)

# Display the list and the sum
print("\nYour list of numbers:", numbers)
print("The sum of all the numbers is:", total_sum)
