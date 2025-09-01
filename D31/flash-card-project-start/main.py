from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# create a random French word
data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records") # change format into[{french:xx,english:xx}]

def next_card():
    random_word = random.choice(to_learn)
    french_word = random_word["French"]
    canvas.itemconfig(card_word, text=french_word)
    canvas.itemconfig(card_title, text="French")

# create ui
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)
card=PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card)

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