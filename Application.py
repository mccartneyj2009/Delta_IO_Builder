import tkinter as tk
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import odbcConn as delta


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initialUI()

    def initialUI(self):
        # frames
        console_window = tk.Canvas(root,bg='white')
        console_window.pack(fill=BOTH,expand=TRUE, padx=5)
        # self.item_canvas = tk.Canvas(root, width=500, height=500, xscrollcommand=self.xbar.set,
        #                              yscrollcommand=self.ybar.set)
        # self.item_canvas.pack(side=LEFT, expand=FALSE, fill=None)
        # self.item_canvas.configure(background='black')
        #
        # self.xbar = tk.Scrollbar(self.item_canvas, orient=HORIZONTAL)
        # self.xbar.pack(side=BOTTOM, fill=X)
        #
        # self.ybar = tk.Scrollbar(self.item_canvas)
        # self.ybar.pack(side=RIGHT, fill=Y)
        #
        #
        #

        button_frame1 = tk.Frame()
        button_frame1.pack(side="left", pady=10)
        button_frame2 = tk.Frame()
        button_frame2.pack(side="right", pady=10)

        # buttons
        self.buttons(button_frame1, "Create Points", lambda: self.create_points_popup(console_window))
        self.buttons(button_frame1, "View Controller Points", lambda: self.view_points_popup())
        self.buttons(button_frame1, "Open DSN Config", lambda: delta.open_driver())
        self.buttons(button_frame2, "Close", lambda: root.destroy())

    def buttons(self, btn_master, btn_text, btn_cmd):
        btn_ext_pad = 10
        return tk.Button(master=btn_master, text=btn_text, command=btn_cmd).pack(side="left", padx=10)

    def create_points_popup(self,master_frame):
        valid_source = delta.verify_dsn_source()
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
                    delta.create_points(dev_id,master_frame)
                else:
                    messagebox.showerror("Invalid BACnet Address.", "The BACnet address given is not valid.")
            else:
                messagebox.showinfo("Stopped", "Points creation stopped.")
        elif not valid_source:
            messagebox.showerror("Invalid Source", "Please Verify ODBC driver.")

    def view_points_popup(self):
        dev_id = simpledialog.askinteger("BACnet Address", "Enter BACnet Address")
        if dev_id is None:
            messagebox.showinfo("Stopped", "Action Stopped.")
        elif dev_id > 0:
            delta.view_controller_points(dev_id)
        else:
            messagebox.showerror("Invalid BACnet Address.", "The BACnet address given is not valid.")


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('750x500')
    root.title("Database I/O Builder")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
