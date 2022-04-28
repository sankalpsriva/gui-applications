# Import Statements
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import string

global hist
global perc
# Global Variables
letters = string.ascii_lowercase
symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`',
'}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
x_data = [i for i in letters]
y_data = []
y_data_perc = []

# Sankalp Srivastava 02/13/2022
# Functions

# Letter Count
def count_letter(letter, sentence):
    count = 0
    for i in sentence:
        if i == letter:
            count += 1
    return count

def count_char(sentence):
    char_count = 0
    special_char_count = 0
    for i in sentence:
        if i in letters:
            char_count += 1
        if i in symbols:
            special_char_count += 1

    return [char_count, special_char_count]

def word_count_sentence(sentence):
    count = 0
    if sentence[0] in letters:
        count += 1
    for i in sentence:
        if i == " ":
            count += 1
    return count

def analyze():
    try:
        global sentence
        global y_data
        global y_data_perc
        global c_count
        y_data.clear()
        y_data_perc.clear()

        exact_sentence = entry.get()
        sentence = (entry.get()).lower()
        word_count = word_count_sentence(sentence) # len(sentence.split(" "))
        c_count = count_char(sentence)
        perc['state'] = 'normal'
        hist['state'] = 'normal'
        if c_count[0] > 0:
            for i in letters:
                y_data.append(count_letter(i ,sentence))
                y_data_perc.append(round((count_letter(i, sentence) / c_count[0]) * 100, 1))

        label.config(text = f"This text sample contains {word_count} words and {c_count[0]} characters with {c_count[1]} symbols \n Text: {exact_sentence}", bg = "black", fg = "white") # Text: {sentence}")
        label.place(relx = .5, rely = .1, anchor = N)
        entry.delete(0, END)
        graph()
    except IndexError:
        label.config(text = "Invalid Text Entered Please Try Again", fg = "red")
        label.place(relx = .5, rely = .1, anchor = N)
        perc['state'] = 'disabled'
        hist['state'] = 'disabled'

def on_closing():
    root.destroy()
    try:
        root2.destroy()
    except TclError:
        pass
    except NameError:
        pass

def graph():
    hist.place(relx = .3, rely = .2, anchor = N)
    perc.place(relx = .7, rely = .2, anchor = N)

def hist_graph():
    plt.close()
    plt.title("Histogram")
    plt.bar(x_data, y_data)
    plt.xlabel("Letters")
    plt.ylabel("Count")
    plt.show()

def perc_graph():
    global root2
    root2 = Tk()
    root2.title("Percentages")
    root2.geometry("500x550")
    root2.config(bg = "black")
    if c_count[0] > 0:
        for i in letters:
            label = Label(root2, text = f"{i}: {round((count_letter(i, sentence) / c_count[0]) * 100, 1)}%", fg = "white", bg = "black")
            label.pack()
    root2.mainloop()

# Main Window
root = Tk()
root.geometry("500x500")
root.title("Text Analyzer")
root.config(bg = "black")


label = Label(root, fg = "white", bg = "black")

entry = Entry(root, width = 83, bg = "white", fg = "black")
entry.insert(0, "Delete this and enter text here!")

button = Button(root, text = "Analyze", command = analyze, bg = "black", fg = "white")
button.place(relx = .5,rely = .05, anchor = N)


entry.focus_set()
entry.place(relx = .5, rely = 0, anchor = N)

hist = Button(root, text = "Histogram", bg = "black", fg = "white", command = hist_graph)
perc = Button(root, text = "Percentages", bg = "black", fg = "white", command = perc_graph)

plt.style.use("dark_background")

# Protocol for closing both GUI windows if Percentages GUI isn't closed
root.protocol("WM_DELETE_WINDOW", on_closing)

# GUI Loop
root.mainloop()
