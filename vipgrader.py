import tkinter as tk
from tkinter import ttk
from generate import Generate
from correct import Correct
from welcome import Welcome
from home import Home
from signup import Signup
from forgot_pass import Forgot_password
from login import Login
from chapters import Chapters
from contact import Contact


try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwarness(1)
except:
    pass

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('VIP GRADER')
        self.geometry('800x500')
        self.frames = {}
        container = ttk.Frame(self)
        container.pack()
        self.show_frame(Login,None,None,None,None,None)

    def show_frame(self, container, a, b, c, d, e):
        if container == Welcome:
            Welcome(self).pack()
        elif container == Home:
            Home(self).pack()
        elif container == Login:
            Login(self).pack()
        elif container == Signup:
            Signup(self).pack()
        elif container == Forgot_password:
            Forgot_password(self).pack()
        elif container == Generate:
            Generate(self).pack()
        elif container == Correct:
            Correct(self).pack()
        elif container == Contact:
            Contact(self).pack()
        elif container == Chapters:
            Chapters(self, a, b, c, d, e).pack()

def btn_clicked():
    print('HI')

root = Window()
root.iconbitmap("./app.ico")
root.resizable(False, False)
root.mainloop()
