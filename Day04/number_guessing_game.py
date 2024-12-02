import random

def main():
    print("Welcome to the Number Guessing Game!")
    while True:
        play_game()
        if not ask_to_play_again():
            print("Thanks for playing! Goodbye!")
            break

def play_game():
    secret_number = random.randint(1, 20)
    guesses = 0
    print("\nI have thought of a number between 1 and 20. Try to guess it!")

    while True:
        user_input = input("Enter your guess (or 'x' to exit, 'n' for a new game, 's' to show the number): ").strip().lower()

        if user_input == 'x':
            print("Exiting the program.")
            exit()
        elif user_input == 'n':
            print("Starting a new game.")
            return
        elif user_input == 's':
            print(f"The secret number is: {secret_number}")
            continue

        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number, 'x', 'n', or 's'.")
            continue

        guesses += 1
        if guess < secret_number:
            print("Too small!")
        elif guess > secret_number:
            print("Too big!")
        else:
            print(f"Correct! You guessed the number in {guesses} tries.")
            return

def ask_to_play_again():
    while True:
        user_input = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if user_input in ['yes', 'y']:
            return True
        elif user_input in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
