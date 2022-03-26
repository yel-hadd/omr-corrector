from tkinter import *
from tkinter import ttk


def btn_clicked():
    print('HI')

class Signup(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.loadcaptcha()
        self.canvas = Canvas(
            bg="#ffffff",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.canvas.create_text(
            405.5, 96.5,
            text="Inscription",
            fill="#000000",
            font=("Kanit Regular", int(29.148176193237305)))

        self.img0 = PhotoImage(file=f"./src/signup/img0.png")
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

        self.img1 = PhotoImage(file=f"./src/signup/img1.png")
        b1 = Button(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        b1.place(
            x=518, y=37,
            width=99,
            height=24)

        self.img2 = PhotoImage(file=f"./src/signup/img2.png")
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

        self.img3 = PhotoImage(file=f"./src/signup/img3.png")
        b3 = Button(
            image=self.img3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Login,None,None,None,None,None),
            relief="flat")

        b3.place(
            x=304, y=461,
            width=196,
            height=24)

        self.canvas.create_text(
            404.5, 139.0,
            text="Créez un compte pour continuer vers l'application",
            fill="#4b4a4a",
            font=("Lato Regular", int(14.574088096618652)))

        self.img4 = PhotoImage(file=f"./src/signup/img4.png")
        b4 = Button(
            image=self.img4,
            borderwidth=0,
            highlightthickness=0,
            command=self.signup_btn,
            relief="flat")

        b4.place(
            x=323, y=419,
            width=158,
            height=39)

        self.entry0_img = PhotoImage(file=f"./src/signup/img_textBox0.png")
        entry0_bg = self.canvas.create_image(
            398.0, 203.5,
            image=self.entry0_img)

        self.entry0 = Entry(
            bd=0,
            bg="#eeeeee",
            font=("Calibri 14"),
            highlightthickness=0)

        self.entry0.place(
            x=285.89360427856445, y=188,
            width=224.2127914428711,
            height=29)

        self.entry1_img = PhotoImage(file=f"./src/signup/img_textBox1.png")
        entry1_bg = self.canvas.create_image(
            399.0, 264.5,
            image=self.entry1_img)

        self.entry1 = Entry(
            bd=0,
            bg="#eeeeee",
            show='•',
            font="Calibri 14",
            highlightthickness=0)

        self.entry1.place(
            x=286.89360427856445, y=249,
            width=224.2127914428711,
            height=29)

        self.entry2_img = PhotoImage(file=f"./src/signup/img_textBox2.png")
        entry2_bg = self.canvas.create_image(
            400.0, 325.5,
            image=self.entry2_img)

        self.entry2 = Entry(
            bd=0,
            bg="#eeeeee",
            show='•',
            font="Calibri 14",
            highlightthickness=0)

        self.entry2.place(
            x=287.89360427856445, y=310,
            width=224.2127914428711,
            height=29)

        self.entry3_img = PhotoImage(file=f"./src/signup/img_textBox3.png")
        entry3_bg = self.canvas.create_image(
            401.0, 386.5,
            image=self.entry3_img)

        self.entry3 = Entry(
            bd=0,
            bg="#eeeeee",
            font="Calibri 14",
            highlightthickness=0)

        self.entry3.place(
            x=288.89360427856445, y=371,
            width=224.2127914428711,
            height=29)

        self.canvas.create_text(
            306.0, 173.5,
            text="Email:",
            fill="#000000",
            font=("Kanit Light", int(13.924510955810547)))

        self.canvas.create_text(
            323.0, 232.5,
            text="Mot de passe:",
            fill="#000000",
            font=("Kanit Light", int(13.924510955810547)))

        self.canvas.create_text(
            340.0, 295.5,
            text="Re-type password:",
            fill="#000000",
            font=("Kanit Light", int(13.924510955810547)))

        self.cbox = self.canvas.create_text(
            309.0, 356.5,
            text=question,
            fill="#000000",
            font=("Kanit Light", int(13.924510955810547)))

        self.nbox = self.canvas.create_text(
            440, 355,
            text='',
            fill="#ff0000",
            font=("Kanit Light", 12))

    def loadcaptcha(self):
        global question, answer
        question, answer = captcha.gencaptcha()
        answer = int(answer)
        return question, answer

    def s_check(self):
        inp = self.entry3.get()
        if inp.isdigit():
            inp = int(inp)
        if inp == answer:
            return 1
        else:
            return 0

    def signup_btn(self):
        cp = self.s_check()
        if cp == 0:
            self.canvas.itemconfigure(self.nbox, text='Invalid Captcha', fill='#FF0000')
            self.loadcaptcha()
            self.canvas.itemconfigure(self.cbox, text=question)

        elif self.entry1.get() != self.entry2.get():
            self.canvas.itemconfigure(self.nbox, text="Passwords don't match", fill='#FF0000')
            self.loadcaptcha()
            self.canvas.itemconfigure(self.cbox, text=question)

        elif cp == 1:
            str = auth.signup(self.entry0.get(), self.entry1.get())
            if str == 0:
                self.canvas.itemconfigure(self.nbox, text="Invalid Email Address", fill='#FF0000')
                self.loadcaptcha()
                self.canvas.itemconfigure(self.cbox, text=question)
            elif str == 1:
                self.canvas.itemconfigure(self.nbox, text="You have signed up successfully!", fill='#008000')
            elif str == 2:
                self.canvas.itemconfigure(self.nbox, text="Email address already exists", fill='#FF0000')
                self.loadcaptcha()
                self.canvas.itemconfigure(self.cbox, text=question)

import auth
import captcha
from welcome import Welcome
from login import Login