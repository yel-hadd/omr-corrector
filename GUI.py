import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import main as m
import auth
import captcha
import generateExam as gen

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwarness(1)
except:
    pass

def btn_clicked():
    print('HI')

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Maxi Correcteur')
        self.geometry('800x500')
        self.frames = {}
        container = ttk.Frame(self)
        container.pack()

        self.show_frame(Correct)

    def show_frame(self, container):
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
            command=lambda: container.show_frame(Generate),
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
            command=lambda: container.show_frame(Correct),
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
            command=lambda: container.show_frame(Contact),
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
            command=btn_clicked,
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
            command=btn_clicked,
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
            command=btn_clicked,
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
            command=lambda: container.show_frame(Signup),
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
            command=lambda: container.show_frame(Welcome),
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
            command=lambda: container.show_frame(Forgot_password),
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
            elif str == 1:
                self.canvas.itemconfigure(self.nbox, text="Successfully logged in!", fill='#008000')
                container.show_frame(Home)
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
            command=lambda: container.show_frame(Login),
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
            command=lambda: container.show_frame(Welcome),
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
            command=lambda: container.show_frame(Login),
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
            command=lambda: container.show_frame(Login),
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
            command=lambda: container.show_frame(Signup),
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
            command=lambda: container.show_frame(Welcome),
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

class Generate(ttk.Frame):
    def select_path(self, event):
        self.output_path = str
        # window.withdraw()
        self.output_path = filedialog.askdirectory(title= ' Répertoire de sortie')
        self.entry3.delete(0, END)
        self.entry3.insert(0, self.output_path)

    def select_file(self, event):
        self.file_path = str
        self.file_path = filedialog.askopenfilename(title = "Select file",filetypes = (("MS Excel","*.xlsx"),))
        self.entry4.delete(0, END)
        self.entry4.insert(0, self.file_path)

    def gen_button(self):
        question = int(self.entry0.get())
        choice = int(self.entry1.get())
        lang = str(self.entry2.get())
        excel = str(self.entry4.get())
        output = str(self.entry3.get())
        gen.generateExam(question, choice, excel, lang, output)
        print('done')

    def quitf(self):
        self.quit()

    def btn_clicked(self):
        print('Hi')


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

        self.entry0_img = PhotoImage(file=f"./src/generate/img_textBox0.png")
        entry0_bg = self.canvas.create_image(
            236.0, 214.5,
            image=self.entry0_img)

        self.entry0 = Entry(
            bd=0,
            bg="#eeeeee",
            font='Calibri 14',
            highlightthickness=0)

        self.entry0.place(
            x=102.5240249633789, y=196,
            width=266.9519500732422,
            height=35)

        self.entry1_img = PhotoImage(file=f"./src/generate/img_textBox1.png")
        entry1_bg = self.canvas.create_image(
            570.0, 215.5,
            image=self.entry1_img)

        self.entry1 = Entry(
            bd=0,
            font='Calibri 14',
            bg="#eeeeee",
            highlightthickness=0)

        self.entry1.place(
            x=436.5240249633789, y=197,
            width=266.9519500732422,
            height=35)

        self.entry2_img = PhotoImage(file=f"./src/generate/img_textBox2.png")
        entry2_bg = self.canvas.create_image(
            237.0, 288.0,
            image=self.entry2_img)

        self.entry2 = Entry(
            bd=0,
            font='Calibri 14',
            bg="#eeeeee",
            highlightthickness=0)

        self.entry2.place(
            x=103.5240249633789, y=270,
            width=266.9519500732422,
            height=34)

        self.entry3_img = PhotoImage(file=f"./src/generate/img_textBox3.png")
        entry3_bg = self.canvas.create_image(
            236.0, 361.0,
            image=self.entry3_img)

        self.entry3 = Entry(
            bd=0,
            font='Calibri 14',
            bg="#eeeeee",
            highlightthickness=0)
        self.entry3.bind("<1>", self.select_path)

        self.entry3.place(
            x=102.5240249633789, y=343,
            width=266.9519500732422,
            height=34)

        self.entry4_img = PhotoImage(file=f"./src/generate/img_textBox4.png")
        entry4_bg = self.canvas.create_image(
            571.0, 288.5,
            image=self.entry4_img)

        self.entry4 = Entry(
            bd=0,
            font='Calibri 14',
            bg="#eeeeee",
            highlightthickness=0)
        self.entry4.bind("<1>", self.select_file)


        self.entry4.place(
            x=437.5240249633789, y=270,
            width=266.9519500732422,
            height=35)

        self.canvas.create_text(
            190, 178.5,
            text="Nombre de questions",
            fill="#000000",
            font=("Kanit Light", 16))

        self.canvas.create_text(
            502, 175,
            text="Nombre de choix",
            fill="#000000",
            font=("Kanit Light", 16))

        self.canvas.create_text(
            127.0, 252.0,
            text="Langue",
            fill="#000000",
            font=("Kanit Light", 16))

        self.canvas.create_text(
            485.0, 252.5,
            text="Fichier Excel",
            fill="#000000",
            font=("Kanit Light", 16))

        self.canvas.create_text(
            185, 324.0,
            text="Répertoire de sortie",
            fill="#000000",
            font=("Kanit Light", 16))

        self.canvas.create_text(
            402.0, 102,
            text="générer les feuilles d'examen",
            fill="#000000",
            font=("Kanit Regular", 24))

        self.canvas.create_text(
            402.0, 138,
            text="un moyen rapide et efficace pour générer les feuilles d'examen",
            fill="#4b4a4a",
            font=("Lato SemiBold", 14))

        self.img0 = PhotoImage(file=f"./src/generate/img0.png")
        b0 = Button(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Home),
            relief="flat")

        b0.place(
            x=65, y=27,
            width=167,
            height=40)

        self.img1 = PhotoImage(file=f"./src/generate/img1.png")
        b1 = Button(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            command=self.gen_button,
            relief="flat")

        b1.place(
            x=426, y=340,
            width=166,
            height=41)

        self.img2 = PhotoImage(file=f"./src/generate/img2.png")
        b2 = Button(
            image=self.img2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Home),
            relief="flat")

        b2.place(
            x=636, y=33,
            width=25,
            height=25)

        self.img3 = PhotoImage(file=f"./src/generate/img3.png")
        b3 = Button(
            image=self.img3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Correct),
            relief="flat")

        b3.place(
            x=672, y=33,
            width=25,
            height=25)

        self.img4 = PhotoImage(file=f"./src/generate/img4.png")
        b4 = Button(
            image=self.img4,
            borderwidth=0,
            highlightthickness=0,
            command=self.quitf,
            relief="flat")

        b4.place(
            x=709, y=33,
            width=25,
            height=25)

        self.img5 = PhotoImage(file=f"./src/generate/img5.png")
        b5 = Button(
            image=self.img5,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        b5.place(
            x=90, y=413,
            width=624,
            height=59)

class Correct(ttk.Frame):
    def select_path(self, event):
        self.output_path = str
        self.output_path = filedialog.askdirectory(title= 'Répertoire de sortie')
        self.entry0.delete(0, END)
        self.entry0.insert(0, self.output_path)

    def select_tf(self):
        self.teacher_sheet = str
        self.teacher_sheet = filedialog.askopenfilename(title = "Select file",filetypes =(("PNG", "*.png"),("JPG", "*.jpg"),("Image Files","*.*")))

    def select_sf(self):
        self.students_sheet = tuple
        self.students_sheet = filedialog.askopenfilenames(title = "Select file",filetypes =(("PNG", "*.png"),("JPG", "*.jpg"),("Image Files","*.*")))
        self.students_sheet = list(self.students_sheet)

    def quitf(self):
        self.quit()

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

        self.entry0_img = PhotoImage(file=f"./src/correct/img_textBox0.png")
        entry0_bg = self.canvas.create_image(
            296.0, 369.0,
            image=self.entry0_img)

        self.entry0 = Entry(
            bd=0,
            bg="#d6d4d4",
            highlightthickness=0)

        self.entry0.bind("<1>", self.select_path)

        self.entry0.place(
            x=166.23933792114258, y=351,
            width=259.52132415771484,
            height=34)

        self.canvas.create_text(
            245.5, 334.0,
            text="Répertoire de sortie",
            fill="#000000",
            font=("Kanit Light", 16))

        self.canvas.create_text(
            401.5, 94.5,
            text="Corriger les feuilles d'examen",
            fill="#000000",
            font=("Kanit Regular", 25))

        self.canvas.create_text(
            402.0, 138.5,
            text="un moyen rapide et efficace pour corriger les feuilles d'examen",
            fill="#4b4a4a",
            font=("Lato", 13))

        self.img0 = PhotoImage(file=f"./src/correct/img0.png")
        b0 = Button(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Home),
            relief="flat")

        b0.place(
            x=74, y=23,
            width=162,
            height=39)

        self.img1 = PhotoImage(file=f"./src/correct/img1.png")
        b1 = Button(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            command=self.correct_button,
            relief="flat")

        b1.place(
            x=483, y=351,
            width=161,
            height=40)

        self.img2 = PhotoImage(file=f"./src/correct/img2.png")
        b2 = Button(
            image=self.img2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Home),
            relief="flat")

        b2.place(
            x=630, y=29,
            width=25,
            height=25)

        self.img3 = PhotoImage(file=f"./src/correct/img3.png")
        b3 = Button(
            image=self.img3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Generate),
            relief="flat")

        b3.place(
            x=665, y=29,
            width=25,
            height=25)

        self.img4 = PhotoImage(file=f"./src/correct/img4.png")
        b4 = Button(
            image=self.img4,
            borderwidth=0,
            highlightthickness=0,
            command=self.quitf,
            relief="flat")

        b4.place(
            x=700, y=29,
            width=25,
            height=25)

        self.img5 = PhotoImage(file=f"./src/correct/img5.png")
        b5 = Button(
            image=self.img5,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        b5.place(
            x=99, y=420,
            width=607,
            height=58)

        self.img6 = PhotoImage(file=f"./src/correct/img6.png")
        b6 = Button(
            image=self.img6,
            borderwidth=0,
            highlightthickness=0,
            command=self.select_sf,
            relief="flat")

        b6.place(
            x=426, y=174,
            width=280,
            height=128)

        self.img7 = PhotoImage(file=f"./src/correct/img7.png")
        b7 = Button(
            image=self.img7,
            borderwidth=0,
            highlightthickness=0,
            command=self.select_tf,
            relief="flat")

        b7.place(
            x=101, y=174,
            width=280,
            height=128)

    def correct_button(self):
        ans = m.genAns(self.teacher_sheet)
        for image in self.students_sheet:
            try:
                m.correctExam(image, ans, None, self.output_path)
            except:
                pass
        print('done')

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
            command=lambda: container.show_frame(Signup),
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
            command=lambda: container.show_frame(Login),
            relief="flat")

        b1.place(
            x=423, y=430,
            width=137,
            height=34)

        self.canvas.create_text(
            399.0, 389.5,
            text="BIENVENU DANS MAXI CORRECTEUR!",
            fill="#000000",
            font=("Lato SemiBold", 23))

class Contact(ttk.Frame):
    def btn_clicked(self):
        print('Clicked')

    def quitf(self):
        self.quit()

    def __init__(self, container):
        super().__init__(container)
        self.canvas = Canvas(
            bg="#00766f",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"./src/contact/background.png")
        background = self.canvas.create_image(
            400.0, 250.0,
            image=self.background_img)

        self.img0 = PhotoImage(file=f"./src/contact/img0.png")
        b0 = Button(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Home),
            relief="flat")

        b0.place(
            x=599, y=21,
            width=25,
            height=25)

        self.img1 = PhotoImage(file=f"./src/contact/img1.png")
        b1 = Button(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Correct),
            relief="flat")

        b1.place(
            x=635, y=21,
            width=25,
            height=25)

        self.img2 = PhotoImage(file=f"./src/contact/img2.png")
        b2 = Button(
            image=self.img2,
            borderwidth=0,
            highlightthickness=0,
            command=self.quitf,
            relief="flat")

        b2.place(
            x=706, y=21,
            width=25,
            height=25)

        self.img3 = PhotoImage(file=f"./src/contact/img3.png")
        b3 = Button(
            image=self.img3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Generate),
            relief="flat")

        b3.place(
            x=671, y=21,
            width=25,
            height=25)

        self.img4 = PhotoImage(file=f"./src/contact/img4.png")
        b4 = Button(
            image=self.img4,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        b4.place(
            x=57, y=14,
            width=162,
            height=39)

        self.canvas.create_text(
            399.5, 121.5,
            text="Contactez-nous:",
            fill="#ffffff",
            font=("Kanit Bold", int(34.36180877685547)))

        self.canvas.create_text(
            244.0, 206.0,
            text="Librarie Essalam Al-Jadida",
            fill="#000000",
            font=("Lato SemiBold", 16))

        self.canvas.create_text(
            243.5, 231.0,
            text="Lorem ipsum dolor sit amet",
            fill="#000000",
            font=("Montserrat Regular", 10))

        self.canvas.create_text(
            240.5, 267.0,
            text="Télephone:",
            fill="#000000",
            font=("Montserrat Bold", 14))

        self.canvas.create_text(
            240.5, 324.0,
            text="Email:",
            fill="#000000",
            font=("Montserrat Bold", 14))

        self.canvas.create_text(
            240.5, 383.0,
            text="Adresse:",
            fill="#000000",
            font=("Montserrat Bold", 14))

        self.canvas.create_text(
            241.0, 294.5,
            text="0600000000",
            fill="#000000",
            font=("AnonymousPro Regular", 13))

        self.canvas.create_text(
            239.5, 352.5,
            text="justanemail@gmail.com",
            fill="#000000",
            font=("AnonymousPro Regular", 13))

        self.canvas.create_text(
            236.5, 410.5,
            text="adresse agadir agadir",
            fill="#000000",
            font=("AnonymousPro Regular", 13))

        self.canvas.create_text(
            561.5, 206.0,
            text="Sté VALKAN SARL",
            fill="#000000",
            font=("Lato SemiBold", 16))

        self.canvas.create_text(
            561.5, 231.0,
            text="Lorem ipsum dolor sit amet",
            fill="#000000",
            font=("Montserrat Regular", 10))

        self.canvas.create_text(
            558.5, 267.0,
            text="Télephone:",
            fill="#000000",
            font=("Montserrat Bold", 14))

        self.canvas.create_text(
            558.5, 324.0,
            text="Email:",
            fill="#000000",
            font=("Montserrat Bold", 14))

        self.canvas.create_text(
            558.5, 383.0,
            text="Adresse:",
            fill="#000000",
            font=("Montserrat Bold", 14))

        self.canvas.create_text(
            559.0, 294.5,
            text="0600000000",
            fill="#000000",
            font=("AnonymousPro Regular", 13))

        self.canvas.create_text(
            557.5, 352.5,
            text="justanemail@gmail.com",
            fill="#000000",
            font=("AnonymousPro Regular", 13))

        self.canvas.create_text(
            554.5, 410.5,
            text="adresse agadir agadir",
            fill="#000000",
            font=("AnonymousPro Regular", 13))


root = Window()
root.resizable(False, False)
root.mainloop()
