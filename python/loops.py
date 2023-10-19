# x = 10

# while x >= 0:
#     print(x)
#     x -= 1

# x = 0

# while x <= 10:
#     if x % 2 == 0:
#       print(x)
#     x += 1

# x = 1

# while x <= 10:
#     print(x)
#     x += 2

# def time_table_with_while_loop():

#     default_number = 0

#     print("Time Table with While Loop:")
#     users_number = int(input("Enter the Number of Times you want the table generated: "))
#     const_users_number = users_number

#     while default_number < 12:  # Adjust the condition to generate up to 12 times (0 to 12)
#         default_number += 1
#         if default_number == 1:
#             print(f"{const_users_number} X {default_number} = {const_users_number * default_number}")
#         else:
#             print(f"{const_users_number} X {default_number} = {const_users_number * default_number}")


# time_table_with_while_loop()

num = int(input("Enter number: "))

if num < 0:
    print("enter a positive number: ")
elif num == 0 or num == 1:
    print("factorial of", num ,"is ")
else:
    result = 1
    while num > 1:
        result *= num
        num -= 1
    print("The factorial of", num, "is", result)