import tkinter

def button_clicked():
    #print("I got clicked")
    new_text = input.get()
    my_label.config(text = new_text )


window = tkinter.Tk()
window.title('My First GUI Program')
window.minsize(width=500,height=300)
window.config(padx=100, pady=100)


#Label
my_label = tkinter.Label(text = "I am a Label", font = ('Arial', 24, 'italic'))
my_label.config(text='New Text')
my_label.pack()
#my_label.place(x=100, y=200)
my_label.grid(column =0, row =0)
my_label.config(padx=100, pady =100)




#Button
button = tkinter.Button(text = 'Click me', command = button_clicked)
#button.pack()
button.grid(column =1, row =1)

new_button = tkinter.Button(text='new button')
new_button.grid(column = 2, row =0)

#Entry..
input = tkinter.Entry(width = 20)
#input.pack()
input.grid(column =3, row = 3)




window.mainloop()
