import tkinter as tk
from tkinter import messagebox
import time
import copy

# ============================================================
# Sudoku Puzzle Dataset
# har difficulty level mein 4 puzzles hain
# 0 ka matlab hai ke cell empty hai
# ============================================================

PUZZLES = {
    "Easy": [
        # Easy Puzzle 1
        [
            [0,0,0,2,6,0,7,0,1],
            [6,8,0,0,7,0,0,9,0],
            [1,9,0,0,0,4,5,0,0],
            [8,2,0,1,0,0,0,4,0],
            [0,0,4,6,0,2,9,0,0],
            [0,5,0,0,0,3,0,2,8],
            [0,0,9,3,0,0,0,7,4],
            [0,4,0,0,5,0,0,3,6],
            [7,0,3,0,1,8,0,0,0],
        ],
        # Easy Puzzle 2
        [
            [0,2,0,6,0,8,0,0,0],
            [5,8,0,0,0,9,7,0,0],
            [0,0,0,0,4,0,0,0,0],
            [3,7,0,0,0,0,5,0,0],
            [6,0,0,0,0,0,0,0,4],
            [0,0,8,0,0,0,0,1,3],
            [0,0,0,0,2,0,0,0,0],
            [0,0,9,8,0,0,0,3,6],
            [0,0,0,3,0,6,0,9,0],
        ],
        # Easy Puzzle 3
        [
            [2,0,0,3,0,0,0,0,0],
            [8,0,4,0,6,2,0,0,3],
            [0,1,3,8,0,0,2,0,0],
            [0,0,0,0,2,0,3,9,0],
            [5,0,7,0,0,0,6,0,2],
            [0,3,2,0,0,6,0,0,0],
            [0,0,1,0,0,3,8,2,0],
            [9,0,0,2,8,0,1,0,4],
            [0,0,0,0,0,9,0,0,5],
        ],
        # Easy Puzzle 4
        [
            [5,3,0,0,7,0,0,0,0],
            [6,0,0,1,9,5,0,0,0],
            [0,9,8,0,0,0,0,6,0],
            [8,0,0,0,6,0,0,0,3],
            [4,0,0,8,0,3,0,0,1],
            [7,0,0,0,2,0,0,0,6],
            [0,6,0,0,0,0,2,8,0],
            [0,0,0,4,1,9,0,0,5],
            [0,0,0,0,8,0,0,7,9],
        ],
    ],
    "Medium": [
        # Medium Puzzle 1
        [
            [0,0,0,0,0,0,9,0,7],
            [0,0,0,4,2,0,1,8,0],
            [0,0,0,7,0,5,0,2,6],
            [1,0,0,9,0,4,0,0,0],
            [0,5,0,0,0,0,0,4,0],
            [0,0,0,5,0,7,0,0,9],
            [9,2,0,1,0,8,0,0,0],
            [0,3,4,0,5,9,0,0,0],
            [5,0,7,0,0,0,0,0,0],
        ],
        # Medium Puzzle 2
        [
            [1,0,0,0,0,7,0,9,0],
            [0,3,0,0,2,0,0,0,8],
            [0,0,9,6,0,0,5,0,0],
            [0,0,5,3,0,0,9,0,0],
            [0,1,0,0,8,0,0,0,2],
            [6,0,0,0,0,4,0,0,0],
            [3,0,0,0,0,0,0,1,0],
            [0,4,0,0,0,0,0,0,7],
            [0,0,7,0,0,0,3,0,0],
        ],
        # Medium Puzzle 3
        [
            [0,8,0,0,0,0,2,0,0],
            [0,0,0,0,8,4,0,9,0],
            [0,0,6,3,0,0,0,0,4],
            [0,9,0,0,0,0,0,0,0],
            [0,0,0,5,3,8,0,0,0],
            [0,0,0,0,0,0,0,4,0],
            [5,0,0,0,0,7,4,0,0],
            [0,1,0,6,4,0,0,0,0],
            [0,0,2,0,0,0,0,1,0],
        ],
        # Medium Puzzle 4
        [
            [9,0,6,0,7,0,4,0,3],
            [0,0,0,4,0,0,2,0,0],
            [0,7,0,0,2,3,0,1,0],
            [5,0,0,0,0,0,1,0,0],
            [0,4,0,2,0,8,0,6,0],
            [0,0,3,0,0,0,0,0,5],
            [0,3,0,7,0,0,0,5,0],
            [0,0,7,0,0,5,0,0,0],
            [4,0,5,0,1,0,7,0,8],
        ],
    ],
    "Hard": [
        # Hard Puzzle 1
        [
            [0,0,0,0,0,3,0,1,7],
            [0,1,5,0,0,9,0,0,8],
            [0,6,0,0,0,0,0,0,0],
            [1,0,0,0,0,7,0,0,0],
            [0,0,9,0,0,0,2,0,0],
            [0,0,0,5,0,0,0,0,4],
            [0,0,0,0,0,0,0,2,0],
            [5,0,0,6,0,0,3,4,0],
            [3,4,0,2,0,0,0,0,0],
        ],
        # Hard Puzzle 2
        [
            [2,0,0,0,8,0,3,0,0],
            [0,6,0,0,7,0,0,8,4],
            [0,3,0,5,0,0,2,0,9],
            [0,0,0,1,0,5,4,0,8],
            [0,0,0,0,0,0,0,0,0],
            [4,0,2,7,0,6,0,0,0],
            [3,0,1,0,0,7,0,4,0],
            [7,2,0,0,4,0,0,6,0],
            [0,0,4,0,1,0,0,0,3],
        ],
        # Hard Puzzle 3
        [
            [0,0,0,0,0,0,0,1,2],
            [0,0,0,0,3,5,0,0,0],
            [0,0,0,6,0,0,0,7,0],
            [7,0,0,0,0,0,3,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,3,0,0,0,0,0,6],
            [0,5,0,0,0,6,0,0,0],
            [0,0,0,8,4,0,0,0,0],
            [3,6,0,0,0,0,0,0,0],
        ],
        # Hard Puzzle 4
        [
            [0,2,0,0,0,0,0,0,0],
            [0,0,0,6,0,0,0,0,3],
            [0,7,4,0,8,0,0,0,0],
            [0,0,0,0,0,3,0,0,2],
            [0,8,0,0,4,0,0,1,0],
            [6,0,0,5,0,0,0,0,0],
            [0,0,0,0,1,0,7,8,0],
            [5,0,0,0,0,9,0,0,0],
            [0,0,0,0,0,0,0,4,0],
        ],
    ],
}


# ============================================================
# Helper functions - yeh basic cheezein hain jo baar baar use hongi
# ============================================================

def get_neighbors(row, col):
    """ek cell ke saare neighbors return karta hai (same row, col, ya 3x3 box)"""
    neighbors = set()

    # same row walay saare cells
    for c in range(9):
        if c != col:
            neighbors.add((row, c))

    # same column walay saare cells
    for r in range(9):
        if r != row:
            neighbors.add((r, col))

    # same 3x3 box walay cells nikalo
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if (r, c) != (row, col):
                neighbors.add((r, c))

    return neighbors


# sab cells ke neighbors pehle se calculate kar lo - taake baar baar na karna pare
NEIGHBORS = {}
for r in range(9):
    for c in range(9):
        NEIGHBORS[(r, c)] = get_neighbors(r, c)


def is_valid(board, row, col, num):
    """check karo ke kya num ko (row, col) pe rakh sakte hain ya nahi"""

    # pehle row check karo
    if num in board[row]:
        return False

    # phir column check karo
    for r in range(9):
        if board[r][col] == num:
            return False

    # ab 3x3 box check karo
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            if board[r][c] == num:
                return False

    return True


def find_empty(board):
    """pehli empty cell dhundo board mein - 0 matlab empty"""
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return (r, c)
    return None  # koi cell khali nahi - sab bhar gayi


# ============================================================
# Backtracking Algorithm
# basic idea: try karo, agar galat ho to wapas aao
# Russell & Norvig textbook se lia hai
# ============================================================

def solve_backtracking(board):
    """
    Backtracking se sudoku solve karo.
    Seedha board modify karta hai.
    True agar puzzle solve ho jaye, False agar na ho sake.
    """
    # sabse pehle koi empty cell dhundo
    empty = find_empty(board)

    if empty is None:
        # sab cells bhar gayi hain - puzzle solved!
        return True

    row, col = empty

    # 1 se 9 tak har number try karo
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # yeh number rakh do
            board[row][col] = num

            # recursively baqi board solve karo
            if solve_backtracking(board):
                return True

            # yeh number nahi chala to wapas 0 karo (BACKTRACK)
            board[row][col] = 0

    # koi number fit nahi hua - wapas jaana hoga
    return False


# ============================================================
# AC-3 Algorithm (Arc Consistency)
# yeh algorithm domains ko chhota karta hai
# constraints check karke impossible values hata deta hai
# ============================================================

def initialize_domains(board):
    """har cell ke liye possible values ka set banao"""
    domains = {}
    for r in range(9):
        for c in range(9):
            if board[r][c] != 0:
                # yeh cell pehle se filled hai - domain mein sirf ek value
                domains[(r, c)] = {board[r][c]}
            else:
                # khali cell - abhi to 1 se 9 sab possible hain
                domains[(r, c)] = set(range(1, 10))
    return domains


def revise(domains, xi, xj):
    """
    REVISE function - textbook se seedha uthaya hai
    xi ka domain check karo xj ke saath
    agar koi value xi mein hai jo xj se conflict karti hai to hata do
    """
    revised = False

    # xi ki har value check karo
    values_to_check = list(domains[xi])  # copy banao kyunke loop mein modify karenge
    for x in values_to_check:
        # dekhte hain kya xj mein koi aisi value y hai ke x != y
        # sudoku mein neighbors ki values different honi chahiye
        found_support = False
        for y in domains[xj]:
            if x != y:
                found_support = True
                break

        if not found_support:
            # koi supporting value nahi mili - yeh value hata do
            domains[xi].remove(x)
            revised = True

    return revised


def ac3(domains):
    """
    AC-3 algorithm - Arc Consistency check karta hai
    Russell & Norvig ki book se implement kiya hai
    Returns True agar sab consistent hai, False agar contradiction aa gayi
    """
    # pehle saare arcs ki queue banao
    queue = []
    for xi in domains:
        for xj in NEIGHBORS[xi]:
            queue.append((xi, xj))

    # jab tak queue khali nahi hoti, arcs process karo
    while queue:
        # queue se ek arc nikalo
        xi, xj = queue.pop(0)

        if revise(domains, xi, xj):
            # agar domain change hua hai
            if len(domains[xi]) == 0:
                # domain khali ho gaya - ab koi solution possible nahi
                return False

            # xi ke neighbors ko dubara check karna hoga
            for xk in NEIGHBORS[xi]:
                if xk != xj:
                    queue.append((xk, xi))

    return True


def solve_ac3(board):
    """
    AC-3 + Backtracking milake solve karo
    Pehle AC-3 se domains reduce karo
    phir agar zaroorat ho to backtracking use karo
    """
    # domains initialize karo
    domains = initialize_domains(board)

    # AC-3 chalao - domains reduce honge
    if not ac3(domains):
        return False

    # ab reduced domains ke saath backtracking karo
    return ac3_backtrack(board, domains)


def ac3_backtrack(board, domains):
    """AC-3 ke baad backtracking - reduced domains use karke"""

    # pehle un cells ko fill karo jinke domain mein sirf 1 value hai
    for r in range(9):
        for c in range(9):
            if len(domains[(r, c)]) == 1:
                board[r][c] = list(domains[(r, c)])[0]
            elif len(domains[(r, c)]) == 0:
                # domain khali hai - yeh raasta galat hai
                return False

    # MRV heuristic - sabse kam options wali empty cell dhundo
    min_domain_size = 10
    best_cell = None
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                size = len(domains[(r, c)])
                if size < min_domain_size:
                    min_domain_size = size
                    best_cell = (r, c)

    # agar koi empty cell nahi mili to puzzle solve ho chuka hai
    if best_cell is None:
        return True

    row, col = best_cell

    # is cell ki possible values try karo
    for num in list(domains[(row, col)]):
        if is_valid(board, row, col, num):
            # board ki purani state save karo - backtrack ke liye zaroori hai
            saved_board = copy.deepcopy(board)

            board[row][col] = num

            # domains ki copy banao aur update karo
            new_domains = copy.deepcopy(domains)
            new_domains[(row, col)] = {num}

            # AC-3 dubara chalao - naye constraints propagate honge
            if ac3(new_domains):
                if ac3_backtrack(board, new_domains):
                    return True

            # nahi chala - board restore karo (wapas purani state)
            for r in range(9):
                for c in range(9):
                    board[r][c] = saved_board[r][c]

    return False


# ============================================================
# Sudoku GUI Class - Tkinter wala interface
# ============================================================

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f0f0")

        # boards store karne ke liye
        self.current_board = [[0]*9 for _ in range(9)]
        self.original_board = [[0]*9 for _ in range(9)]
        self.solution_board = None  # hint ke liye solution yahan store hoga

        # GUI cells ka 2D array
        self.cells = [[None]*9 for _ in range(9)]

        # control variables - radio buttons aur dropdown ke liye
        self.algorithm_var = tk.StringVar(value="AC-3")
        self.puzzle_var = tk.IntVar(value=1)
        self.level_var = tk.StringVar(value="Easy")

        # GUI setup karo
        self.setup_gui()
        # pehla puzzle load karo
        self.load_puzzle()

    def setup_gui(self):
        """poora GUI yahan banta hai - grid, buttons, sab kuch"""

        # ---------- Menu bar - level select karne ke liye ----------
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        level_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label="Level", menu=level_menu)

        # teen difficulty levels
        for level in ["Easy", "Medium", "Hard"]:
            level_menu.add_command(
                label=level,
                command=lambda l=level: self.change_level(l)
            )

        # ---------- Main frame ----------
        main_frame = tk.Frame(self.root, padx=15, pady=15, bg="#f0f0f0")
        main_frame.pack()

        # ---------- Left side: Sudoku Grid ----------
        # 3x3 boxes ke liye nested frames banao - taake borders sahi dikhein
        grid_frame = tk.Frame(main_frame, bg="black", bd=2, relief="solid")
        grid_frame.grid(row=0, column=0, padx=(0, 25))

        for box_r in range(3):
            for box_c in range(3):
                # har 3x3 box ka apna frame hai
                box_frame = tk.Frame(grid_frame, bd=1, relief="solid", bg="black")
                box_frame.grid(row=box_r, column=box_c, padx=1, pady=1)

                for r in range(3):
                    for c in range(3):
                        # actual row aur column calculate karo
                        actual_r = box_r * 3 + r
                        actual_c = box_c * 3 + c

                        cell = tk.Entry(
                            box_frame,
                            width=3,
                            font=("Arial", 16),
                            justify="center",
                            bd=1,
                            relief="ridge",
                            bg="white"
                        )
                        cell.grid(row=r, column=c, padx=0, pady=0, ipady=5)
                        self.cells[actual_r][actual_c] = cell

        # ---------- Right side: Buttons aur Options ----------
        control_frame = tk.Frame(main_frame, bg="#f0f0f0")
        control_frame.grid(row=0, column=1, sticky="n")

        # Reset button - puzzle ko wapas original pe le jaata hai
        reset_btn = tk.Button(
            control_frame, text="Reset",
            width=14, height=2,
            font=("Arial", 10),
            command=self.reset_puzzle
        )
        reset_btn.pack(pady=(0, 8))

        # Solve button - algorithm se solve karta hai
        solve_btn = tk.Button(
            control_frame, text="Solve",
            width=14, height=2,
            font=("Arial", 10),
            command=self.solve_puzzle
        )
        solve_btn.pack(pady=(0, 8))

        # Hint button - ek cell ka jawab dikhata hai
        hint_btn = tk.Button(
            control_frame, text="Hint",
            width=14, height=2,
            font=("Arial", 10),
            command=self.give_hint
        )
        hint_btn.pack(pady=(0, 15))

        # ---------- Algorithm selection ----------
        algo_label = tk.Label(
            control_frame, text="Algorithms:",
            font=("Arial", 10, "bold"), bg="#f0f0f0"
        )
        algo_label.pack(anchor="w")

        ac3_radio = tk.Radiobutton(
            control_frame, text="Arc Consistency-3",
            variable=self.algorithm_var, value="AC-3",
            bg="#f0f0f0", font=("Arial", 9)
        )
        ac3_radio.pack(anchor="w")

        bt_radio = tk.Radiobutton(
            control_frame, text="Backtracking",
            variable=self.algorithm_var, value="Backtracking",
            bg="#f0f0f0", font=("Arial", 9)
        )
        bt_radio.pack(anchor="w", pady=(0, 15))

        # ---------- Puzzle selection - konsa puzzle chahiye ----------
        puzzle_label = tk.Label(
            control_frame, text="Choose Puzzle:",
            font=("Arial", 10, "bold"), bg="#f0f0f0"
        )
        puzzle_label.pack(anchor="w")

        for i in range(1, 5):
            rb = tk.Radiobutton(
                control_frame,
                text="Puzzle " + str(i),
                variable=self.puzzle_var,
                value=i,
                command=self.load_puzzle,
                bg="#f0f0f0",
                font=("Arial", 9)
            )
            rb.pack(anchor="w")

        # ---------- Bottom: Time display ----------
        self.time_label = tk.Label(
            self.root,
            text="Time:",
            font=("Arial", 11),
            anchor="w",
            padx=15,
            bg="#f0f0f0"
        )
        self.time_label.pack(fill="x", pady=(0, 10))

    def change_level(self, level):
        """jab user difficulty level change kare"""
        self.level_var.set(level)
        self.puzzle_var.set(1)
        self.load_puzzle()

    def load_puzzle(self):
        """puzzle dataset se load karke grid mein show karo"""
        level = self.level_var.get()
        puzzle_num = self.puzzle_var.get()

        # data nikalo
        puzzle = PUZZLES[level][puzzle_num - 1]

        # deep copy zaroori hai - warna original data kharab ho jayega
        self.current_board = copy.deepcopy(puzzle)
        self.original_board = copy.deepcopy(puzzle)
        self.solution_board = None
        self.time_label.config(text="Time:")

        self.update_grid()

    def update_grid(self):
        """board ki current state grid mein dikhao"""
        for r in range(9):
            for c in range(9):
                cell = self.cells[r][c]
                cell.config(state="normal")
                cell.delete(0, tk.END)

                if self.original_board[r][c] != 0:
                    # yeh original puzzle ki value hai - bold aur black
                    cell.insert(0, str(self.original_board[r][c]))
                    cell.config(
                        fg="black",
                        font=("Arial", 16, "bold"),
                        state="disabled",
                        disabledforeground="black",
                        disabledbackground="#e8e8e8"
                    )
                elif self.current_board[r][c] != 0:
                    # yeh solved ya hint wali value hai - red color
                    cell.insert(0, str(self.current_board[r][c]))
                    cell.config(fg="red", font=("Arial", 16), bg="white")
                else:
                    # khali cell - user type kar sakta hai
                    cell.config(fg="blue", font=("Arial", 16), bg="white")

    def read_grid(self):
        """grid se values parho - user ne kuch likha ho shayad"""
        for r in range(9):
            for c in range(9):
                cell = self.cells[r][c]
                val = cell.get().strip()

                if val and val.isdigit() and 1 <= int(val) <= 9:
                    self.current_board[r][c] = int(val)
                elif self.original_board[r][c] != 0:
                    self.current_board[r][c] = self.original_board[r][c]
                else:
                    self.current_board[r][c] = 0

    def reset_puzzle(self):
        """sab wapas original state mein - clean start"""
        self.current_board = copy.deepcopy(self.original_board)
        self.solution_board = None
        self.time_label.config(text="Time:")
        self.update_grid()

    def solve_puzzle(self):
        """selected algorithm se puzzle solve karo aur time bhi dikhao"""
        board = copy.deepcopy(self.original_board)
        algo = self.algorithm_var.get()

        # time measure karo
        start_time = time.time()

        if algo == "AC-3":
            solved = solve_ac3(board)
        else:
            solved = solve_backtracking(board)

        end_time = time.time()
        elapsed = end_time - start_time

        if solved:
            self.current_board = board
            self.solution_board = copy.deepcopy(board)
            self.update_grid()
            self.time_label.config(
                text="Time: " + str(round(elapsed, 4)) + " seconds"
            )
        else:
            messagebox.showerror("Error", "Is puzzle ka solution nahi mil saka!")
            self.time_label.config(text="Time: Failed")

    def give_hint(self):
        """ek empty cell ka sahi jawab dikhao - hint feature"""
        # user ki current state parho
        self.read_grid()

        # solution calculate karo agar pehle se nahi hua
        if self.solution_board is None:
            temp_board = copy.deepcopy(self.original_board)
            if solve_backtracking(temp_board):
                self.solution_board = temp_board
            else:
                messagebox.showerror("Error", "Puzzle solve nahi ho saka!")
                return

        # koi khali cell dhundo aur usme sahi value daal do
        for r in range(9):
            for c in range(9):
                if self.current_board[r][c] == 0:
                    correct_val = self.solution_board[r][c]
                    self.current_board[r][c] = correct_val

                    # cell mein green color se value dikhao
                    cell = self.cells[r][c]
                    cell.config(state="normal")
                    cell.delete(0, tk.END)
                    cell.insert(0, str(correct_val))
                    cell.config(fg="green", font=("Arial", 16))
                    return  # bas ek hint dena hai ek baar mein

        # agar sab cells bhar chuki hain
        messagebox.showinfo("Done", "Sudoku pehle se solved hai!")


# ============================================================
# Yahan se program start hota hai
# ============================================================

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGUI(root)
    root.mainloop()
