from tkinter import *
from tkinter import messagebox
from random import randint, choice,shuffle
import  pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
import random
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [ choice(letters) for _ in range(randint(8,10))]
    password_symbools = [ choice(symbols) for _ in range(randint(2,4))]
    password_number = [ choice(numbers) for _ in range(randint(2,4))]
    password_list = password_number+password_letters+password_symbools
    shuffle(password_list)
    password= "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_string():
    web_site = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(web_site) == 0 or len(email)==0 or len(password)==0:
        messagebox.showerror(title="empty field", message="please dont leave any empty field")

    else:
        string = f" {web_site} | {email} | {password}"
        is_ok = messagebox.askokcancel(title="save", message=f"data entered: \n{string}")

        if is_ok:
            with open("../password-manager-start/data.txt", "a") as f:
                f.write(f"{string}\n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Passaword Manager")
window.config(padx=50, pady=50)
image = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, highlightthickness=0)
canvas.create_image(100,100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/name:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry= Entry(width=50)
website_entry.grid(row=1,column=1, columnspan=2)
website_entry.focus()

email_entry= Entry(width=50)
email_entry.grid(row=2,column=1, columnspan=2)
email_entry.insert(index=END, string="hikmet_guler@email.com")

password_entry= Entry(width=32)
password_entry.grid(row=3,column=1)

generate_psw_button= Button(text="generate password", command=generate_password)
generate_psw_button.grid(row=3,column=2)

add_button = Button(text="add", width=43, command=add_string)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()