from tkinter import *

window=Tk()

window.title("My first GUI")
window.minsize(width=500,height=300)
window.config(padx=100,pady=100)
def click_button():
    print("I got clicked")
    val= input.get()
    label.config(text=val)

# Label
label=Label(text="I am a label",font=("Arial",20,"bold")) # font is a tuple
# label.pack(expand=True) # to display on screen
# different ways to change label
label["text"]='New label'
label.config(text='New label',padx=10,pady=10)
# label.pack(side="left")
# label.pack() # can't use pack() if using grid()
label.grid(column=0, row=0)

#Button
new_button=Button(text="New Button")
new_button.grid(column=2, row=0)
button=Button(text="click me",command=click_button)
# button.pack()
button.grid(column=1, row=1)

# Entry
input=Entry()
# input.pack()
input.grid(column=4, row=2)



window.mainloop() # keep the window on and listening user interaction
