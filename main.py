from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x600")
root.title("Tic Tac Toe")

frame1 = Frame(root)
frame1.grid(row=0, pady=12)
titleLabel = Label(frame1, text="Tic Tac Toe",width=22, font=("Arial", 30))
titleLabel.grid(row=0, column=0)

board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}



def checkForWinner(player):
    if board[1] == board[2] == board[3] and board[3] == player:
        return True
    elif board[4] == board[5] == board[6] and board[6] == player:
        return True
    elif board[7] == board[8] == board[9] and board[9] == player:
        return True
    elif board[1] == board[4] == board[7] and board[7] == player:
        return True
    elif board[2] == board[5] == board[8] and board[8] == player:
        return True
    elif board[3] == board[6] == board[9] and board[9] == player:
        return True
    elif board[1] == board[5] == board[9] and board[3] == player:
        return True
    elif board[3] == board[5] == board[7] and board[7] == player:
        return True

    else:
        return False

def checkForDraw():
    for i in board.keys():
        if board[i] == " ":
            return False
    return True

def restartGame():
    global board
    for button in buttons:
        button["text"] = " "
    board = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '
    }
    turn = "X"
    titleLabel = Label(frame1, text="Tic Tac Toe", width=22, font=("Arial", 30))
    titleLabel.grid(row=0, column=0)

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

                winnerLabel = Label(frame1, text=f"{turn} is winner", font=("Arial", 30),width=22, height=1,
                                    bg="#3a405a", fg="White")
                winnerLabel.grid(row=0, column=0)

            turn = "O"
        else:
            button["text"] = "O"
            board[clicked] = turn
            if checkForWinner(turn):
                winnerLabel = Label(frame1, text=f"{turn} is winner", font=("Arial", 30), width=22, height=1,
                                    bg="#3a405a", fg="White")
                winnerLabel.grid(row=0, column=0)

            turn = "X"

        if checkForDraw():
            winnerLabel = Label(frame1, text=f"Game Draw", font=("Arial", 30), width=22, height=1,
                                bg="#3a405a", fg="White")
            winnerLabel.grid(row=0, column=0)

    print(board)
# Board setup
boardFrame = Frame(root)
boardFrame.grid(row=1)

# frist row
Grid1 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30), relief=RAISED, border=5)
Grid1.grid(row=0, column=0)
Grid1.bind("<Button-1>", play)

Grid2 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30), relief=RAISED, border=5)
Grid2.grid(row=0, column=1)
Grid2.bind("<Button-1>", play)

Grid3 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30), relief=RAISED, border=5)
Grid3.grid(row=0, column=2)
Grid3.bind("<Button-1>", play)

# Second row
Grid4 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30), relief=RAISED, border=5)
Grid4.grid(row=1, column=0)
Grid4.bind("<Button-1>", play)

Grid5 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30), relief=RAISED, border=5)
Grid5.grid(row=1, column=1)
Grid5.bind("<Button-1>", play)

Grid6 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30), relief=RAISED, border=5)
Grid6.grid(row=1, column=2)
Grid6.bind("<Button-1>", play)

# third row
Grid7 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30), relief=RAISED, border=5)
Grid7.grid(row=2, column=0)
Grid7.bind("<Button-1>", play)


Grid8 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30), relief=RAISED, border=5)
Grid8.grid(row=2, column=1)
Grid8.bind("<Button-1>", play)

Grid9 = Button(boardFrame, text=" ", width=4, height=2, font=("Arial", 30), relief=RAISED, border=5)
Grid9.grid(row=2, column=2)
Grid9.bind("<Button-1>", play)

restartFrame = Frame(root)
restartFrame.grid(row=3, pady=12)
restartButton = Button(restartFrame, text="Restart Game", width=12, height=1, command=restartGame)
restartButton.grid(row=4, column=0)
buttons = [Grid1, Grid2, Grid3, Grid4, Grid5, Grid6, Grid7, Grid8, Grid9]



winFrame = Frame(root, width=22)
winFrame.grid(row=4, pady=12)
root.mainloop()
