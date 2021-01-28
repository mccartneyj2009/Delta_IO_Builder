import tkinter as tk
import odbcConn as delta


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.initialUI()

    def initialUI(self):
        #frames
        label_frame_main = tk.LabelFrame(root,text="Console", height=300, bg="white")
        label_frame_main.pack(fill="both", expand="yes", padx=5)
        button_frame1 = tk.Frame()
        button_frame1.pack(side="left", pady=10)
        button_frame2 = tk.Frame()
        button_frame2.pack(side="right", pady=10)


        #buttons
        create_points_btn = self.buttons(button_frame1, "Create Points", lambda: delta.create_points())
        query_panel_btn = self.buttons(button_frame1, "View Controller Points", lambda: delta.view_controller_points())
        open_dsn_btn = self.buttons(button_frame1, "Open DSN Config", lambda: delta.open_driver())
        close_btn = self.buttons(button_frame2, "Close", lambda: root.destroy())

    def buttons(self, btn_master, btn_text, btn_cmd):
        btn_ext_pad = 10
        return tk.Button(master=btn_master, text=btn_text, command=btn_cmd).pack(side="left", padx=10)

    def dsn_popup(self):
        #new_window = tk.
        pass


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('750x500')
    root.title("Database I/O Builder")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()