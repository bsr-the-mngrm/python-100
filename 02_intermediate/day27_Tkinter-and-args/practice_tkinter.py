from tkinter import *


def button_clicked():
    print("I got clicked!")
    my_label["text"] = textbox.get()


if __name__ == '__main__':
    window = Tk()

    window.title("Hello World w/ GUI")
    window.minsize(width=500, height=300)

    # Label
    my_label = Label(text="I am a Label!", font=('Ariel', 24, "normal"))
    my_label.pack()

    my_label["text"] = "New text"
    my_label.config(text="Third Text")

    # Button
    button = Button(text="Click Me", command=button_clicked)
    button.pack()

    # Textbox/Entry
    textbox = Entry(width=10)
    textbox.pack()

    window.mainloop()
