import tkinter as tk
import random

# --- Symbol setup ---
symbols = ['A', 'B', 'C', 'D', 'E']
weights = [40, 30, 20, 8, 2]
payouts = {
    'A': 5,
    'B': 12,
    'C': 25,
    'D': 200,
    'E': 2000
}

# --- Slot Machine Logic ---
def spin_reels():
    return [random.choices(symbols, weights=weights)[0] for _ in range(3)]

def evaluate_spin(reel):
    if reel[0] == reel[1] == reel[2]:
        return payouts[reel[0]]
    return 0

# --- GUI Setup ---
class SlotMachineApp:
    def __init__(self, root):
        self.root = root
        self.root.title("High Volatility Slot Machine")

        self.balance = 1000
        self.bet = 1

        self.reels = [tk.Label(root, text='-', font=('Helvetica', 48)) for _ in range(3)]
        for i, label in enumerate(self.reels):
            label.grid(row=0, column=i, padx=10)

        self.spin_button = tk.Button(root, text="Spin", command=self.spin, font=('Helvetica', 16))
        self.spin_button.grid(row=1, column=0, columnspan=3, pady=10)

        self.result_label = tk.Label(root, text="", font=('Helvetica', 16))
        self.result_label.grid(row=2, column=0, columnspan=3)

        self.balance_label = tk.Label(root, text=f"Balance: {self.balance}", font=('Helvetica', 14))
        self.balance_label.grid(row=3, column=0, columnspan=3)

    def spin(self):
        if self.balance < self.bet:
            self.result_label.config(text="Insufficient balance")
            return

        self.balance -= self.bet
        result = spin_reels()
        for i, symbol in enumerate(result):
            self.reels[i].config(text=symbol)

        win = evaluate_spin(result)
        self.balance += win
        
        if win > 0:
            self.result_label.config(text=f"You won {win}!")
        else:
            self.result_label.config(text="No win, try again.")

        self.balance_label.config(text=f"Balance: {self.balance}")


if __name__ == "__main__":
    root = tk.Tk()
    app = SlotMachineApp(root)
    root.mainloop()
