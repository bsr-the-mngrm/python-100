from tkinter import *


def calculate():
    kilometer_label2["text"] = round(int(miles_entry.get())*1.6, 2)


if __name__ == '__main__':
    window = Tk()

    window.title("Mile to Km Converter")
    # set padding:
    window.config(padx=20, pady=20)

    # Textbox/Entry
    miles_entry = Entry(width=10)
    miles_entry.grid(column=1, row=0)

    # Miles Label
    miles_label = Label(text="Miles", font=('Ariel', 12, "normal"))
    miles_label.grid(column=2, row=0)

    # Kilometer Label #1
    kilometer_label1 = Label(text="is equal to", font=('Ariel', 12, "normal"))
    kilometer_label1.grid(column=0, row=1)

    # Kilometer Label #2
    kilometer_label2 = Label(text="0", font=('Ariel', 12, "normal"))
    kilometer_label2.grid(column=1, row=1)

    # Kilometer Label #3
    kilometer_label3 = Label(text="Km", font=('Ariel', 12, "normal"))
    kilometer_label3.grid(column=2, row=1)

    # Button
    calculate_button = Button(text="Calculate", command=calculate)
    calculate_button.grid(column=1, row=2)

    window.mainloop()
