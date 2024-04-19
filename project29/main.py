from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


def password_generation():

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for i in range(nr_letters)]
    password_list += [random.choice(numbers) for i in range(nr_numbers)]
    password_list += [random.choice(symbols) for i in range(nr_symbols)]

    random.shuffle(password_list)

    gen_password = "".join(password_list)
    password_clear()
    password_entry.insert(0, gen_password)
    pyperclip.copy(gen_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    global password, email
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(
            title="Empty input observed",
            message="There are empty elements!\n Please fill all lines.",
        )
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            clear()


# ---------------------------- CLEAR------------------------------- #
def clear():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


def password_clear():
    password_entry.delete(0, END)


# ---------------------------- Website search------------------------------- #
def website_search():
    searched_website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            # Reading old data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(
            title="No data file found",
            message="There is no file with passwords for now.",
        )
    else:
        try:
            with open("data.json", "r") as file:
                # Reading old data
                data = json.load(file)
            messagebox.showinfo(
                title=f"{searched_website} credentials:",
                message=f"Password: {data[searched_website]['password']},\nEmail: {data[searched_website]['email']}",
            )
        except KeyError:
            messagebox.showinfo(
                title="Absent website",
                message="No details for the website exist",
            )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

window.config(pady=40, padx=40)

# MyPass lock photo
canvas = Canvas(width=200, height=200)
lock_photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_photo)
canvas.config(highlightthickness=0)
canvas.grid(row=0, column=1)

# Website description
website_desc = Label(text="Website:")
website_desc.grid(row=1, column=0)


# EMail/Username description
email_desc = Label(text="EMail/Username:")
email_desc.grid(row=2, column=0)

# Password description
password_desc = Label(text="Password:")
password_desc.grid(row=3, column=0)

# WEbsite entry
website_entry = Entry(bg="white", width=31)
website_entry.grid(row=1, column=1)

website_entry.focus()

# EMail/Username Entry
email_entry = Entry(bg="white", width=52)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "thomaslore1993@gmail.com")

# Password Entry
password_entry = Entry(bg="white", width=31)
password_entry.grid(row=3, column=1)

# Password button
password_button = Button(text="Generate Password", command=password_generation)
password_button.grid(row=3, column=2)

# Website search button
search_button = Button(text="Search", command=website_search, width=14)
search_button.grid(row=1, column=2)
# add button
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
