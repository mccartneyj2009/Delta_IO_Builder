import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
import odbcConn as Delta


def create_points_popup(master_frame):
    valid_source = Delta.verify_dsn_source()
    if valid_source:
        proceed = messagebox.askyesnocancel("Proceed", "Valid Source available.\nPlease verify that the proper "
                                                       "'Site' is "
                                                       "setup in the ODBC Data Source Administrator (32-bit).\n"
                                                       "Failure to do so could cause unwanted results.")
        if proceed:
            global dev_id
            dev_id = simpledialog.askinteger("BACnet Address", "Enter BACnet Address")
            if dev_id is not None:
                messagebox.showinfo("BACnet Address", f"BACnet Address set to {dev_id}.")
                Delta.create_points(dev_id, master_frame)

            else:
                messagebox.showerror("Invalid BACnet Address.", "The BACnet address given is not valid.")
        else:
            messagebox.showinfo("Stopped", "Points creation stopped.")
    elif not valid_source:
        messagebox.showerror("Invalid Source", "Please Verify ODBC driver.")


def view_points_popup():
    dev_id = simpledialog.askinteger("BACnet Address", "Enter BACnet Address")
    if dev_id is None:
        messagebox.showinfo("Stopped", "Action Stopped.")
    elif dev_id > 0:
        Delta.view_controller_points(dev_id)
    else:
        messagebox.showerror("Invalid BACnet Address.", "The BACnet address given is not valid.")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('750x500')
    root.title("Database I/O Builder")
    root.rowconfigure(0, minsize=450, weight=0)
    root.columnconfigure(0, weight=1)
    root.grid_propagate(False)
    root.pack_propagate(False)

    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    scroll_bar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    scroll_bar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=scroll_bar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    working_frame = Frame(my_canvas, bg='green')
    working_frame

    my_canvas.create_window((0, 0), window=working_frame, anchor="nw")

    new_button = Button(root, text='Create Points', command=lambda: create_points_popup(working_frame))
    new_button.grid(sticky='sw', padx=10, pady=10)


    # # buttons
    # create_points_btn = tk.Button(root, text="Create Points",
    #                               command=lambda: create_points_popup())
    # create_points_btn.pack(side="left", padx=10)
    #
    # view_controller_points_btn = tk.Button(root, text="View Controller Points",
    #                                        command=lambda: view_points_popup())
    # view_controller_points_btn.pack(side="left", padx=10)
    #
    # open_dsn_btn = tk.Button(root, text="Open DSN Config",
    #                          command=lambda: Delta.open_driver())
    # open_dsn_btn.pack(side="left", padx=10)
    #
    # close_btn = tk.Button(root, text="Close",
    #                       command=lambda: root.destroy())
    # close_btn.pack(side="left", padx=10)


    root.mainloop()
