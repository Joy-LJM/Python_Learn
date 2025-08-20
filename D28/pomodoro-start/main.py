from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer=None
marks = ""
# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    reps =0
    global marks
    marks = ""
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text="")
    # stop timer
    window.after_cancel(timer)
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    reps += 1
    if  reps % 8 ==0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif reps % 2 == 0 :
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    if count >0:
        min= math.floor(count/60)
        sec=count%60
        if sec<10:
            sec=f"0{sec}" #dynamic typing: int->str

        canvas.itemconfig(timer_text,text=f"{min}:{sec}")
        global timer
        timer=window.after(1000, count_down, count - 1)
    else:
        start_timer()
        # add checkmark every 2 reps
        work_sections=math.floor(reps/2)
        global marks
        for _ in range(work_sections):
            marks+="✔"
        check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)
tomato=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato)
timer_text=canvas.create_text(100,130,font=(FONT_NAME,35,"bold"),text="00:00",fill="white")
canvas.grid(column=1,row=1)

timer_label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,20,"bold"),bg=YELLOW)
timer_label.grid(column=1,row=0)

start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_mark=Label(fg=GREEN,font=(FONT_NAME,16,"bold"),bg=YELLOW)
check_mark.grid(column=1,row=3)

window.mainloop()

