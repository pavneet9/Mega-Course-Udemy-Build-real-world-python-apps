from Tkinter import *

window = Tk()

def km_to_miles():
    print el_value.get()
    miles = float(el_value.get())*1.6
    t1.insert(END, miles)
b1 = Button(window, text="execute" , command= km_to_miles)
b1.grid(row=2, column=3)

el_value = StringVar()
b1 = Entry(window, textvariable = el_value)
b1.grid(row=1, column=2)

t1 = Text(window,height=1, width=20)
t1.grid(row=1, column=1)

window.mainloop()
