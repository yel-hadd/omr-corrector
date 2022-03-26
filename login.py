from tkinter import ttk
import auth
import captcha


def btn_clicked():
    print('HI')

class Login(ttk.Frame):
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

        self.entry0_img = PhotoImage(file=f"./src/login/img_textBox0.png")
        entry0_bg = self.canvas.create_image(
            404.0, 216.5,
            image=self.entry0_img)

        self.entry0 = Entry(
            bd=0,
            font='Lato 13',
            bg="#eeeeee",
            highlightthickness=0)

        self.entry0.place(
            x=263.17389965057373, y=197,
            width=281.65220069885254,
            height=37)

        self.entry1_img = PhotoImage(file=f"./src/login/img_textBox1.png")
        entry1_bg = self.canvas.create_image(
            406.0, 292.5,
            image=self.entry1_img)

        self.entry1 = Entry(
            bd=0,
            show='•',
            font='Lato 13',
            bg="#eeeeee",
            highlightthickness=0)

        self.entry1.place(
            x=265.17389965057373, y=273,
            width=281.65220069885254,
            height=37)

        self.entry2_img = PhotoImage(file=f"./src/login/img_textBox2.png")
        entry2_bg = self.canvas.create_image(
            407.0, 369.5,
            image=self.entry2_img)

        self.entry2 = Entry(
            bd=0,
            font='Lato 13',
            bg="#eeeeee",
            highlightthickness=0,
        )

        self.entry2.place(
            x=266.17389965057373, y=350,
            width=281.65220069885254,
            height=37)

        self.canvas.create_text(
            279.5, 177.5,
            text="Email:",
            fill="#000000",
            font=("Kanit Light", 17))

        self.canvas.create_text(
            320, 252.5,
            text="Mot de passe:",
            fill="#000000",
            font=("Kanit Light", 17))

        self.cbox = self.canvas.create_text(
            291.5, 331.5,
            text=question,
            fill="#000000",
            font=("Kanit Light", 17))

        self.nbox = self.canvas.create_text(
            420, 331.5,
            text='',
            fill="#ff0000",
            font=("Kanit Light", 12))

        self.canvas.create_text(
            404.5, 87.5,
            text="Connexion",
            fill="#000000",
            font=("Kanit Regular", 30))

        self.img0 = PhotoImage(file=f"./src/login/img0.png")
        b0 = Button(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Signup,None,None,None,None,None),
            relief="flat")

        b0.place(
            x=638, y=30,
            width=104,
            height=28)

        self.img1 = PhotoImage(file=f"./src/login/img1.png")
        b1 = Button(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        b1.place(
            x=522, y=31,
            width=101,
            height=25)

        self.img2 = PhotoImage(file=f"./src/login/img2.png")
        b2 = Button(
            image=self.img2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Welcome,None,None,None,None,None),
            relief="flat")

        b2.place(
            x=58, y=25,
            width=164,
            height=39)

        self.img3 = PhotoImage(file=f"./src/login/img3.png")
        b3 = Button(
            image=self.img3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Forgot_password,None,None,None,None,None),
            relief="flat")

        b3.place(
            x=302, y=449,
            width=201,
            height=24)

        self.canvas.create_text(
            404.5, 136.5,
            text="connectez-vous pour continuer vers l'application",
            fill="#4b4a4a",
            font=("Lato Regular", 17))

        self.img4 = PhotoImage(file=f"./src/login/img4.png")
        b4 = Button(
            image=self.img4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.login_btn(container),
            relief="flat")

        b4.place(
            x=322, y=407,
            width=162,
            height=41)

    def quitf(self):
        self.quit()

    def btn_clicked(self):
        print("Button Clicked")

    def loadcaptcha(self):
        global question, answer
        question, answer = captcha.gencaptcha()
        answer = int(answer)
        return question, answer

    def check(self):
        inp = self.entry2.get()
        if inp.isdigit():
            inp = int(inp)
        if inp == answer:
            return 1
        else:
            return 0

    def login_btn(self, container):
        cp = self.check()
        if cp == 0:
            self.canvas.itemconfigure(self.nbox, text='Invalid Captcha')
            self.loadcaptcha()
            self.canvas.itemconfigure(self.cbox, text=question)
        elif cp == 1:
            str = auth.login(self.entry0.get(), self.entry1.get())
            if str == 0:
                self.canvas.itemconfigure(self.nbox, text="Invalid Email Address")
                self.loadcaptcha()
                self.canvas.itemconfigure(self.cbox, text=question)
            elif str == 3:
                self.canvas.itemconfigure(self.nbox, text="No Internet Connection")
                self.loadcaptcha()
                self.canvas.itemconfigure(self.cbox, text=question)
            elif str == 1:
                self.canvas.itemconfigure(self.nbox, text="Successfully logged in!", fill='#008000')
                container.show_frame(Home,None,None,None,None,None)
            elif str == 2:
                self.canvas.itemconfigure(self.nbox, text="Invalid email or password")
                self.loadcaptcha()
                self.canvas.itemconfigure(self.cbox, text=question)

from tkinter import *
from welcome import Welcome
from home import Home
from signup import Signup
from forgot_pass import Forgot_password