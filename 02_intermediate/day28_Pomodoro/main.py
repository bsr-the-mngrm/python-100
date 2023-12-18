from tkinter import *
import time

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


if __name__ == '__main__':
    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
    title_label.grid(column=1, row=0)

    # Tomato image settings
    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_photo = PhotoImage(file="img/tomato.png")
    canvas.create_image(100, 112, image=tomato_photo)
    canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
    canvas.grid(column=1, row=1)



    window.mainloop()
