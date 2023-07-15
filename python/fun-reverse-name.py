# Prompt the user to enter their first name and last name
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Print the reversed values (::-1 iterates through the string in reverse order)
print("Reversed values:")
print(first_name[::-1])  # Reverse the first name using slicing [::-1] and print
print(last_name[::-1])   # Reverse the last name using slicing [::-1] and print
