"""
Create a GUI to convert user input of ounce into gram with tkinker
"""

from tkinter import *

window = Tk()
window.title("Ounce to Gram Converter")
#window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Input
input = Entry(width=10)
input.grid(column=1, row=1)
input.insert(END, string="0")
print(input.get())

#Label
ounces = Label(text="Ounces", font=("Arial", 10))
ounces.grid(column=2, row=1)
#my_label.config(padx=50, pady=50)

equal = Label(text="is equal to", font=("Arial", 10))
equal.grid(column=0, row=2)

result = Label(text="0", font=("Arial", 10))
result.grid(column=1, row=2)

gram = Label(text="Gram", font=("Arial", 10))
gram.grid(column=2, row=2)

# Button
def button_clicked():
    ounce = float(input.get())
    gram = round(ounce*28.3495231)
    result.config(text=f"{gram}")

button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=3)
