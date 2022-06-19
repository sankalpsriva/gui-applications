from buttonObj import newButton
from constants import Constants
import numpy as np

def shift():
    for i in range(len(Buttons.buttons)):
        for j in range(len(Buttons.buttons[i])):
            Buttons.buttons[i][j].setToSecondFunction()
class Buttons:
    # global buttons
    # First Row Buttons
    numberZero = newButton(screen = Constants.screen, text = "0", relx = .1, rely = .9, buttonWidth = Constants.buttonWidth, 
    buttonHeight = Constants.buttonHeight, screenWidth = Constants.screenWidth, screenHeight = Constants.screenHeight, 
    labelSize = None, color = "Navy", functionOneName = "1", functionTwoName = None)
    
    decimalPoint = newButton(screen = Constants.screen, text = ".", relx = .3, rely = .9, buttonWidth = Constants.buttonWidth, 
    buttonHeight = Constants.buttonHeight, screenWidth = Constants.screenWidth, screenHeight = Constants.screenHeight, 
    labelSize = None, color = "Navy", functionOneName = "1", functionTwoName = "π")









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

    


    # Eighth Row Buttons
    shiftButton = newButton(screen = Constants.screen, text = "Shift", relx = .1, 
    rely = .1, buttonWidth = Constants.buttonWidth, buttonHeight = Constants.buttonHeight, 
    screenWidth = Constants.screenWidth, screenHeight = Constants.screenHeight, labelSize = None, 
    color = "Navy", functionOneName = "shift",functionTwoName = None)

    buttons = [[numberZero, decimalPoint],
    [numberOne, numberTwo, numberThree, plusSign, minusSign], 
    [], 
    [],
    [shiftButton]]

    shiftButton.tkbutton.config(command = shift)