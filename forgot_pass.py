from tkinter import *
from tkinter import ttk
import auth
from login import Login
from signup import Signup
from welcome import Welcome


def btn_clicked():
    print('HI')

class Forgot_password(ttk.Frame):
    def reset(self):
        a = auth.reset_password(self.entry0.get())
        if a == 0:
            self.canvas.itemconfigure(self.nbox, text='Invalid Email Address', fill='#FF0000')
        else:
            self.canvas.itemconfigure(self.nbox, text='If the the email address exists password reset link will be sent', fill='#0000CD')


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

        self.entry0_img = PhotoImage(file=f"./src/reset/img_textBox0.png")
        entry0_bg = self.canvas.create_image(
            399.0, 246.5,
            image=self.entry0_img)

        self.entry0 = Entry(
            bd=0,
            font='Calibri 20',
            bg="#eeeeee",
            highlightthickness=0)

        self.entry0.place(
            x=98.05547618865967, y=223,
            width=601.8890476226807,
            height=45)

        self.canvas.create_text(
            396.0, 141.5,
            text="Réinitialisez votre mot de passe",
            fill="#000000",
            font=("Kanit Regular", 31))

        self.img0 = PhotoImage(file=f"./src/reset/img0.png")
        b0 = Button(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Login,None,None,None,None,None),
            relief="flat")

        b0.place(
            x=631, y=35,
            width=101,
            height=27)

        self.img1 = PhotoImage(file=f"./src/reset/img1.png")
        b1 = Button(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Signup,None,None,None,None,None),
            relief="flat")

        b1.place(
            x=518, y=37,
            width=99,
            height=24)

        self.img2 = PhotoImage(file=f"./src/reset/img2.png")
        b2 = Button(
            image=self.img2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Welcome,None,None,None,None,None),
            relief="flat")

        b2.place(
            x=66, y=31,
            width=160,
            height=38)

        self.canvas.create_text(
            400.0, 181.0,
            text="Entrez l'adresse e-mail que vous avez utilisé pour vous inscrire",
            fill="#4b4a4a",
            font=("Lato Regular", 15))

        self.nbox = self.canvas.create_text(
            400.0, 355,
            text="",
            fill="#FF0000",
            font=("Lato Regular", 16))

        self.img3 = PhotoImage(file=f"./src/reset/img3.png")
        b3 = Button(
            image=self.img3,
            borderwidth=0,
            highlightthickness=0,
            command=self.reset,
            relief="flat")

        b3.place(
            x=320, y=291,
            width=158,
            height=39)

        self.img4 = PhotoImage(file=f"./src/reset/img4.png")
        b4 = Button(
            image=self.img4,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        b4.place(
            x=59, y=398,
            width=680,
            height=65)
