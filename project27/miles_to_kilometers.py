from tkinter import *


def calc_button():
    miles_value = float(miles_input.get())
    calculated_value = round(miles_value * 1.609, 3)
    km_value.config(text=calculated_value)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=40, pady=30)


is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

miles_input = Entry()
miles_input.grid(column=1, row=0)


miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx=14)


km_value = Label(text="0")
km_value.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calc_button)
calculate_button.grid(column=1, row=2)


window.mainloop()
