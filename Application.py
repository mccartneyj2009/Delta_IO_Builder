import tkinter as tk
from tkinter import *
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
    root.rowconfigure(0, minsize=90, weight=0)
    root.columnconfigure(0, weight=1)
    readout_frame = Frame(root, bg='green')
    readout_frame.grid(row=0, column=0, sticky='nsew')
    new_button = Button(root, text='Create Points', command=lambda: create_points_popup(readout_frame))
    new_button.grid()


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
