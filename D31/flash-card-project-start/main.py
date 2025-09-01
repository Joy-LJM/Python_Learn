from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas=Canvas(width=800,height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(column=0,row=0,columnspan=2)
card=PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card)

title_text=canvas.create_text(400,150,font=(FONT_NAME,40,"italic"),text="French")
word_text=canvas.create_text(400,263,font=(FONT_NAME,60,"bold"),text="English")


wrong_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0)
wrong_button.grid(column=0,row=1)

right_image=PhotoImage(file="images/right.png")
right_button=Button(image=right_image,highlightthickness=0)
right_button.grid(column=1,row=1)

window.mainloop()