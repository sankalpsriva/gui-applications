import tkinter as tk
class newButton:
    def __init__(self, screen, text, relx, rely, buttonWidth, buttonHeight, screenWidth, screenHeight, labelSize, color, functionOneName, functionTwoName, function = None, secondFunction = None):
        self.text = text
        self.screen = screen
        self.x = relx
        self.y = rely
        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.labelSize = labelSize
        self.color = color
        self.functionOneName = functionOneName
        self.functionTwoName = functionTwoName
        self.function = function
        self.secondFunction = secondFunction
        self.tkbutton = tk.Button(self.screen, width = buttonWidth, bg = self.color, fg = "white", height = buttonHeight, text=self.text, command = function)
        
    def placeButton(self):
        self.tkbutton.place(relx = self.x, rely = self.y, anchor = tk.N)

    def setToFirstFunction(self):
        self.tkbutton.config(text = self.functionOneName, command=self.function)

    def setToSecondFunction(self):
        self.tkbutton.config(text = self.functionTwoName, command=self.secondFunction)
    
    def getFirstFunction(self):
        return self.function
    
    def getSecondFunction(self):
        return self.secondFunction
