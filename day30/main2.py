from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters= random.randint(8,10)
    nr_symbols = random.randint(2,4)
    nr_numbers = random.randint(2,4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = ''.join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website)==0 or len(password) ==0:
        messagebox.showinfo(title='Oops', message = "Please make sure you haven't left any fields empty ")
        return 
    
    is_okay = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password}\nIs it ok to save?")
    if is_okay:
        with open('data.txt', mode='a') as file:
            record = f"{website} | {email} | {
            password} \n"
            file.write(record)
        website_entry.delete(0,END)
        password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#labels..
website = Label(text='Website:')
email = Label(text='Email/Username:')
password = Label(text='Password:')
website.grid(column=0, row=1)
email.grid(column=0, row=2)
password.grid(column=0, row=3)

#Entries..
website_entry = Entry(width=35)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'aakashkumarpy@gmail.com')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons..
generate = Button(text='Generate password', command=generate_password)
generate.grid(column=2, row =3)

add_button = Button(text='Add', width=35, command=save_password)
add_button.grid(row=4, column=1, columnspan =2)







window.mainloop()
