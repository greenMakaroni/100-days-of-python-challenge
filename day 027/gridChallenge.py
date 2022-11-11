
from tkinter import *

# init tkinter window
window = Tk()
window.title("My second GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#Label
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

def button_clicked():
    my_label.config(text=input.get())

#Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)


#Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3, row=2)

window.mainloop()