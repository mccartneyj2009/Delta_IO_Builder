import tkinter as tk
import odbcConn as Delta
import scrollfrm
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox


def create_points_popup(master_frame, site_id):
    valid_source = Delta.verify_dsn_source()
    if valid_source:
        proceed = messagebox.askyesnocancel("Proceed", "Valid Source available.\nPlease verify that the proper "
                                                       "'Site' is set.\nFailure to do so could cause unwanted results.")
        if proceed:
            global dev_id
            dev_id = simpledialog.askinteger("BACnet Address", "Enter BACnet Address")
            if dev_id is not None:
                messagebox.showinfo("BACnet Address", f"BACnet Address set to {dev_id}.")
                Delta.create_points(dev_id, master_frame, site_id)
            else:
                messagebox.showerror("Invalid BACnet Address.", "The BACnet address given is not valid.")
        else:
            messagebox.showinfo("Stopped", "Points creation stopped.")
    elif not valid_source:
        messagebox.showerror("Invalid Source", "Please Verify ODBC driver.")


def view_points_popup(master_frame, site_id):
    dev_id = simpledialog.askinteger("BACnet Address", "Enter BACnet Address")
    if dev_id is None:
        messagebox.showinfo("Stopped", "Action Stopped.")
    elif dev_id > 0:
        Delta.view_controller_points(dev_id, master_frame, site_id)
    else:
        messagebox.showerror("Invalid BACnet Address.", "The BACnet address given is not valid.")


if __name__ == "__main__":
    # Main root
    root = tk.Tk()
    root.geometry('600x350')
    root.title("Database I/O Builder")
    root.rowconfigure(0, minsize=450, weight=0)
    root.columnconfigure(0, weight=1)
    root.grid_propagate(False)
    root.pack_propagate(False)

    # Holding frames
    parent_frame = Frame(root, bg='white')
    parent_frame.pack(fill=BOTH, expand=TRUE)
    button_frame = Frame(root)
    button_frame.pack(side=BOTTOM, fill=BOTH)
    drop_down_frame = Frame(parent_frame)
    drop_down_frame.pack(side=RIGHT, fill=Y)
    style = ttk.Style()
    style.configure('TFrame', background='white')

    # Frame that the SQL labels get added to
    frame = scrollfrm.ScrollableFrame(parent_frame)

    # Drop Down Menus
    sites_list = Delta.query_for_sites()
    sites_menu_lbl = Label(drop_down_frame, text="Select Site:")
    sites_menu = ttk.Combobox(drop_down_frame, values=sites_list)
    sites_menu_lbl.grid(row=0)
    sites_menu.grid(row=1, padx=10)
    system_type_list = ["AHU", "Chilled Water System", "Hot Water System"]
    system_type_lbl = Label(drop_down_frame, text="System Type:")
    systems_menu = ttk.Combobox(drop_down_frame, values=system_type_list)
    system_type_lbl.grid(row=3)
    systems_menu.grid(row=4, padx=10)

    # Buttons
    create_points_btn = Button(button_frame, text='Create Points',
                               command=lambda: create_points_popup(frame.scrollable_frame, sites_menu.get()))
    create_points_btn.pack(side=LEFT, padx=10, pady=10)

    view_controller_points_btn = tk.Button(button_frame, text="View Controller Points",
                                           command=lambda: view_points_popup(frame.scrollable_frame, sites_menu.get()))
    view_controller_points_btn.pack(side=LEFT, padx=10, pady=10)

    open_dsn_btn = Button(button_frame, text="Open DSN Config", command=lambda: Delta.open_driver())
    open_dsn_btn.pack(side=LEFT, padx=10, pady=10)

    close_btn = Button(button_frame, text="Close", command=lambda: root.destroy())
    close_btn.pack(side=RIGHT, padx=10, pady=10)

    frame.pack(fill=BOTH, expand=TRUE)

    root.mainloop()
