# from faulthandler import disable
from tkinter import *

root = Tk()


def ClickMe():
    myLabel3 = Label(root, text=myEntry.get())
    myLabel3.grid(row=3)


# create a label widget and shoving it to the screen
myLabel1 = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Loukas")

myButton = Button(root, text="Click Me!", fg='blue', command=ClickMe)

myEntry = Entry(root, width=50)

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=0, column=1)
myButton.grid(row=1, column=0)
myEntry.grid(row=1, column=1)

root.mainloop()
