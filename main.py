from tkinter import *


root = Tk()
root.geometry("500x600")
root.title("Tic Tac Toe")

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1, text="Tic Tac Toe", font=("Arial", 30))
titleLabel.pack()



turn = "X"
def play(event):
    global turn
    button = event.widget

    if turn == 'X':
        button["text"] = "X"
        turn = "O"
    else:
        button["text"] = "O"
        turn = "X"
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
