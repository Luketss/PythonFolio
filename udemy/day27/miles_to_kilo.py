from tkinter import *

def calculate():
    miles = open_label.get()
    km = float(miles) * 1.609344
    kilometer.config(text=km)

window = Tk()
window.title('Miles to Killometers')
window.config(padx=20, pady=20)

open_label = Entry(width=7)
open_label.grid(column=1, row=0)

my_label = Label(text='Miles')
my_label.grid(column=2, row=0)

is_equal_label = Label(text='is equal to')
is_equal_label.grid(column=0, row=1)

kilometer = Label(text='')
kilometer.grid(column=1, row=1)

button = Button(text ="Hello", command=calculate)
button.grid(column=1, row=2)

window.mainloop()