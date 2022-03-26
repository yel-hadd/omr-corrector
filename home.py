from tkinter import ttk

def btn_clicked():
    print('HI')

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
            command=lambda: container.show_frame(Generate,None,None,None,None,None),
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
            command=lambda: container.show_frame(Correct,None,None,None,None,None),
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
            command=lambda: container.show_frame(Contact,None,None,None,None,None),
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
            text="Contactez-moi",
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
            text="Bienvenue sur VIP GRADER",
            fill="#000000",
            font=("Kanit Regular", 24))

        canvas.create_text(
            400.0, 148.5,
            text="un logiciel rapide, puissant et pratique !",
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

from tkinter import *
from generate import Generate
from contact import Contact
from correct import Correct