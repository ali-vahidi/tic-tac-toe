import tkinter as tk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title("Tic Tac Toe")

turn = "X"
result = [""] * 9
points = [0, 0]
buttons = []

def clicked(btn):
    global turn
    btn = int(btn)
    if result[btn] == "":
        result[btn] = turn
        buttons[btn]["text"] = turn
        buttons[btn]["state"] = tk.DISABLED
        buttons[btn]["relief"] = tk.GROOVE

        if turn == "X":
            buttons[btn]["bg"] = "white"
            buttons[btn]["fg"] = "white"
            turn = "O"
        else:
            buttons[btn]["bg"] = "black"
            buttons[btn]["fg"] = "white"
            turn = "X"
        win()

def win():
    combos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    for combo in combos:
        if result[combo[0]] == result[combo[1]] == result[combo[2]] != "":
            show_winner(result[combo[0]])
            return
    check_draw()

def show_winner(winner):
    if winner == "X":
        showinfo("End", "Player 1 wins")
        points[0] += 1
    else:
        showinfo("End", "Player 2 wins")
        points[1] += 1
    reset()

def check_draw():
    if "" not in result:
        showinfo("End", "Draw")
        reset()

def reset():
    global result, turn
    result = [""] * 9
    turn = "X"
    for widget in window.winfo_children():
        widget.destroy()
    point()
    board()

def point():
    board_frame = tk.Frame(window)
    board_frame.grid(row=0)
    tk.Label(board_frame, text="Player 1", padx=10).grid(row=0, column=0)
    tk.Label(board_frame, text="Player 2", padx=10).grid(row=0, column=2)

    point_frame = tk.Frame(window)
    point_frame.grid(row=1)
    tk.Label(point_frame, text=points[0], padx=20).grid(row=0, column=0)
    tk.Label(point_frame, text=points[1], padx=20).grid(row=0, column=1)

def board():
    global buttons
    buttons = []
    board_frame = tk.Frame(window)
    board_frame.grid(row=2)
    counter = 0
    for row in range(3):
        for col in range(3):
            index = counter
            button = tk.Button(board_frame, command=lambda x=index: clicked(x))
            button.config(width=10, height=4)
            button.grid(row=row, column=col)
            buttons.append(button)
            counter += 1

point()
board()
window.mainloop()
