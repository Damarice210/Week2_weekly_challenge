# Function to get a set of integers from the user
def get_integer_set(prompt):
    user_input = input(prompt)
    # Convert the input string to a set of integers
    integer_set = set(map(int, user_input.split()))
    return integer_set

# Get two sets of integers from the user
set1 = get_integer_set("Enter integers for the first set, separated by spaces: ")
set2 = get_integer_set("Enter integers for the second set, separated by spaces: ")

# Find the common elements (intersection) between the two sets
common_elements = set1.intersection(set2)

# Display the results
print("\nFirst set:", set1)
print("Second set:", set2)
print("Common elements:", common_elements)
# Function to get a set of integers from the user
def get_integer_set(prompt):
    user_input = input(prompt)
    # Convert the input string to a set of integers
    integer_set = set(map(int, user_input.split()))
    return integer_set

# Get two sets of integers from the user
set1 = get_integer_set("Enter integers for the first set, separated by spaces: ")
set2 = get_integer_set("Enter integers for the second set, separated by spaces: ")

# Find the common elements (intersection) between the two sets
common_elements = set1.intersection(set2)

# Display the results
print("\nFirst set:", set1)
print("Second set:", set2)
print("Common elements:", common_elements)
