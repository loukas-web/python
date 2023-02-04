# from faulthandler import disable
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("Youtube Song Downloader")


# root.config(bg='lightgrey')

def clickme():
    myLabel3 = Label(root, text=myEntry1.get())
    myLabel3.grid(row=3, column=0, columnspan=2)
    print(myEntry1.get())


def select_directory():
    path = filedialog.askdirectory(initialdir='/home/loukas') + '/'
    myLabel4 = Label(root, text=path)
    myLabel4.grid(row=1, column=1, padx=5, pady=5)
    return path


# create a label widget and shoving it to the screen
myLabel1 = Label(root, text="Youtube URL")

myButton1 = Button(root, text="Select Output Folder", fg='blue', command=select_directory)

myEntry1 = Entry(root, width=50)
#myEntry2 = Entry(root, width=50)

myLabel1.grid(row=0, column=0, padx=5, pady=5)
myEntry1.grid(row=0, column=1, padx=5, pady=5)
myButton1.grid(row=1, column=0, padx=5, pady=5)

root.mainloop()
