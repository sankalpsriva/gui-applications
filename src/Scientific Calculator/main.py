from tkinter import *
from constants import Constants 
from buttons import Buttons as b


def shift():
    for i in range(len(b.buttons)):
        for j in range(len(b.buttons[i])):
            b.buttons[i][j].setToSecondFunction()

root = Constants.screen
root.geometry("400x700+130-10")
root.title("Scientific Calculator")
root.configure(background = "white")



# Button Placement First Row
b.buttons[0][0].placeButton()
b.buttons[0][1].placeButton()


# Button Placement Second Row 
b.buttons[1][0].placeButton()
b.buttons[1][1].placeButton()
b.buttons[1][2].placeButton()
b.buttons[1][3].placeButton()
b.buttons[1][4].placeButton()


b.buttons[4][0].placeButton()
root.mainloop()