import time
from termcolor import colored

i = 1

up = True

while i > 0:
    # print the number of stars equal to i, followed by a space and thank you in red
    print(colored("*", "green") * i + " " + colored("Thank You", "red"))
    time.sleep(1)
    if up and i == 6:
        up = False
    # if the counter is increasing, increment i by 1
    if up:
        i += 1
    # if the counter is decreasing, decrement i by 1
    else:
        i -= 1
