import tkinter as tk
class button:
    def __init__(self, screen, text, x, y, buttonWidth, buttonHeight, screenWidth, screenHeight, labelSize, functionOneName, functionTwoName, functionThreeName, function = None, secondFunction = None, thirdFunction = None):
        self.text = text
        self.screen = screen
        self.x = x
        self.y = y
        self.buttonWidth = buttonWidth
        self.buttonHeight = buttonHeight
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.labelSize = labelSize
        self.functionOneName = functionOneName
        self.functionTwoName = functionTwoName
        self.functionThreeName = functionThreeName
        self.function = function
        self.secondFunction = secondFunction
        self.thirdFunction = thirdFunction
        self.button = tk.Button(self.screen, width = buttonWidth, text=self.text)
    
    def getButton(self):
        return self.button
    
    def placeButton(self):
        self.button.place(x=self.x, y=self.y, width=self.buttonWidth, height=self.buttonHeight)

    def setToFirstFunction(self):
        self.button.config(text = self.functionOneName, command=self.function)

    def setToSecondFunction(self):
        self.button.config(text = self.functionTwoName, command=self.secondFunction)
    
    def setToThirdFunction(self):
        self.button.config(text = self.functionThreeName ,command=self.thirdFunction)
    
    def getFirstFunction(self):
        return self.function
    
    def getSecondFunction(self):
        return self.secondFunction

    def getThirdFunction(self):
        return self.thirdFunction