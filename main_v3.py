import tkinter as tk
import random

# --- Constants ---
ROWS = 7
COLS = 6
SYMBOLS = ['R', 'G', 'B', 'Y', 'X', 'T', 'P']  # Gem colors and special symbols
WEIGHTS = [20, 20, 20, 20, 5, 10, 5]
SYMBOL_COLORS = {
    'R': 'red',
    'G': 'green',
    'B': 'blue',
    'Y': 'yellow',
    'X': 'black',   # Bomb
    'T': 'orange',  # Transform
    'P': 'brown'    # Peanut
}
PARROT_MARKERS = {
    'R': 'PR',
    'G': 'PG',
    'B': 'PB',
    'Y': 'PY'
}

# --- Grid Logic ---
def generate_grid():
    return [[random.choices(SYMBOLS, weights=WEIGHTS)[0] for _ in range(COLS)] for _ in range(ROWS)]

def get_adjacent_positions(r, c):
    positions = []
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS:
            positions.append((nr, nc))
    return positions

# --- GUI Setup ---
class SlotGridApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Pirots3-style Grid with Parrot Movement")

        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack(pady=20)

        self.grid = generate_grid()
        self.labels = []

        # Place one parrot for each color in starting corners
        self.parrots = {
            'R': (ROWS - 1, 0),
            'G': (ROWS - 1, COLS - 1),
            'B': (0, 0),
            'Y': (0, COLS - 1)
        }

        for r in range(ROWS):
            row_labels = []
            for c in range(COLS):
                lbl = tk.Label(self.grid_frame, text='', font=('Helvetica', 16), width=4, height=2, relief='ridge', borderwidth=2)
                lbl.grid(row=r, column=c, padx=2, pady=2)
                row_labels.append(lbl)
            self.labels.append(row_labels)

        self.update_display()

        self.regenerate_button = tk.Button(root, text="Spin / Regenerate Grid", command=self.refresh_grid)
        self.regenerate_button.pack(pady=5)

        self.move_button = tk.Button(root, text="Move Parrots", command=self.move_parrots)
        self.move_button.pack(pady=5)

    def update_display(self):
        for r in range(ROWS):
            for c in range(COLS):
                symbol = self.grid[r][c]
                label = self.labels[r][c]
                label.config(text=symbol, bg=SYMBOL_COLORS[symbol], fg='white' if symbol in ['X', 'T', 'P'] else 'black')

        for color, (pr, pc) in self.parrots.items():
            self.labels[pr][pc].config(text=PARROT_MARKERS[color], bg='white', fg='black')

    def refresh_grid(self):
        self.grid = generate_grid()
        self.parrots = {
            'R': (ROWS - 1, 0),
            'G': (ROWS - 1, COLS - 1),
            'B': (0, 0),
            'Y': (0, COLS - 1)
        }
        self.update_display()

    def move_parrots(self):
        for color, (pr, pc) in self.parrots.items():
            target_color = color  # Gem color the parrot collects
            adjacent = get_adjacent_positions(pr, pc)
            for nr, nc in adjacent:
                if self.grid[nr][nc] == target_color:
                    self.grid[nr][nc] = 'T'  # Collected, mark as transform for now
                    self.parrots[color] = (nr, nc)  # Move parrot
                    break
        self.update_display()


if __name__ == "__main__":
    root = tk.Tk()
    app = SlotGridApp(root)
    root.mainloop()