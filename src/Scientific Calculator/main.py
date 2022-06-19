from tkinter import *
import buttonObj

root = Tk()
root.geometry("400x700+130-10")
root.title("Scientific Calculator")
root.configure(background="white")

screenWidth = 400
screenHeight = 700
buttonWidth = None # will be set later should be number of buttons divided by width of screen
buttonHeight = None # will be set later should be number of buttons divided by height of screen

numberOne = buttonObj.button(root, "AC", .5, .5, 5, screenWidth, screenHeight, "30").getButton()
root.mainloop()