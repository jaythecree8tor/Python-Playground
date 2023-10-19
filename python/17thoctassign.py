def find_maximum(*args):
    max_num = args[0]
    for x in args[0:]:
        if x > max_num:
            max_num = x
    return max_num
print(find_maximum(100, 30, 40, 10))


def find_minimum(*args):
    min_num = args[0]
    for x in args[0:]:
        if x < min_num:
            min_num = x
    return min_num
print(find_minimum(100, 30, 40, 10))


def find_average(*args):
    if not args:
        return None
    sum_of_numbers = sum(args)
    average = sum_of_numbers / len(args)
    return average
print(find_average(100, 30, 40, 10))