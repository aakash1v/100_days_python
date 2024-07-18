import tkinter
MY_FONT =('Arial', 12, 'normal')

window = tkinter.Tk()

window.title('Mile to Km Converter')
window.config(padx=30, pady=30)

def mile_to_km_converter():
    result = mile_var.get()*1.6
    km_var.set(result)


#labels...
lb1 = tkinter.Label(text='is equal to', font = MY_FONT)
lb2 = tkinter.Label(text='Miles', font = MY_FONT)
lb3 = tkinter.Label(text='Km', font = MY_FONT)
lb1.grid(column=0, row=1)
lb2.grid(column=2, row=0)
lb3.grid(column=2, row=1)


#button
button = tkinter.Button(text='Calculate', command=mile_to_km_converter, font =MY_FONT)
button.grid(column=1, row=2)

#entry...
mile_var = tkinter.IntVar()
km_var = tkinter.IntVar()
inp1 = tkinter.Entry(text=mile_var)
inp2 = tkinter.Entry(text = km_var)
inp1.grid(column =1, row =0)
inp2.grid(column =1, row =1)

mile_var.set(0)
km_var.set(0)









window.mainloop()
