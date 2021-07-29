import tkinter as tk
from tkinter import *
from tkinter import ttk
import auth
import captcha

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwarness(1)
except:
    pass

class Window(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title('Maxi Correcteur')
        self.geometry('800x500')
        Signup(self).pack()

class Home(ttk.Frame):
    def quitf(self):
        self.quit()

    def btn_clicked(self):
        print("Button Clicked")

    def __init__(self, container):
        super().__init__(container)

        canvas = Canvas(
            bg="#ffffff",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        self.img0 = PhotoImage(file=f"./src/home/img0.png")
        b0 = Button(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b0.place(
            x=262, y=198,
            width=78,
            height=78)

        self.img1 = PhotoImage(file=f"./src/home/img1.png")
        b1 = Button(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b1.place(
            x=457, y=198,
            width=78,
            height=78)

        self.img2 = PhotoImage(file=f"./src/home/img2.png")
        b2 = Button(
            image=self.img2,
            borderwidth=0,
            highlightthickness=0,
            command=self.quitf,
            relief="flat")

        b2.place(
            x=457, y=334,
            width=78,
            height=78)

        self.img3 = PhotoImage(file=f"./src/home/img3.png")
        b3 = Button(
            image=self.img3,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b3.place(
            x=262, y=334,
            width=78,
            height=78)

        canvas.create_text(
            300.0, 298.0,
            text="Générer un examen",
            fill="#000000",
            font=("Kanit Regular", 15))

        canvas.create_text(
            297.5, 438.0,
            text="Contactez-nous",
            fill="#000000",
            font=("Kanit Regular", 15))

        canvas.create_text(
            498.5, 298.0,
            text="Corriger un examen",
            fill="#000000",
            font=("Kanit Regular", 15))

        canvas.create_text(
            498.5, 438.0,
            text="Quitter l'application",
            fill="#000000",
            font=("Kanit Regular", 15))

        canvas.create_text(
            399.0, 110,
            text="Lorem ipsum dolor sit amet",
            fill="#000000",
            font=("Kanit Regular", 24))

        canvas.create_text(
            400.0, 148.5,
            text="Lorem ipsum dolor sit amet, consectetur adipiscing elit ut aliquam.",
            fill="#4b4a4a",
            font=("Lato SemiBold", 14))

        self.img4 = PhotoImage(file=f"./src/home/img4.png")
        b4 = Button(
            image=self.img4,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b4.place(
            x=33, y=21,
            width=174,
            height=41)

        self.img5 = PhotoImage(file=f"./src/home/img5.png")
        b5 = Button(
            image=self.img5,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b5.place(
            x=33, y=194,
            width=132,
            height=259)

        self.img6 = PhotoImage(file=f"./src/home/img6.png")
        b6 = Button(
            image=self.img6,
            borderwidth=0,
            highlightthickness=0,
            command=self.btn_clicked,
            relief="flat")

        b6.place(
            x=632, y=194,
            width=132,
            height=259)

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
            command=self.btn_clicked,
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
            command=self.btn_clicked,
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
            command=self.btn_clicked,
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
            command=self.btn_clicked,
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
            command=self.login_btn,
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

    def login_btn(self):
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
            elif str == 1:
                self.canvas.itemconfigure(self.nbox, text="Successfully logged in!", fill='#008000')
            elif str == 2:
                self.canvas.itemconfigure(self.nbox, text="Invalid email or password")
                self.loadcaptcha()
                self.canvas.itemconfigure(self.cbox, text=question)

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
            command=self.btn_clicked,
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
            command=self.btn_clicked,
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
            command=self.btn_clicked,
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
            command=self.btn_clicked,
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

    def btn_clicked(self):
        print('Button clicked')

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

class Forgot_password(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

class Genrate(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

class Correct(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

class Contact(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)


root = Window()
root.resizable(False, False)
root.mainloop()
