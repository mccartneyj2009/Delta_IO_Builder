from tkinter import *

root = Tk()

topframe = Frame(root, bg='red')
midframe = Frame(root, bg='blue')
bottomframe = Frame(root, bg='yellow')

root.rowconfigure([0,2], minsize=90)    # Set min size for top and bottom
root.rowconfigure(1, weight=1)          # Row 1 should adjust to window size
root.columnconfigure(0, weight=1)       # Column 0 should adjust to window size
topframe.grid(row=0, column=0, sticky='nsew')   # sticky='nsew' => let frame
midframe.grid(row=1, column=0, sticky='nsew')   # fill available space
bottomframe.grid(row=2, column=0, sticky='nsew')

toplabel = Label(topframe, bg='red', text='Must be non resizable unless window cannot fit it \n (Contains buttons)',height=10)
midlabel = Label(midframe, bg='blue', text='Must be resizable \n (Contains a graph)',height=10)
bottomlabel = Label(bottomframe, bg='yellow', text='Must be non resizable unless window cannot fit it \n (Contains simulation results)',height=10)

toplabel.pack(fill=X,expand=TRUE)
midlabel.pack(fill=X,expand=TRUE)
bottomlabel.pack(fill=X,expand=TRUE)

root.mainloop()