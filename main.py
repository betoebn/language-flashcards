from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    with open("./data/words_to_learn.csv") as data:
        database = pd.read_csv(data)
        dictionary = database.to_dict(orient="records")
except FileNotFoundError:
    with open("./data/french_words.csv") as data:
        database = pd.read_csv(data)
        dictionary = database.to_dict(orient="records")

current_card = {}


# ----------------------- Reading CSV File ------------------------------
def correct_answer():
    dictionary.remove(current_card)
    to_learn = pd.DataFrame.from_dict(dictionary)
    to_learn.to_csv("./data/words_to_learn.csv", index=False)
    generate_word()


# ----------------------- Reading CSV File ------------------------------
def generate_word():
    global current_card

    canvas.itemconfig(canvas_image, image=front_image)
    current_card = random.choice(dictionary)
    actual_card = current_card["French"]
    canvas.itemconfig(title, text="French")
    canvas.itemconfig(word, text=actual_card)
    window.after(3000, flip_card)


# ----------------------- Reading CSV File ------------------------------
def flip_card():
    canvas.itemconfig(canvas_image, image=back_image)
    canvas.itemconfig(title, text="English")
    english_word = current_card["English"]
    canvas.itemconfig(word, text=english_word)


# -------------------------- GUI WINDOW ----------------------------------


window = Tk()
window.title("French Flash Cards")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=20)

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.grid(column=0, row=0, columnspan=2)

check_button_image = PhotoImage(file="./images/right.png")
check_button = Button(image=check_button_image, highlightthickness=0, command=correct_answer)
check_button.grid(column=0, row=1)

wrong_button_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_image, highlightthickness=0, command=generate_word)
wrong_button.grid(column=1, row=1)

title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), tag="french")

generate_word()

window.mainloop()
