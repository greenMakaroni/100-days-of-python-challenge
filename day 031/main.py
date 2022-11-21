#bg color
BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *

# window setup
window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# canvas setup
canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

# images setup
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
cross_image = PhotoImage(file="images/wrong.png")
tick_image = PhotoImage(file="images/right.png")

canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0, columnspan=2)

# buttons setup
red_button = Button(image=cross_image)
green_button = Button(image=tick_image)
green_button.grid(row=1, column=0)
red_button.grid(row=1, column=1)

# text setup
canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))










# keep main window open in a loop
window.mainloop()


