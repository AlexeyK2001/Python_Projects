from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "lightgreen"


data = pd.read_csv("data/french_words.csv")
dict_data = data.to_dict(orient="records")
current_card = {}


# __________________________functions________________________________________________________________
def new_french_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(dict_data)
    new_french_word = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=new_french_word, fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


def remove_the_word_from_list():
    global df_data, dict_data
    try:
        temp = open("words_to_learn.csv", "r")
        temp.close()
        data = pd.read_csv("words_to_learn.csv")
        dict_data = data.to_dict(orient="records")

        dict_data.remove(current_card)
        df_data = pd.DataFrame(dict_data)
        df_data.to_csv("data/words_to_learn.csv", index=False)
        new_french_word()
    except FileNotFoundError:

        dict_data.remove(current_card)
        df_data = pd.DataFrame(dict_data)
        df_data.to_csv("data/words_to_learn.csv", index=False)
        new_french_word()


def flip_card():
    new_eng_word = current_card["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=new_eng_word, fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)


# __________________________________________________________________________________________


# ___________________________Window & canvas, buttons settings__________________________________________________________
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(
    image=cross_image, highlightthickness=0, command=new_french_word
)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(
    image=check_image, highlightthickness=0, command=remove_the_word_from_list
)
known_button.grid(row=1, column=1)


new_french_word()

window.mainloop()
