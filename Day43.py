"""
CREATE A FLASH CARD APP USING MOST COMMON WORDS OF SPANISH 
List of words: https://github.com/hermitdave/FrequencyWords/tree/master/content/2018
In Google Sheet you can translate the words using GOOGLE TRANSLATE function
"""




from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original = pd.read_csv("data/common_spanish_words.csv")
    to_learn = original.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



# ---------------------------- FLIP CARDS ------------------------------- #
def flip_card():
    english_word = current_card["EN"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(canvas_image, image=card_back)

# ---------------------------- GENERATE RANDOM WORD ------------------------------- #

def generate_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)
    spanish_word = current_card["ES"]
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=spanish_word, fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)

# ---------------------------- REMOVE WORD------------------------------- #
def remove_word():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    print(len(data))
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("FLASH ME")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=526, width=800)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Courier", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Courier", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

generate_word()

# BUTTONS
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, borderwidth=0, command=remove_word)
right_button.grid(row=1, column=0)

wrong_img = PhotoImage(file="images/wrong.png")
right_button = Button(image=wrong_img, highlightthickness=0, borderwidth=0, command=generate_word)
right_button.grid(row=1, column=1)

window.mainloop()
