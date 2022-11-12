from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
# Pomodoro technique
# 25 min work
# 5 min break
# 25 min work
# 5 min break
# 25 min work
# 5 min break
# 25 min work
# 20 min break

def start_timer():
    global REPS

    if REPS == 8:
        count_down(20 * 60)
        REPS = 1
    elif REPS < 8 and REPS % 2 != 0:
        count_down(25 * 60)
        REPS += 1
    else:
        count_down(5 * 60)
        REPS += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global window
    minutes = math.floor(count / 60)
    seconds = count % 60

    # if seconds is a single digit append 0 to the front 0 = 00 / 1 = 01 etc...
    if len(str(seconds)) == 1:
        seconds = f"0{seconds}"

    if len(str(minutes)) == 1:
        minutes = f"0{minutes}"

    # way to mutate element in a canvas
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)
        print(count)

# ---------------------------- UI SETUP ------------------------------- #



# Window setup
window = Tk()
window.title("Python Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# Time function, 1st arg is delay, second arg is a function to execute after the delay

# Label element
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

# Buttons
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=2)

# Checkmarks
check_mark = Label(text="✔", highlightthickness=0, bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)

# canvas widgets
tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Keep window open
window.mainloop()
