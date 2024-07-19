import tkinter
MY_FONT =('Arial', 12, 'normal')

window = tkinter.Tk()

window.title('Mile to Km Converter')
window.config(padx=30, pady=30)

def mile_to_km_converter():
    result = my_var.get()*1.6
    display.config(text=result)

#labels...
lb1 = tkinter.Label(text='is equal to', font = MY_FONT)
lb2 = tkinter.Label(text='Miles', font = MY_FONT)
lb3 = tkinter.Label(text='Km', font = MY_FONT)
lb1.grid(column=0, row=1)
lb2.grid(column=2, row=0)
lb3.grid(column=2, row=1)

display = tkinter.Label(text='___')
display.grid(column=1, row=1)

#button
button = tkinter.Button(text='Calculate', command=mile_to_km_converter, font =MY_FONT)
button.grid(column=1, row=2)

#entry...
my_var = tkinter.IntVar()

inp = tkinter.Entry(text=my_var)
inp.focus()
inp.bind('<Return>', lambda event : mile_to_km_converter())
inp.grid(column =1, row =0)

window.mainloop()
