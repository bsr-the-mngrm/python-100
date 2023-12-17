from tkinter import *

if __name__ == '__main__':
    window = Tk()

    window.title("Hello World w/ GUI")
    window.minsize(width=500, height=300)

    # Label
    my_label = Label(text="I am a Label!", font=('Ariel', 24, "normal"))
    my_label.pack(expand=True)

    window.mainloop()
