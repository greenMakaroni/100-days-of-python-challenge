THEME_COLOR = "#375362"

from tkinter import *
from quiz_brain import QuizBrain

class QuizzInterface:
    def __init__(self, quizz: QuizBrain):
        self.quizz_brain = quizz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(
            padx=20,
            pady=20,
            bg=THEME_COLOR)

        self.score_label = Label(
            text="Score: 0",
            fg="white",
            bg=THEME_COLOR)

        self.score_label.grid(
            row=0,
            column=1)

        self.canvas = Canvas(
            width=300,
            height=250,
            bg="white",)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Question text placeholder",
            fill=THEME_COLOR,
            font=("Arial", 16, "italic"))

        self.canvas.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=50)

        true_image = PhotoImage(file="./images/true.png")
        false_image = PhotoImage(file="./images/false.png")

        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quizz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quizz_brain.score}")
            q_text = self.quizz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quizz. Your score is {self.quizz_brain.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def true_pressed(self):
        self.feedback(self.quizz_brain.check_answer("True"))

    def false_pressed(self):
        self.feedback(self.quizz_brain.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)




