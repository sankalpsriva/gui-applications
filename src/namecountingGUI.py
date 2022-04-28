from string import ascii_lowercase as lower
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("600x200")
root.config(bg = "black")
root.title("Name Counting")

def isRunning():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            root.destroy()
global firstName, lastName, firstNameCount, lastNameCount

label = Label(root, text = "Count your name!", font = ("Times New Roman", 30), fg = "white", bg = "black")

firstName = Entry(root, width = 30, bg = "black", fg = "white", justify = "center")
firstName.insert(0, "Enter you First Name here.")
firstName.focus_set()

lastName = Entry(root, width = 30, bg = "black", fg = "white", justify = "center")
lastName.insert(0, "Enter you Last Name here.")
lastName.focus_set()


label.place(anchor = N, relx = .5, rely = .02)
firstName.place(anchor = N, relx = .25, rely = .35)
lastName.place(anchor = N, relx = .75, rely = .35)

firstNameCount = Label(root, text = "", bg = "black", fg = "white")
lastNameCount = Label(root, text = "", bg = "black", fg = "white")

def getName():
    fName = firstName.get()
    lName = lastName.get()

    firstName.delete(0, END)
    lastName.delete(0, END)

    firstNameSum = sum([lower.find(i) + 1 for i in fName.lower()])
    lastNameSum = sum([lower.find(i) + 1 for i in lName.lower()])

    firstNameCount.config(text = firstNameSum)
    lastNameCount.config(text = lastNameSum)

button = Button(root, text = "Click to count your name!", bg = "black", fg = "white", command = getName)
button.place(anchor = N, relx = .5, rely = .7)
firstNameCount.place(anchor = N, relx = .25, rely = .55)
lastNameCount.place(anchor = N, relx = .75, rely = .55)

root.protocol("WM_DELETE_WINDOW", isRunning)
root.mainloop()