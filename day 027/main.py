# Day 27 working with TK inter a popular graphical user interface library for python

import tkinter
# init tkinter window
window = tkinter.Tk()
window.title("My first tkinter GUI")
window.minsize(width=500, height=300)

# event callback
def button_clicked():
    label.config(text=input.get())

#LABEL
# create component - Label
label = tkinter.Label(text="I am a Label", font=("Arial", 24, "italic bold"))
# display component on the screen
label.pack()


# BUTTON
# only method name, don't call the method
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# INPUT
# input.get() returns input text as string
# empty text field = input.get() returning empty string
input = tkinter.Entry()
input.pack()

# main loop that will keep the window open
# this line of code must be at the very end of the program
window.mainloop()