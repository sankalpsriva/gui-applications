from tkinter import *
from constants import Constants 
from buttons import Buttons as b

b.reset()
root = Constants.screen
root.geometry("400x700+130-10")
root.title("Scientific Calculator")
root.configure(background = "white")
Constants.label.place(relx = .5, rely = .05, anchor = N)


# Button Placement First Row
b.buttons[0][0].placeButton()
b.buttons[0][1].placeButton()


# Button Placement Second Row 
b.buttons[1][0].placeButton()
b.buttons[1][1].placeButton()
b.buttons[1][2].placeButton()
b.buttons[1][3].placeButton()
b.buttons[1][4].placeButton()

# Button Placement Third Row
b.buttons[2][0].placeButton()
b.buttons[2][1].placeButton()
b.buttons[2][2].placeButton()
b.buttons[2][3].placeButton()
b.buttons[2][4].placeButton()

b.buttons[3][0].placeButton()
b.buttons[3][1].placeButton()
b.buttons[3][2].placeButton()
b.buttons[3][3].placeButton()
b.buttons[3][4].placeButton()

b.buttons[6][0].placeButton()
b.buttons[6][1].placeButton()

b.buttons[7][0].placeButton()
b.buttons[7][1].placeButton()
b.buttons[7][2].placeButton()
b.buttons[7][3].placeButton()
b.buttons[7][4].placeButton()


root.mainloop()