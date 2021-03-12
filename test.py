# from tkinter import *
#
# root = Tk()
#
# topframe = Frame(root, bg='red')
# midframe = Frame(root, bg='blue')
# bottomframe = Frame(root, bg='yellow')
#
# root.rowconfigure([0,2], minsize=90)    # Set min size for top and bottom
# root.rowconfigure(1, weight=1)          # Row 1 should adjust to window size
# root.columnconfigure(0, weight=1)       # Column 0 should adjust to window size
# topframe.grid(row=0, column=0, sticky='nsew')   # sticky='nsew' => let frame
# midframe.grid(row=1, column=0, sticky='nsew')   # fill available space
# bottomframe.grid(row=2, column=0, sticky='nsew')
#
# toplabel = Label(topframe, bg='red', text='Must be non resizable unless window cannot fit it \n (Contains buttons)',height=10)
# midlabel = Label(midframe, bg='blue', text='Must be resizable \n (Contains a graph)',height=10)
# bottomlabel = Label(bottomframe, bg='yellow', text='Must be non resizable unless window cannot fit it \n (Contains simulation results)',height=10)
#
# toplabel.pack(fill=X,expand=TRUE)
# midlabel.pack(fill=X,expand=TRUE)
# bottomlabel.pack(fill=X,expand=TRUE)
#
# root.mainloop()

# from tkinter import *
# from tkinter import ttk
#
# root = Tk()
# root.title('Learn To Code at Codemy.com')
# root.geometry("500x400")
#
# # Create A Main Frame
# main_frame = Frame(root)
# main_frame.pack(fill=BOTH, expand=1)
#
# # Create A Canvas
# my_canvas = Canvas(main_frame)
# my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
#
# # Add A Scrollbar To The Canvas
# my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
# my_scrollbar.pack(side=RIGHT, fill=Y)
#
# # Configure The Canvas
# my_canvas.configure(yscrollcommand=my_scrollbar.set)
# my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))
#
# # Create ANOTHER Frame INSIDE the Canvas
# second_frame = Frame(my_canvas)
#
# # Add that New frame To a Window In The Canvas
# my_canvas.create_window((0,0), window=second_frame, anchor="nw")
#
# for thing in range(100):
# 	Button(second_frame, text=f'Button {thing} Yo!').grid(row=thing, column=0, pady=10, padx=10)
#
# my_label = Label(second_frame, text="It's Friday Yo!").grid(row=3, column=2)
#
#
# root.mainloop()