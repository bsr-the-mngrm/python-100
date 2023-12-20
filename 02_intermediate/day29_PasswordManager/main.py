from tkinter import *
from tkinter import messagebox
from password_generator import PasswordGenerator
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    generated_password = PasswordGenerator.generate()

    pyperclip.copy(generated_password)

    password_entry.delete(0, END)
    password_entry.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password
        }
    }

    if "" in new_data:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} "
                                                          f"\nPassword: {password} \nIs it ok to save")

    if is_ok:
        data = None
        try:
            with open(".data/pwd.json", mode="r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            # Load first data
            data = new_data
        else:
            # Updating old data with new data
            data.update(new_data)
        finally:
            with open(".data/pwd.json", mode="w") as data_file:
                # Saving data
                json.dump(data, data_file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open(".data/pwd.json", mode="r") as data_file:
            data = json.load(data_file)
        searched_data = data[website]
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="No data file found.")
    except KeyError:
        messagebox.showwarning(title="Warning", message="No details for the website exists")
    else:
        messagebox.showinfo(title="Information", message=f"Username: {searched_data['username']}\n"
                                                         f"Password: {searched_data['password']}")


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

    website_entry = Entry(width=23)
    website_entry.grid(column=1, row=1, sticky='w')
    website_entry.focus()

    # Password Search UI element(s)
    search_btn = Button(text="Search", width=15, command=find_password)
    search_btn.grid(column=1, row=1, sticky='e')

    # Email/Username UI element(s)
    username_label = Label(text="Email/Username:")
    username_label.grid(column=0, row=2, sticky='e')

    username_entry = Entry(width=43)
    username_entry.grid(column=1, row=2, sticky='w')
    username_entry.insert(0, "example@email.com")

    # Password UI element(s)
    password_label = Label(text="Password:")
    password_label.grid(column=0, row=3, sticky='e')

    password_entry = Entry(width=23)
    password_entry.grid(column=1, row=3, sticky='w')

    # Password generator UI element(s)
    password_generator_btn = Button(text="Generate Password", width=15, command=generate_password)
    password_generator_btn.grid(column=1, row=3, sticky='e')

    # Save password element(s)
    save_password_btn = Button(text="Add", width=36, command=save_password)
    save_password_btn.grid(column=1, row=4, sticky='w')

    window.mainloop()
