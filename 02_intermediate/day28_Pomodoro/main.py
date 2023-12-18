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
def countdown(count):
    canvas.itemconfig(timer_text, text=count)
    if count > 0:
        window.after(1000, countdown, count-1)


if __name__ == '__main__':
    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Pomodoro")
    window.config(padx=100, pady=50, bg=YELLOW)

    # Title label
    title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
    title_label.grid(column=1, row=0)

    # Tomato image settings
    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_photo = PhotoImage(file="img/tomato.png")
    canvas.create_image(100, 112, image=tomato_photo)
    timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
    canvas.grid(column=1, row=1)

    # Start button
    start_button = Button(text="Start", highlightthickness=0)
    start_button.grid(column=0, row=2)

    # Reset button
    reset_button = Button(text="Reset", highlightthickness=0)
    reset_button.grid(column=2, row=2)

    # Checkmarks
    check_marks = Label(text="✓", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18, "bold"))
    check_marks.grid(column=1, row=3)

    # Call countdown mechanism
    countdown(5)

    window.mainloop()
