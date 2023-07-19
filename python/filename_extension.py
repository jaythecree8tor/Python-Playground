# Get the filename from the user
filename = input("Enter a filename: ")

# Split the filename into its name and extension
extension = filename.split(".")

# Print the file extension
print("File extension:", extension[-1])


# OR


# Get the filename from the user
filename = input("Enter a filename: ")

# Split the filename into its name and extension
name, extension = filename.split(".")

# Print the file extension
print("File extension:", extension)

#OR

Extensive_Name = input("Enter Your File Name: ")
dot_index = Extensive_Name.find(".")
if dot_index != -1:
    print("You've Inputted  a ."+Extensive_Name[dot_index + 1:] + " File")
else:
    print("No dot (.) found in the file name.")

#Third Method
def print_value_after_dot(string):
  """Prints any value after the "." sign.

  Args:
    string: The string to print the value from.
  """

  index = string.find(".")
  if index == -1:
    print("The string does not contain a '.'")
  else:
    print(string[index + 1:])


if __name__ == "__main__":
  string = input("Enter Your File Name: ")
  print_value_after_dot(string)
