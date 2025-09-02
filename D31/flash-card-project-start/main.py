from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# create a random French word
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records") # change format into[{french:xx,english:xx}]
current_english_word=""

def next_card():
    random_word = random.choice(to_learn)
    french_word = random_word["French"]
    global current_english_word, timer
    current_english_word=random_word["English"]
    canvas.itemconfig(card_word, text=french_word,fill="black")
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_image,image=front_card)

    window.after_cancel(timer)
    timer = window.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_image,image=back_card)
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_english_word,fill="white")

# create ui
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

timer=window.after(3000, flip_card)

canvas=Canvas(width=800,height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)
front_card=PhotoImage(file="images/card_front.png")
back_card=PhotoImage(file="images/card_back.png")
card_image =canvas.create_image(400, 263, image=front_card)


card_title=canvas.create_text(400, 150, font=(FONT_NAME, 40, "italic"), text="")
card_word=canvas.create_text(400, 263, font=(FONT_NAME, 60, "bold"), text="")

wrong_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(column=0,row=1)

right_image=PhotoImage(file="images/right.png")
right_button=Button(image=right_image,highlightthickness=0,command=next_card)
right_button.grid(column=1,row=1)

next_card()

window.mainloop()