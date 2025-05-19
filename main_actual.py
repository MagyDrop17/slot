import tkinter as tk
import random

# --- Constants ---
ROWS = 7
COLS = 6
SYMBOLS = ['R', 'G', 'B', 'Y', 'X', 'T', 'P']
WEIGHTS = [20, 20, 20, 20, 5, 10, 5]  # Normal gems, dynamite, transform, peanut
SYMBOL_COLORS = {
    'R': 'red',
    'G': 'green',
    'B': 'blue',
    'Y': 'yellow',
    'X': 'black',   # Bomb
    'T': 'orange',  # Transform
    'P': 'brown'    # Peanut
}

# --- Grid Logic ---
def generate_grid():
    return [[random.choices(SYMBOLS, weights=WEIGHTS)[0] for _ in range(COLS)] for _ in range(ROWS)]

# --- GUI Setup ---
class SlotGridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pirots3-style Grid")

        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack(pady=20)

        self.grid = generate_grid()
        self.labels = []

        for r in range(ROWS):
            row_labels = []
            for c in range(COLS):
                lbl = tk.Label(
                    self.grid_frame,
                    text=self.grid[r][c],
                    font=('Helvetica', 20),
                    width=4,
                    height=2,
                    bg=SYMBOL_COLORS[self.grid[r][c]],
                    fg='white' if self.grid[r][c] in ['X', 'T', 'P'] else 'black',
                    relief='ridge',
                    borderwidth=2
                )
                lbl.grid(row=r, column=c, padx=3, pady=3)
                row_labels.append(lbl)
            self.labels.append(row_labels)

        self.regenerate_button = tk.Button(root, text="Spin / Regenerate Grid", command=self.refresh_grid)
        self.regenerate_button.pack(pady=10)

    def refresh_grid(self):
        self.grid = generate_grid()
        for r in range(ROWS):
            for c in range(COLS):
                symbol = self.grid[r][c]
                self.labels[r][c].config(
                    text=symbol,
                    bg=SYMBOL_COLORS[symbol],
                    fg='white' if symbol in ['X', 'T', 'P'] else 'black'
                )

if __name__ == "__main__":
    root = tk.Tk()
    app = SlotGridApp(root)
    root.mainloop()