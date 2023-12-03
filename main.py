from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x600")
root.title("Tic Tac Toe")

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1, text="Tic Tac Toe", font=("Arial", 30))
titleLabel.pack()

board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

def _winnerHelper(player):
    messagebox.showinfo("Game Over", f"{player} wins the game")


def checkForWinner(player):
    if board[1] == board[2] == board[3] and board[3] == player:
        _winnerHelper(player)
    elif board[4] == board[5] == board[6] and board[6] == player:
        _winnerHelper(player)
    elif board[7] == board[8] == board[9] and board[9] == player:
        _winnerHelper(player)
    elif board[1] == board[4] == board[7] and board[7] == player:
        _winnerHelper(player)
    elif board[2] == board[5] == board[8] and board[8] == player:
        _winnerHelper(player)
    elif board[3] == board[6] == board[9] and board[9] == player:
        _winnerHelper(player)
    elif board[1] == board[5] == board[9] and board[3] == player:
        _winnerHelper(player)
    elif board[3] == board[5] == board[7] and board[7] == player:
        _winnerHelper(player)

    else:
        return False

def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True

turn = "X"
def play(event):
    global turn
    button = event.widget
    buttonText = str(button)
    clicked = buttonText[-1]

    if clicked == "n":
        clicked = 1
    else:
        clicked = int(clicked)

    if button["text"] == " ":
        if turn == 'X':
            button["text"] = "X"
            board[clicked] = turn
            if checkForWinner(turn):
                print(turn, " is winner")
                print("Game Over")
            turn = "O"
        else:
            button["text"] = "O"
            board[clicked] = turn
            if checkForWinner(turn):
                print(turn, " is winner")
                print("Game Over")
            turn = "X"

        if checkForDraw():
            messagebox.showinfo("Game Over", "Game Draw")

    print(board)
# Board setup
boardFrame = Frame(root)
boardFrame.pack()

# frist row
Grid1 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30))
Grid1.grid(row=0, column=0)
Grid1.bind("<Button-1>", play)

Grid2 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30))
Grid2.grid(row=0, column=1)
Grid2.bind("<Button-1>", play)

Grid3 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30))
Grid3.grid(row=0, column=2)
Grid3.bind("<Button-1>", play)

# Second row
Grid4 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30))
Grid4.grid(row=1, column=0)
Grid4.bind("<Button-1>", play)

Grid5 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30))
Grid5.grid(row=1, column=1)
Grid5.bind("<Button-1>", play)

Grid6 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30))
Grid6.grid(row=1, column=2)
Grid6.bind("<Button-1>", play)

# third row
Grid7 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30))
Grid7.grid(row=2, column=0)
Grid7.bind("<Button-1>", play)


Grid8 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30))
Grid8.grid(row=2, column=1)
Grid8.bind("<Button-1>", play)

Grid9 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30))
Grid9.grid(row=2, column=2)
Grid9.bind("<Button-1>", play)

root.mainloop()
