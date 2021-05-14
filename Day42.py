"""
Create a local GUI password manager, which stores the password and username to respective website, and generate strong password
Missing image "logo.png"
100 Days of Code - Angela Ju Udemy Course
"""

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    password_number = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_number + password_symbol
    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"Your password is: {password}")
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username}\n"
                                                          f"Password: {password} \nIs it ok to save?")

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oh no", message="Please make sure you don't leave any box empty")
    else:
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")
                file.close()
                website_input.delete(0, END)
                #username_input.delete(0, END)
                password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.focus()

username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Input
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "hanh00hoang@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#Button
generate_button = Button(text="Generate Password", highlightthickness=0, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", highlightthickness=0, width=36, command=add_password)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
