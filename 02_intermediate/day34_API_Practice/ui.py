from tkinter import *

THEME_COLOR = "#375362"
SCORE_COLOR = "white"
SCORE_FONT = ("Arial", 12, "bold")
QUESTION_BG_COLOR = "white"
QUESTION_COLOR = THEME_COLOR
QUESTION_FONT = ("Arial", 16, "italic")


class QuizInterface:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", font=SCORE_FONT, bg=THEME_COLOR, fg=SCORE_COLOR)
        self.score_label.grid(column=1, row=0)

        self.question_canvas = Canvas(width=300, height=250, bg=QUESTION_BG_COLOR, highlightthickness=0)
        self.question_canvas.create_text(150, 125, text="First Question?", font=QUESTION_FONT, fill=QUESTION_COLOR)
        self.question_canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=50)

        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        self.true_canvas = Canvas(width=100, height=97, highlightthickness=0)
        self.true_canvas.create_image(50, 48, image=true_img)
        self.true_canvas.grid(column=0, row=2)

        self.false_canvas = Canvas(width=100, height=97, highlightthickness=0)
        self.false_canvas.create_image(50, 48, image=false_img)
        self.false_canvas.grid(column=1, row=2)

        self.window.mainloop()
