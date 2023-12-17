from tkinter import *


def button_clicked():
    print("I got clicked!")
    my_label["text"] = textbox.get()


if __name__ == '__main__':
    window = Tk()

    window.title("Hello World w/ GUI")
    window.minsize(width=500, height=300)
    # set padding:
    window.config(padx=20, pady=20)

    # Label
    my_label = Label(text="I am a Label!", font=('Ariel', 24, "normal"))
    # my_label.pack()
    # my_label.place(x=100, y=200)
    my_label.grid(column=0, row=0)

    my_label["text"] = "New text"
    my_label.config(text="Third Text")

    # Button
    button = Button(text="Click Me", command=button_clicked)
    # button.pack()
    button.grid(column=0, row=1)

    button2 = Button(text="Don't Click Me", command=button_clicked)
    # button.pack()
    button2.grid(column=1, row=1)

    # Textbox/Entry
    textbox = Entry(width=10)
    # textbox.pack()
    textbox.grid(column=0, row=2)

    window.mainloop()
