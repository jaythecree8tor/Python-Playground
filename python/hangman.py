import random

# List of words for the game
words = ["python", "hangman", "programming", "openai", "machine", "learning"]

# Function to choose a random word from the list
def choose_word():
    return random.choice(words)

# Function to display the current state of the word (with underscores for missing letters)
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

# Function to play Hangman
def play_hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 6  # Number of incorrect attempts allowed

    print("Welcome to Hangman!")
    print("You have 6 attempts to guess the word correctly.")

    while attempts > 0:
        print("\nWord:", display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("Good guess!")
            if word_to_guess == display_word(word_to_guess, guessed_letters):
                print("Congratulations! You've guessed the word:", word_to_guess)
                break
        else:
            attempts -= 1
            print("Incorrect guess. You have", attempts, "attempts left.")

    if attempts == 0:
        print("Game over! The word was:", word_to_guess)

# Main function
if __name__ == "__main__":
    play_hangman()
