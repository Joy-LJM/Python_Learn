from tkinter import *

window=Tk()
window.title("Miles To Km Converter")
window.minsize(width=500,height=400)
window.config(padx=100,pady=100)

#Entry
mile_input=Entry(width=7)
mile_input.grid(row=0,column=1)

miles_label=Label(text="Miles")
miles_label.grid(row=0,column=2)

equal_label=Label(text="is equal to")
equal_label.grid(row=1,column=0)

#Entry
km_input=Label()
km_input.grid(row=1,column=1)

km_label=Label(text="Km")
km_label.grid(row=1,column=2)

def calculate_km():
    miles=float(mile_input.get())
    converted_miles=round(miles* 1.609)
    km_input.config(text=f"{converted_miles}")

button=Button(text="Calculate")
button.grid(row=2,column=1)
button.config(command=calculate_km)

window.mainloop()