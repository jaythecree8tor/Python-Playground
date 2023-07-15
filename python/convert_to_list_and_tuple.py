# Prompt the user to enter a list of numbers separated by commas
values = input("Enter some numbers separated by commas: ")

# Split the input string into a list of numbers
number_list = values.split(",")

# Convert the list into a tuple
number_tuple = tuple(number_list)

# Print the list and tuple
print('List:', number_list)    # Print the list
print('Tuple:', number_tuple)  # Print the tuple
