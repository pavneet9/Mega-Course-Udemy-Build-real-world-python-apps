"""
A program to stores book information (title, author, year, ISBN) .
The user can

view all entries
update entries
delete entries
add entries

"""

from Tkinter import *
import backend

window = Tk()

def get_selected_row(event):
    global selectedtuple
    index = list1.curselection()[0]
    selectedtuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selectedtuple[1])

    e2.delete(0, END)
    e2.insert(END, selectedtuple[2])

    e3.delete(0, END)
    e3.insert(END, selectedtuple[3])

    e4.delete(0, END)
    e4.insert(END, selectedtuple[4])

def viewcommand():
    list1.delete(0, END)
    rows = backend.viewall()
    for row in rows:
        list1.insert(END, row)

def searchcommand():
    list1.delete(0, END)
    rows = backend.search(title.get(), Author.get(), Year.get(), isbn.get())
    for row in rows:
        list1.insert(END, row)

def addcommand():
    list1.delete(0, END)
    backend.insert(title.get(), Author.get(), Year.get(), isbn.get())

def updateselected():
    print selectedtuple[0],title.get(), Author.get(), Year.get(), isbn.get()
    backend.update(selectedtuple[0],title.get(), Author.get(), Year.get(), isbn.get())

def deleteselected():
    backend.delete(selectedtuple[0])


l1 = Label(window, text="Title")
l1.grid(row=0, column=0 )

l2 = Label(window, text="Author")
l2.grid(row=0, column=2 )

l3 = Label(window, text="Year")
l3.grid(row=1, column=0 )

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2 )

title = StringVar()
e1 = Entry(window, textvariable= title)
e1.grid(row=0, column=1 )

Author = StringVar()
e2 = Entry(window, textvariable= Author)
e2.grid(row=0, column=3 )

Year = StringVar()
e3 = Entry(window, textvariable= Year)
e3.grid(row=1, column=1 )

isbn = StringVar()
e4 = Entry(window, textvariable= isbn)
e4.grid(row=1, column=3 )

list1 = Listbox(window, height = 6 , width = 35)
list1.grid(row=2, column=0, rowspan = 6 , columnspan = 2)

list1.bind('<<ListboxSelect>>', get_selected_row)

p1 = Scrollbar(window)
p1.grid(row=2, column=2, rowspan= 6)

list1.configure(yscrollcommand = p1.set)
p1.configure(command = list1.yview)

b1 = Button(window, text="View All" , width=12, command=viewcommand)
b1.grid(row=2 , column= 3)

b2 = Button(window, text="Search Entries" , width=12, command=searchcommand)
b2.grid(row=3 , column= 3)

b3 = Button(window, text="Add Entries" , width=12, command=addcommand)
b3.grid(row=4 , column= 3)

b4 = Button(window, text="Update Selected" , width=12, command=updateselected)
b4.grid(row=5 , column= 3)

b5 = Button(window, text="Delete Selected" , width=12, command=deleteselected)
b5.grid(row=6 , column= 3)


window.mainloop()
