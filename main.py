from tkinter import *

window = Tk()
window.title("This is new window")
window.minsize(width=500, height=500)

my_label = Label(text="This is my label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.grid(row=0,column=0)


def button_clicked():
    my_label.config(text=entry.get())
entry = Entry(width=10)
entry.grid(row=1,column=1)
button_2 = Button(text="this is button 2")
button_2.grid(row=0, column=2)

button = Button(text="Click me", command=button_clicked)
button.grid(columnspan=2)



























window.mainloop()
