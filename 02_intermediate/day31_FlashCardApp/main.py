from tkinter import *
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
flip_timer = None
is_french = True
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

FRENCH_WORDS = data.to_dict(orient="records")


def get_word():
    return choice(FRENCH_WORDS)


def next_card():
    global current_card, flip_timer, is_french

    window.after_cancel(flip_timer)
    current_card = get_word()
    is_french = True

    canvas.itemconfig(lang, text="French", fill="black")
    canvas.itemconfig(word, text=f"{current_card['French']}", fill="black")
    canvas.itemconfig(bg_img, image=card_front_img)

    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    global is_french
    is_french = False

    canvas.itemconfig(lang, text="English", fill="white")
    canvas.itemconfig(word, text=f"{current_card['English']}", fill="white")
    canvas.itemconfig(bg_img, image=card_back_img)


def is_known():
    if is_french:
        FRENCH_WORDS.remove(current_card)
        df = pandas.DataFrame(FRENCH_WORDS)
        df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


if __name__ == '__main__':
    # ----------------------- UI SETUP ----------------------- #
    window = Tk()
    window.title("Flash Card App")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    flip_timer = window.after(3000, func=next_card)

    card_back_img = PhotoImage(file="images/card_back.png")
    card_front_img = PhotoImage(file="images/card_front.png")
    check_mark_img = PhotoImage(file="images/right.png")
    cross_mark_img = PhotoImage(file="images/wrong.png")

    # Flash Card
    canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
    bg_img = canvas.create_image(400, 263, image=card_front_img)
    lang = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), tags="language")
    word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), tags="word")
    canvas.grid(column=0, row=0, columnspan=2)

    # Cross mark button
    cross_mark_btn = Button(image=cross_mark_img, highlightthickness=0, command=flip_card)
    cross_mark_btn.grid(column=0, row=1)

    # Check mark button
    check_mark_btn = Button(image=check_mark_img, highlightthickness=0, command=is_known)
    check_mark_btn.grid(column=1, row=1)

    next_card()

    window.mainloop()
