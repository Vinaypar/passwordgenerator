from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_num = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_num
    # print(type(password_list))
    shuffle(password_list)

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_web = website_entry.get()
    new_web = new_web.lower()
    new_user = user_entry.get()
    new_pass = password_entry.get()

    new_data = {
        new_web: {
            "email": new_user,
            "password": new_pass,
        }
    }
    #print(new_data)
    if len(new_web) == 0 or len(new_user) == 0 or len(new_pass) == 0:
        messagebox.showinfo(title="Oops", message="You left some fild empty.")
    else:
        try:
            with open("data.json", "r") as data_file:
                #  Reading old data
                data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def search():
    website = website_entry.get()
    website = website.lower()
    try:
        with open("data.json", "r") as data_file:
            new_dict = json.load(data_file)
            # print(new_dict)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data FileFound")
    else:
        if website in new_dict:
            messagebox.showinfo(title=website.title(), message=f"Email: {new_dict[website]['email']}"
                                                               f"\nPassword: {new_dict[website]['password']}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

user_label = Label(text="Email/Username:")
user_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# Entry
website_entry = Entry(width=33)
website_entry.grid(column=1, row=1)
website_entry.focus()

user_entry = Entry(width=53)
user_entry.grid(column=1, row=2, columnspan=2)
user_entry.insert(0, "vinay@gmail.com")

password_entry = Entry(width=34)
password_entry.grid(column=1, row=3)

# Button
generate_button = Button(text="Generate Password", width=15, command=generate_password)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)

window.mainloop()
