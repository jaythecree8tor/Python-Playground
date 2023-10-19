# import random
# import os

# def main():
#     randomnumber = str(random.randrange(0,9999)).zfill(4)
    
#     user_guessed_number = input("Please input any 4-digit number: ")
    
#     if user_guessed_number == randomnumber:
#         print("You have guessed right:", randomnumber)
#     elif len(user_guessed_number) != 4:
#         print("Please input a 4-digit number.")
#         os.system("cls")
#         main()
#     else:
#         print("Not guessed correctly, the correct guess is:", randomnumber)

# if __name__ == "__main__":
#     main()


import random
import os

def main():
    randomnumber = str(random.randrange(0, 9999)).zfill(4)
    print("Generated 4-digit number:", randomnumber)

    user_guessed_number = input("Please input any 4-digit number: ")

    if len(user_guessed_number) != 4:
        print("Please input a 4-digit number.")
        os.system("cls")
        main()
    else:
        masked_guess = ''
        for i in range(4):
            if user_guessed_number[i] == randomnumber[i]:
                masked_guess += user_guessed_number[i]
            else:
                masked_guess += '*'

        if masked_guess == randomnumber:
            print("You have guessed right:", randomnumber)
        else:
            print("Not guessed correctly", masked_guess)

if __name__ == "__main__":
    main()
