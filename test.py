import tkinter as tk
from tkinter import *


class DialogueCreation(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)




if __name__ == '__main__':
    root = tk.Tk()
    DialogueCreation(root)
    root.title("Editor")
    root.mainloop()