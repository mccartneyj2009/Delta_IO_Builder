import tkinter as tk
import odbcConn as Delta
import scrollfrm
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox


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
    root.geometry('500x350')
    root.title("Database I/O Builder")
    root.rowconfigure(0, minsize=450, weight=0)
    root.columnconfigure(0, weight=1)
    root.grid_propagate(False)
    root.pack_propagate(False)
    parent_frame = Frame(root, bg='white')
    parent_frame.pack(fill=BOTH, expand=TRUE)
    button_frame = Frame(root)
    button_frame.pack(side=BOTTOM, fill=BOTH)
    style = ttk.Style()
    style.configure('TFrame', background='white')

    frame = scrollfrm.ScrollableFrame(parent_frame)

    create_points_btn = Button(button_frame, text='Create Points', command=lambda: create_points_popup(frame.scrollable_frame))
    create_points_btn.pack(side=LEFT, padx=10, pady=10)
    view_controller_points_btn = tk.Button(button_frame, text="View Controller Points", command=lambda: view_points_popup())
    view_controller_points_btn.pack(side=LEFT, padx=10, pady=10)
    open_dsn_btn = tk.Button(button_frame, text="Open DSN Config", command=lambda: Delta.open_driver())
    open_dsn_btn.pack(side=LEFT, padx=10, pady=10)
    close_btn = tk.Button(button_frame, text="Close", command=lambda: root.destroy())
    close_btn.pack(side=RIGHT, padx=10, pady=10)

    frame.pack(fill=BOTH, expand=TRUE)

    root.mainloop()
