from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


if __name__ == '__main__':
    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Password Manager")
    window.config(padx=20, pady=20)

    # Password Manager logo
    canvas = Canvas(width=200, height=189, highlightthickness=0)
    logo_img = PhotoImage(file="img/logo.png")
    canvas.create_image(100, 94, image=logo_img)
    canvas.grid(column=0, row=0)

    window.mainloop()
