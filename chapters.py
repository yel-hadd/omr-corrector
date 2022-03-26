from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from generate import Generate
from correct import Correct
from home import Home
import generateExam as gen


def btn_clicked():
    print('HI')

class Chapters(ttk.Frame):
    def quitg(self):
        self.quit()
    def __init__(self, container, question, choice, excel, lang, output):
        super().__init__(container)

        self.canvas2 = Canvas(
            bg="#ffffff",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas2.place(x=0, y=0)

        self.background_img = PhotoImage(file=f"./src/chapters/background.png")
        self.background = self.canvas2.create_image(
            400.0, 250.0,
            image=self.background_img)

        self.canvas2.create_text(
            340.0, 167.5,
            text="Titre du 1er unité",
            fill="#000000",
            font=("Kanit Light", int(13.17255973815918)))

        self.canvas2.create_text(
            347.0, 251.5,
            text="Titre du 2éme unité",
            fill="#000000",
            font=("Kanit Light", int(13.17255973815918)))

        self.canvas2.create_text(
            347, 335.5,
            text="Titre du 3éme unité",
            fill="#000000",
            font=("Kanit Light", int(13.17255973815918)))

        self.canvas2.create_text(
            585.5, 167.0,
            text="Nombre de questions",
            fill="#000000",
            font=("Kanit Light", 11))

        self.canvas2.create_text(
            585.5, 251.0,
            text="Nombre de questions",
            fill="#000000",
            font=("Kanit Light", 11))

        self.canvas2.create_text(
            585.5, 335.0,
            text="Nombre de questions",
            fill="#000000",
            font=("Kanit Light", 11))

        """self.canvas2.create_text(
            440.5, 416.0,
            text="Ajouter un Barème personalisé",
            fill="#000000",
            font=("Kanit Light", int(13.17255973815918)))"""

        self.canvas2.create_text(
            207.0, 190.5,
            text="Unité 1:",
            fill="#000000",
            font=("Kanit SemiBold", int(13.17255973815918)))

        self.canvas2.create_text(
            211.5, 274.5,
            text="Unité 2:",
            fill="#000000",
            font=("Kanit SemiBold", int(13.17255973815918)))

        self.canvas2.create_text(
            207.0, 358.5,
            text="Unité 3:",
            fill="#000000",
            font=("Kanit SemiBold", int(13.17255973815918)))

        self.im0 = PhotoImage(file=f"./src/chapters/img0.png")
        bu0 = Button(
            image=self.im0,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")

        bu0.place(
            x=66, y=31,
            width=160,
            height=38)

        self.im1 = PhotoImage(file=f"./src/chapters/img1.png")
        bu1 = Button(
            image=self.im1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Home,None,None,None,None,None),
            relief="flat")

        bu1.place(
            x=633, y=38,
            width=25,
            height=25)

        self.im2 = PhotoImage(file=f"./src/chapters/img2.png")
        bu2 = Button(
            image=self.im2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Correct,None,None,None,None,None),
            relief="flat")

        bu2.place(
            x=669, y=38,
            width=25,
            height=25)

        self.im3 = PhotoImage(file=f"./src/chapters/img3.png")
        bu3 = Button(
            image=self.im3,
            borderwidth=0,
            highlightthickness=0,
            command=self.quitg,
            relief="flat")

        bu3.place(
            x=705, y=38,
            width=25,
            height=25)

        self.ent0_img = PhotoImage(file=f"./src/chapters/img_textBox0.png")
        ent0_bg = self.canvas2.create_image(
            374.5, 198.5,
            image=self.ent0_img)

        self.ent0 = Entry(
            bd=0,
            bg="#eeeeee",
            highlightthickness=0)

        self.ent0.place(
            x=287.0116558074951, y=183,
            width=174.97668838500977,
            height=29)

        self.ent1_img = PhotoImage(file=f"./src/chapters/img_textBox1.png")
        self.ent1_bg = self.canvas2.create_image(
            374.5, 282.5,
            image=self.ent1_img)

        self.ent1 = Entry(
            bd=0,
            bg="#eeeeee",
            highlightthickness=0)

        self.ent1.place(
            x=287.0116558074951, y=267,
            width=174.97668838500977,
            height=29)

        self.ent2_img = PhotoImage(file=f"./src/chapters/img_textBox2.png")
        self.ent2_bg = self.canvas2.create_image(
            374.5, 366.5,
            image=self.ent2_img)

        self.ent2 = Entry(
            bd=0,
            bg="#eeeeee",
            highlightthickness=0)

        self.ent2.place(
            x=287.0116558074951, y=351,
            width=174.97668838500977,
            height=29)

        self.ent3_img = PhotoImage(file=f"./src/chapters/img_textBox3.png")
        self.ent3_bg = self.canvas2.create_image(
            587.0, 198.5,
            image=self.ent3_img)

        self.ent3 = Entry(
            bd=0,
            bg="#eeeeee",
            highlightthickness=0)

        self.ent3.place(
            x=528.0116558074951, y=183,
            width=117.97668838500977,
            height=29)

        self.ent4_img = PhotoImage(file=f"./src/chapters/img_textBox4.png")
        self.ent4_bg = self.canvas2.create_image(
            587.0, 282.5,
            image=self.ent4_img)

        self.ent4 = Entry(
            bd=0,
            bg="#eeeeee",
            highlightthickness=0)

        self.ent4.place(
            x=528.0116558074951, y=267,
            width=117.97668838500977,
            height=29)

        self.ent5_img = PhotoImage(file=f"./src/chapters/img_textBox5.png")
        ent5_bg = self.canvas2.create_image(
            587.0, 366.5,
            image=self.ent5_img)

        self.ent5 = Entry(
            bd=0,
            bg="#eeeeee",
            highlightthickness=0)

        self.ent5.place(
            x=528.0116558074951, y=351,
            width=117.97668838500977,
            height=29)

        self.im4 = PhotoImage(file=f"./src/chapters/img4.png")
        b4 = Button(
            image=self.im4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.generate_chap_btn(question, choice, excel, lang, output),
            relief="flat")

        b4.place(
            x=408, y=420,
            width=136,
            height=34)

        self.im5 = PhotoImage(file=f"./src/chapters/img5.png")
        self.bu5 = Button(
            image=self.im5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Generate,None,None,None,None,None),
            relief="flat")

        self.bu5.place(
            x=255, y=420,
            width=136,
            height=34)

        self.canvas2.create_text(
            399.0, 107.0,
            text="Ajout Des Unités",
            fill="#000000",
            font=("Kanit Regular", 24))

        """self.canvas2.create_text(
            399.5, 129.0,
            text="un moyen rapide et efficace pour générer les feuilles d'examen",
            fill="#4b4a4a",
            font=("Lato SemiBold", int(13.300724983215332)))"""

        self.ch1c = BooleanVar()
        self.ch2c = BooleanVar()
        self.ch3c = BooleanVar()
        self.bareme_c = BooleanVar()

        self.cbu1 = Checkbutton(self.canvas2, variable=self.ch1c, bg='white', onvalue=True, offvalue=False)

        self.cbu1.place(x=136, y=180)

        cbu2 = Checkbutton(self.canvas2, variable=self.ch2c, bg='white', onvalue=True, offvalue=False)

        cbu2.place(x=137, y=265)

        cbu3 = Checkbutton(self.canvas2, variable=self.ch3c, bg='white', onvalue=True, offvalue=False)

        cbu3.place(x=137, y=345)

        #cbb = Checkbutton(self.canvas2, variable=self.bareme_c, bg='white', onvalue=True, offvalue=False)

        #cbb.place(x=286, y=404)

        return

    def generate_chap_btn(self, question, choice, excel, lang, output):
        quest = question
        choi = choice
        xlsx = excel
        language = lang
        out = output
        c1 = self.ch1c.get()
        c2 = self.ch2c.get()
        c3 = self.ch3c.get()
        b = self.bareme_c.get()
        if (c1 == True) and (c2 != True) and (c3!= True):
            self.ch1 = f'{self.ent0.get()}:{self.ent3.get()}'
            self.ch2 = None
            self.ch3 = None
            self.chapters = 1
        elif (c1 == True) and (c2 == True) and (c3!= True):
            self.ch1 = f'{self.ent0.get()}:{self.ent3.get()}'
            self.ch2 = f'{self.ent1.get()}:{self.ent4.get()}'
            self.ch3 = None
            self.chapters = 2
        elif (c1 == True) and (c2 == True) and (c3 == True):
            self.ch1 = f'{self.ent0.get()}:{self.ent3.get()}'
            self.ch2 = f'{self.ent1.get()}:{self.ent4.get()}'
            self.ch3 = f'{self.ent2.get()}:{self.ent5.get()}'
            self.chapters = 3
        else:
            self.ch1 = None
            self.ch2 = None
            self.ch3 = None
            self.chapters = 0

        messagebox.showinfo(title="Veuillez patienter",
                            message="La tâche est en cours de traitement")

        gen.generateExam(quest, choi, xlsx, language, out,
                         self.ch1, self.ch2, self.ch3, self.chapters)

        messagebox.showinfo(title='succès',
                            message='tâche accomplie avec succès')
