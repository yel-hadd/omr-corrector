from tkinter import ttk

class Welcome(ttk.Frame):
    def btn_clicked(self):
        print('Button Clicked')
    def __init__(self, container):
        super().__init__(container)
        self.canvas = Canvas(
            bg="#ffffff",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"./src/welcome/background.png")
        background = self.canvas.create_image(
            399.5, 250.0,
            image=self.background_img)

        self.img0 = PhotoImage(file=f"./src/welcome/img0.png")
        b0 = Button(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Signup,None,None,None,None,None),
            relief="flat")

        b0.place(
            x=239, y=430,
            width=137,
            height=34)

        self.img1 = PhotoImage(file=f"./src/welcome/img1.png")
        b1 = Button(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Login,None,None,None,None,None),
            relief="flat")

        b1.place(
            x=423, y=430,
            width=137,
            height=34)

        self.canvas.create_text(
            399.0, 389.5,
            text="BIENVENUE SUR VIP GRADER!",
            fill="#000000",
            font=("Lato SemiBold", 23))


from tkinter import *
from signup import Signup
from login import Login