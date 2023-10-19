def find_numbers():
    numbers = []
    for num in range(1500, 2701):
        if num % 7 == 0 and num % 5 == 0:
            numbers.append(num)
    return numbers

divisible_by_7_and_5 = find_numbers()
print("Numbers divisible by 7 and multiples of 5 between 1500 and 2700:")
print(divisible_by_7_and_5)
