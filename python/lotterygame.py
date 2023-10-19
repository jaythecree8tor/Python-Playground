import random
import time

# Function to generate random winning numbers
def generate_winning_numbers():
    return random.sample(range(1, 51), 5)  # Assuming you have 50 possible numbers

# Function to get the user's selected numbers
def get_user_numbers():
    user_numbers = []
    print("Welcome to the Football Lottery System!")
    print("Try your luck by selecting 5 numbers between 1 and 50.")
    while len(user_numbers) < 5:
        try:
            number = int(input(f"Enter your {len(user_numbers) + 1}st number (1-50): "))
            if 1 <= number <= 50 and number not in user_numbers:
                user_numbers.append(number)
                print(f"Number {number} added to your list!")
            elif number in user_numbers:
                print("You've already chosen that number. Please select a different one.")
            else:
                print("Invalid input. Please enter a unique number between 1 and 50.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return user_numbers

# Function to check if the user has won
def check_winning(user_numbers, winning_numbers):
    matched_numbers = set(user_numbers) & set(winning_numbers)
    return matched_numbers

# Function to display lottery results
def display_results(user_numbers, winning_numbers):
    print("\nWinning Numbers are being drawn...")
    time.sleep(2)
    print(f"Winning Numbers: {winning_numbers}\n")
    matched_numbers = check_winning(user_numbers, winning_numbers)
    
    if len(matched_numbers) == 5:
        print("Congratulations! You've won the jackpot!")
    elif len(matched_numbers) > 0:
        print(f"You matched {len(matched_numbers)} number(s): {matched_numbers}")
    else:
        print("Sorry, no matched numbers. Better luck next time!")

# Main game loop
def football_lottery_game():
    winning_numbers = generate_winning_numbers()
    user_numbers = get_user_numbers()
    display_results(user_numbers, winning_numbers)

if __name__ == "__main__":
    football_lottery_game()
