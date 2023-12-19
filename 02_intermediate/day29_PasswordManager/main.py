from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    with open(".data/pw.txt", mode="a") as data_file:
        new_entry = (website_entry.get(), username_entry.get(), password_entry.get())
        new_data = " | ".join(new_entry)
        data_file.write(new_data + "\n")

    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)


if __name__ == '__main__':
    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    # Password Manager logo
    canvas = Canvas(width=200, height=189, highlightthickness=0)
    logo_img = PhotoImage(file="img/logo.png")
    canvas.create_image(100, 94, image=logo_img)
    canvas.grid(column=0, row=0, columnspan=2)

    # Website UI element(s)
    website_label = Label(text="Website:")
    website_label.grid(column=0, row=1, sticky='e')

    website_entry = Entry(width=43)
    website_entry.grid(column=1, row=1, sticky='w')
    website_entry.focus()

    # Email/Username UI element(s)
    username_label = Label(text="Email/Username:")
    username_label.grid(column=0, row=2, sticky='e')

    username_entry = Entry(width=43)
    username_entry.grid(column=1, row=2, sticky='w')
    username_entry.insert(0, "example@email.com")

    # Password UI element(s)
    password_label = Label(text="Password:")
    password_label.grid(column=0, row=3, sticky='e')

    password_entry = Entry(width=21)
    password_entry.grid(column=1, row=3, sticky='w')

    # Password generator UI element(s)
    password_generator_btn = Button(text="Generate Password")
    password_generator_btn.grid(column=1, row=3, sticky='e')

    # Save password element(s)
    save_password_btn = Button(text="Add", width=36, command=save_password)
    save_password_btn.grid(column=1, row=4, sticky='w')

    window.mainloop()
