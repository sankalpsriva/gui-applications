import turtle 
from tkinter import *

mRed = "orangered1"
mBlue = "DeepSkyBlue3"
mYellow = "gold1"
mGreen = "chartreuse3"
# screen_width = turtle.screensize()[0]
# screen_height = turtle.screensize()[1]

# Turtle variables 
WIDTH_BETWEEN = 10

# Functions
def square(color, forward = 100):
    turtle.pendown()
    turtle.pensize(1)
    turtle.color(color, color)
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.forward(forward)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()

def target():
    try:
        turtle.reset()
    except Exception:
        pass
    turtle.speed(100)
    turtle.hideturtle()
    turtle.color('red', 'red')
    turtle.penup()
    turtle.goto(0,-200)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(200)
    turtle.end_fill()
    turtle.goto(0,-150)
    turtle.color("white", "white")
    turtle.begin_fill()
    turtle.circle(150)
    turtle.end_fill()
    turtle.color('red', 'red')
    turtle.penup()
    turtle.goto(0,-50)
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    



def dominos():
    try:
        turtle.reset()
    except Exception:
        pass
    turtle.speed(100)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-75,50)
    turtle.right(45)
    turtle.begin_fill()
    square("blue", forward = 200)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(75,200)
    square("red", forward = 200)
    turtle.penup()

    turtle.goto(45, 30)
    turtle.pendown()
    turtle.width(5)
    turtle.begin_fill()
    turtle.color("white")
    turtle.circle(40)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-165, -115)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(40)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(-50, -120)
    turtle.begin_fill()
    turtle.pendown()
    turtle.circle(40)
    turtle.end_fill()


def microsoft():
    try:
        turtle.reset()
    except Exception:
        pass
    turtle.bgcolor("black")
    turtle.hideturtle()
    turtle.speed(100)
    turtle.penup()
    turtle.goto(-200, 600 / 25)
    # Yellow Square
    square(mYellow)

    # Green Square
    turtle.left(90)
    turtle.forward(WIDTH_BETWEEN)
    square(mGreen)

    # Red Square
    turtle.left(90)
    turtle.forward(WIDTH_BETWEEN)
    square(mRed)

    # Blue Square
    turtle.left(90)
    turtle.forward(WIDTH_BETWEEN)
    square(mBlue)

    turtle.color("white")
    turtle.goto(-75,-45)
    turtle.color("white")
    turtle.write("Microsoft", move = False, align = 'left', font = ("segoe", 70, 'normal'))
    root.mainloop()
    turtle.mainloop()


# Tkinter Start
root = Tk()
root.geometry("600x600")
root.config(bg = 'black')
root.title("Logo Selector")

microsoftButton = Button(root, text = "Microsoft", bg = 'black', fg = 'white', command = microsoft, padx = 600 / 6 , pady = 600 / 6)
targetButton = Button(root, text = "Target", bg = 'black', fg = 'white', command = target, padx = 600 / 6 , pady = 600 / 6)
dominosLogo = Button(root, text = "Dominos", bg = 'black', fg = 'white', command = dominos, padx = 600 / 6 , pady = 600 / 6)

microsoftButton.place(relx = .75, rely = .1, anchor = N)
targetButton.place(relx = .25, rely = .1, anchor = N)
dominosLogo.place(relx = .5, rely = .55, anchor = N)

root.mainloop()