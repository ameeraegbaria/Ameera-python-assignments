
import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")
        
        self.secret_number = random.randint(1, 20)
        self.guesses = 0

        # Create widgets
        self.label = tk.Label(root, text="I have thought of a number between 1 and 20. Try to guess it!", wraplength=300)
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(root, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.new_game_button = tk.Button(root, text="New Game", command=self.start_new_game)
        self.new_game_button.pack(pady=5)

        self.show_button = tk.Button(root, text="Show Secret Number", command=self.show_secret_number)
        self.show_button.pack(pady=5)

        self.exit_button = tk.Button(root, text="Exit", command=self.root.quit)
        self.exit_button.pack(pady=5)

    def check_guess(self):
        user_input = self.entry.get().strip()

        try:
            guess = int(user_input)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid whole number.")
            return

        self.guesses += 1

        if guess < self.secret_number:
            messagebox.showinfo("Hint", "Too small!")
        elif guess > self.secret_number:
            messagebox.showinfo("Hint", "Too big!")
        else:
            messagebox.showinfo("Correct!", f"Correct! You guessed the number in {self.guesses} tries.")
            self.start_new_game()

    def start_new_game(self):
        self.secret_number = random.randint(1, 20)
        self.guesses = 0
        self.entry.delete(0, tk.END)
        messagebox.showinfo("New Game", "A new game has started! Guess the new number.")

    def show_secret_number(self):
        messagebox.showinfo("Secret Number", f"The secret number is: {self.secret_number}")

if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
