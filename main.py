from tkinter import *


root = Tk()
root.geometry("500x600")
root.title("Tic Tac Toe")

frame1 = Frame(root)
frame1.pack()
titleLabel = Label(frame1, text="Tic Tac Toe", font=("Arial", 30))
titleLabel.pack()



root.mainloop()
