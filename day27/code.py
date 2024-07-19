import tkinter as tk

window = tk.Tk()
window.config(padx=20, pady=20)

def show_data():
    print(f"First Name: {e1.get()} Last Name : {e2.get()} ")
    e1.delete(0,tk.END)
    e2.delete(0,tk.END)

tk.Label(text='First Name').grid(row=0)
tk.Label(text='Last Name').grid(row=1)

e1 = tk.Entry()
e2 = tk.Entry()

e1.grid(column=1,row=0)
e2.grid(column=1,row=1)

#Starting..entry..
e1.insert(10,'Example')
e2.insert(10,'kumar')

#Buttons..
btn1 = tk.Button(text='Quit', command=window.quit)
btn2 = tk.Button(text='Show', command= show_data)
btn1.grid(column=0, row=3)
btn2.grid(column=1, row=3)



window.mainloop()
