from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# create a random French word
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    origin_data=pandas.read_csv("data/french_words.csv")
    to_learn = origin_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records") # change format into[{french:xx,english:xx}]

current_dict={}
count=0
def next_card():
    random_word = random.choice(to_learn)
    french_word = random_word["French"]
    global current_dict, timer
    current_dict=random_word
    canvas.itemconfig(card_word, text=french_word,fill="black")
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_image,image=front_card)
    #clean previous timer
    window.after_cancel(timer)
    timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(card_image,image=back_card)
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_dict["English"],fill="white")

def is_known():
    to_learn.remove(current_dict)
    to_learn_data=pandas.DataFrame(to_learn)
    to_learn_data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

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
unknown_button=Button(image=wrong_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

right_image=PhotoImage(file="images/right.png")
known_button=Button(image=right_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

next_card()

window.mainloop()