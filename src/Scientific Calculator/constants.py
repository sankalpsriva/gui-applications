import tkinter as tk
class Constants:
    # Constants for the Scientific Calculator 
    currentText = ""
    screen =  tk.Tk()
    label = tk.Label(screen, text = currentText, font = ("Arial", 20), bg = "white")
    screenWidth = 400
    screenHeight = 700
    buttonWidth = 5
    buttonHeight = 2 
    topButtonWidth = 3
    topButtonHeight = 1