from audioop import add
from buttonObj import newButton
from constants import Constants
import numpy as np

class Buttons:
    # global buttons
    def shift():
        for i in range(len(Buttons.buttons)):
            for j in range(len(Buttons.buttons[i])):
                Buttons.buttons[i][j].setToSecondFunction()

    def reset():
        Constants.currentText = ""
        Constants.label.config(text = Constants.currentText)
        for i in range(len(Buttons.buttons)):
            for j in range(len(Buttons.buttons[i])):
                Buttons.buttons[i][j].setToFirstFunction()

    def addToLabel(number):
        Constants.currentText += str(number)
        newText = Constants.currentText
        Constants.label.config(text = newText)
    
    def delButtonCommand():
        Constants.currentText = Constants.currentText[:-1]
        newText = Constants.currentText
        Constants.label.config(text = newText)

    # First Row Buttons
    numberZero = newButton(screen = Constants.screen, text = "0", relx = .1, rely = .9, buttonWidth = Constants.buttonWidth, 
    buttonHeight = Constants.buttonHeight, screenWidth = Constants.screenWidth, screenHeight = Constants.screenHeight, 
    labelSize = None, color = "Navy", functionOneName = "0", functionTwoName = None)
    
    decimalPoint = newButton(screen = Constants.screen, text = ".", relx = .3, rely = .9, buttonWidth = Constants.buttonWidth, 
    buttonHeight = Constants.buttonHeight, screenWidth = Constants.screenWidth, screenHeight = Constants.screenHeight, 
    labelSize = None, color = "Navy", functionOneName = ".", functionTwoName = "π")

    # Second Row Buttons
    numberOne = newButton(screen = Constants.screen, text = "1", relx = .1, rely = .8, buttonWidth = Constants.buttonWidth, 
    buttonHeight = Constants.buttonHeight, screenWidth = Constants.screenWidth, screenHeight = Constants.screenHeight, 
    labelSize = None, color = "Navy", functionOneName = "1", functionTwoName = None)
    
    numberTwo = newButton(screen = Constants.screen, text = "2", relx = .3, 
    rely = .8, buttonWidth = Constants.buttonWidth, buttonHeight = Constants.buttonHeight, screenWidth=Constants.screenWidth, 
    screenHeight=Constants.screenHeight, labelSize=None, color="Navy", functionOneName="2", functionTwoName=None)

    numberThree = newButton(screen = Constants.screen, text = "3", relx = .5, rely = .8, buttonWidth = Constants.buttonWidth, 
    buttonHeight = Constants.buttonHeight, screenWidth=Constants.screenWidth, screenHeight=Constants.screenHeight, 
    labelSize=None, color="Navy", functionOneName="3", functionTwoName=None)

    plusSign = newButton(screen = Constants.screen, text = "+", relx = .7,
    rely = .8, buttonWidth = Constants.buttonWidth, buttonHeight = Constants.buttonHeight, 
    screenWidth=Constants.screenWidth, screenHeight=Constants.screenHeight, 
    labelSize=None, color="Navy", functionOneName="+", functionTwoName=None) 

    minusSign = newButton(screen = Constants.screen, text = "-", relx = .9,
    rely = .8, buttonWidth = Constants.buttonWidth, buttonHeight = Constants.buttonHeight, 
    screenWidth=Constants.screenWidth, screenHeight=Constants.screenHeight, 
    labelSize=None, color="Navy", functionOneName="-", functionTwoName=None) 

    # Third Row Buttons
    numberFour = newButton(screen = Constants.screen, text = "-", relx = .1,
    rely = .7, buttonWidth = Constants.buttonWidth, buttonHeight = Constants.buttonHeight, 
    screenWidth=Constants.screenWidth, screenHeight=Constants.screenHeight, 
    labelSize=None, color="Navy", functionOneName="4", functionTwoName=None) 
    
    numberFive = newButton(screen = Constants.screen, text = "-", relx = .3,
    rely = .7, buttonWidth = Constants.buttonWidth, buttonHeight = Constants.buttonHeight, 
    screenWidth=Constants.screenWidth, screenHeight=Constants.screenHeight, 
    labelSize=None, color="Navy", functionOneName="5", functionTwoName=None) 

    numberSix = newButton(screen = Constants.screen, text = "-", relx = .5,
    rely = .7, buttonWidth = Constants.buttonWidth, buttonHeight = Constants.buttonHeight, 
    screenWidth=Constants.screenWidth, screenHeight=Constants.screenHeight, 
    labelSize=None, color="Navy", functionOneName="6", functionTwoName=None) 

    timesSign = newButton(screen = Constants.screen, text = "-", relx = .7,
    rely = .7, buttonWidth = Constants.buttonWidth, buttonHeight = Constants.buttonHeight, 
    screenWidth=Constants.screenWidth, screenHeight=Constants.screenHeight, 
    labelSize=None, color="Navy", functionOneName="x", functionTwoName=None) 

    divideSign = newButton(screen = Constants.screen, text = "-", relx = .9,
    rely = .7, buttonWidth = Constants.buttonWidth, buttonHeight = Constants.buttonHeight, 
    screenWidth=Constants.screenWidth, screenHeight=Constants.screenHeight, 
    labelSize=None, color="Navy", functionOneName="÷", functionTwoName=None) 

    # Fourth Row Buttons
    numberSeven  = newButton(screen = Constants.screen, text = "-", relx = .1,
    rely = .6, buttonWidth = Constants.buttonWidth, buttonHeight = Constants.buttonHeight, 
    screenWidth=Constants.screenWidth, screenHeight=Constants.screenHeight, 
    labelSize=None, color="Navy", functionOneName="7", functionTwoName=None) 

    numberEight = newButton(screen = Constants.screen, text = "-", relx = .3,
    rely = .6, buttonWidth = Constants.buttonWidth, buttonHeight = Constants.buttonHeight, 
    screenWidth=Constants.screenWidth, screenHeight=Constants.screenHeight, 
    labelSize=None, color="Navy", functionOneName="8", functionTwoName=None) 

    numberNine = newButton(screen = Constants.screen, text = "-", relx = .5,
    rely = .6, buttonWidth = Constants.buttonWidth, buttonHeight = Constants.buttonHeight, 
    screenWidth=Constants.screenWidth, screenHeight=Constants.screenHeight, 
    labelSize=None, color="Navy", functionOneName="9", functionTwoName=None) 

    delSign = newButton(screen = Constants.screen, text = "-", relx = .7,
    rely = .6, buttonWidth = Constants.buttonWidth, buttonHeight = Constants.buttonHeight, 
    screenWidth=Constants.screenWidth, screenHeight=Constants.screenHeight, 
    labelSize=None, color="Navy", functionOneName="DEL", functionTwoName=None) 

    clearButton = newButton(screen = Constants.screen, text = "-", relx = .9,
    rely = .6, buttonWidth = Constants.buttonWidth, buttonHeight = Constants.buttonHeight, 
    screenWidth=Constants.screenWidth, screenHeight=Constants.screenHeight, 
    labelSize=None, color="Navy", functionOneName="AC", functionTwoName=None) 


    # Seventh Row Buttons
    sqauredButton = newButton(screen = Constants.screen, text = "", relx = .1, rely = .4, buttonWidth = Constants.topButtonWidth, 
    buttonHeight = Constants.topButtonHeight, screenWidth = Constants.screenWidth, screenHeight = Constants.screenHeight, 
    labelSize = None, color = "Navy", functionOneName = "x^2", functionTwoName = "√")

    exponentButton = newButton(screen = Constants.screen, text = "Reset", relx = .25, rely = .4, buttonWidth = Constants.topButtonWidth, 
    buttonHeight = Constants.topButtonHeight, screenWidth = Constants.screenWidth, screenHeight = Constants.screenHeight, 
    labelSize = None, color = "Navy", functionOneName = "^", functionTwoName = "x√")


    # Eighth Row Buttons
    shiftButton = newButton(screen = Constants.screen, text = "Shift", relx = .1, 
    rely = .3, buttonWidth = Constants.topButtonWidth, buttonHeight = Constants.topButtonHeight, 
    screenWidth = Constants.screenWidth, screenHeight = Constants.screenHeight, labelSize = None, 
    color = "gold", functionOneName = "shift",functionTwoName = None)

    resetButton = newButton(screen = Constants.screen, text = "Reset", relx = .25, rely = .3, buttonWidth = Constants.topButtonWidth, 
    buttonHeight = Constants.topButtonHeight, screenWidth = Constants.screenWidth, screenHeight = Constants.screenHeight, 
    labelSize = None, color = "Navy", functionOneName = "reset", functionTwoName = None)

    sineButton = newButton(screen = Constants.screen, text = "Reset", relx = .4, rely = .3, buttonWidth = Constants.topButtonWidth, 
    buttonHeight = Constants.topButtonHeight, screenWidth = Constants.screenWidth, screenHeight = Constants.screenHeight, 
    labelSize = None, color = "Navy", functionOneName = "sin", functionTwoName = "sin^-1")

    cosineButton = newButton(screen = Constants.screen, text = "Reset", relx = .55, rely = .3, buttonWidth = Constants.topButtonWidth, 
    buttonHeight = Constants.topButtonHeight, screenWidth = Constants.screenWidth, screenHeight = Constants.screenHeight, 
    labelSize = None, color = "Navy", functionOneName = "cos", functionTwoName = "cos^-1")

    tangnetButton = newButton(screen = Constants.screen, text = "Reset", relx = .7, rely = .3, buttonWidth = Constants.topButtonWidth, 
    buttonHeight = Constants.topButtonHeight, screenWidth = Constants.screenWidth, screenHeight = Constants.screenHeight, 
    labelSize = None, color = "Navy", functionOneName = "tan", functionTwoName = "tan^-1")

    buttons = [[numberZero, decimalPoint],
    [numberOne, numberTwo, numberThree, plusSign, minusSign], 
    [numberFour, numberFive, numberSix, timesSign, divideSign], 
    [numberSeven, numberEight, numberNine, delSign, clearButton],
    [],
    [],
    [shiftButton, resetButton,],
    [sqauredButton, exponentButton, sineButton, cosineButton, tangnetButton]]

    shiftButton.tkbutton.config(command = shift)
    resetButton.tkbutton.config(command = reset)
    delSign.tkbutton.config(command = delButtonCommand)


    numberOne.tkbutton.config(command = lambda: Buttons.addToLabel('1') )
    numberTwo.tkbutton.config(command = lambda: Buttons.addToLabel('2'))
    numberThree.tkbutton.config(command = lambda: Buttons.addToLabel('3'))
    numberFour.tkbutton.config(command = lambda: Buttons.addToLabel('4'))
    numberFive.tkbutton.config(command = lambda: Buttons.addToLabel('5'))
    numberSix.tkbutton.config(command = lambda: Buttons.addToLabel('6'))
    numberSeven.tkbutton.config(command = lambda: Buttons.addToLabel('7'))
    numberEight.tkbutton.config(command = lambda: Buttons.addToLabel('8'))
    numberNine.tkbutton.config(command = lambda: Buttons.addToLabel('9'))