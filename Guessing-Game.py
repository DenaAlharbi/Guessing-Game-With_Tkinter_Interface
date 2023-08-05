from random import randint
from tkinter import *

root = Tk()
root.title("The Guessing Game")

photo = PhotoImage(file="guessing_game_icon.png")
root.iconphoto(False, photo)
root.eval("tk::PlaceWindow . center")

myLabel = Label(root, text="Hello! Welcome to my game ;)\n Enter a guess: ")
myLabel.pack()

e = Entry(root, width=20, font=('Helvetica', 24))  # This alone creates an input box
e.pack()


def game():
    randomB = randint(1, 9)
    randomB = str(randomB)
    if randomB == e.get():
        text1 = "You have won"
        myLabel1 = Label(root, text=text1)  # This enters the text based on the variable
        myLabel1.pack()
    else:
        text1 = "You have lost"
        myLabel1 = Label(root, text=text1)  # This enters the text based on the variable
        myLabel1.pack()


myButton = Button(root, text="Click Me!", command=game)
myButton.pack()

root.mainloop()
