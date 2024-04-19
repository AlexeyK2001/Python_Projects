from tkinter import *


def button_clicked():
    my_label.config(text=input.get(), font=("Times", 18, "italic"))


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=40, pady=30)

# Label
my_label = Label(
    text="I am a label", font=("Arial", 24, "bold")
)  # Label was only created. The arguments can be chabged like in a dictionary: my_label["text"] = "New Text" or with config: my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=40, pady=40)
# pack() puts the object (label) on the window one after another
# place() puts the object in a specific location (x,y)
# grid() puts the object in a grid format like a.place(column=1, row=2) and so on
# grid() and pack() CAN NOT be in the same program
# Button
new_button = Button(text="I am a new button", command=button_clicked)
new_button.grid(column=2, row=0)
my_button = Button(text="My button", command=button_clicked)
my_button.grid(column=1, row=1)

# Entry
input = Entry(width=20)
input.grid(column=3, row=2)


window.mainloop()
