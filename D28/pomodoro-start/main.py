from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
canvas.create_text(100,130,font=(FONT_NAME,35,"bold"),text="00:00",fill="white")
canvas.grid(column=1,row=1)

label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,20,"bold"),bg=YELLOW)
label.grid(column=1,row=0)

start_button=Button(text="Start",highlightthickness=0)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0)
reset_button.grid(column=2,row=2)

check_mark=Label(text="✔", fg=GREEN,font=(FONT_NAME,16,"bold"),bg=YELLOW)
check_mark.grid(column=1,row=3)
window.mainloop()

