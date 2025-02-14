import random
import tkinter as tk
from tkinter import messagebox

class Game:
    def __init__(self):
        self.code = self.gen_code()

    def gen_code(self):
        return ''.join(random.sample('0123456789', 4))

    def eval_guess(self, guess):
        bulls, cows = 0, 0
        for i in range(4):
            if guess[i] == self.code[i]:
                bulls += 1
            elif guess[i] in self.code:
                cows += 1
        return bulls, cows

    def reset(self):
        self.code = self.gen_code()

class App:
    def __init__(self, root):
        self.game = Game()
        self.root = root
        self.root.title("Bulls and Cows")

        self.frame = tk.Frame(root, padx=20, pady=20)
        self.frame.pack()

        self.label = tk.Label(self.frame, text="Guess the number:", font=("Arial", 14))
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.entry = tk.Entry(self.frame, font=("Arial", 14))
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        self.button = tk.Button(self.frame, text="Submit", font=("Arial", 14), command=self.check_guess)
        self.button.grid(row=1, columnspan=2, pady=10)

        self.result = tk.Label(self.frame, text="", font=("Arial", 14))
        self.result.grid(row=2, columnspan=2, pady=10)

    def check_guess(self):
        guess = self.entry.get()
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) != 4:
            messagebox.showerror("Invalid input", "Enter a 4-digit number with unique digits.")
            return

        bulls, cows = self.game.eval_guess(guess)
        self.result.config(text=f"Bulls: {bulls}, Cows: {cows}")

        if bulls == 4:
            messagebox.showinfo("Congrats","You got it")
            self.game.reset()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()