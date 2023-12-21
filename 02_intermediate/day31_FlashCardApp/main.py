from tkinter import *
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FRENCH_WORDS = pandas.read_csv("data/french_words.csv").to_dict(orient="records")


if __name__ == '__main__':
    # ----------------------- UI SETUP ----------------------- #
    window = Tk()
    window.title("Flash Card App")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

    card_back_img = PhotoImage(file="images/card_back.png")
    card_front_img = PhotoImage(file="images/card_front.png")
    check_mark_img = PhotoImage(file="images/right.png")
    cross_mark_img = PhotoImage(file="images/wrong.png")

    # Flash Card
    canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
    canvas.create_image(400, 263, image=card_back_img)
    canvas.grid(column=0, row=0, columnspan=2)
    canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"), tags="language")
    canvas.create_text(400, 263, text="ui", font=("Ariel", 60, "bold"), tags="word")

    # Cross mark button
    cross_mark_btn = Button(image=cross_mark_img, highlightthickness=0)
    cross_mark_btn.grid(column=0, row=1)

    # Check mark button
    check_mark_btn = Button(image=check_mark_img, highlightthickness=0)
    check_mark_btn.grid(column=1, row=1)

    window.mainloop()
