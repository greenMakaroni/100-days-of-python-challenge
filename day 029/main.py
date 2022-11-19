from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
print("he")

# window setup
window = Tk()
window.title("Password manager")
window.config(padx=40, pady=40)

# canvas setup
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Inputs
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(column=1,row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Buttons
generate_password_button = Button(text="Generate password")
generate_password_button.grid(column=2, row=3)
add_password_button = Button(text="Add Password", width=36)
add_password_button.grid(column=1, row=4, columnspan=2)

window.mainloop()