from tkinter import *
from tkinter import ttk
from generate import Generate
from correct import Correct
from home import Home


def btn_clicked():
    print('HI')

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
            command=lambda: container.show_frame(Home,None,None,None,None,None),
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
            command=lambda: container.show_frame(Correct,None,None,None,None,None),
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
            command=lambda: container.show_frame(Generate,None,None,None,None,None),
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
            400.5, 121.5,
            text="Contactez-moi:",
            fill="#ffffff",
            font=("Kanit Bold", int(34.36180877685547)))

        self.canvas.create_text(
            400.0, 232.5,
            text="Yassine El Haddad",
            fill="#000000",
            font=("Kanit Regular", int(29.166667938232422)))

        self.canvas.create_text(
            399.5, 271.0,
            text="services divers de développement informatique.",
            fill="#000000",
            font=("Lato Regular", int(16.33333396911621)))

        self.canvas.create_text(
            399.5, 334.5,
            text="0619666722",
            fill="#000000",
            font=("Kanit Regular", int(21.0)))

        self.canvas.create_text(
            400.0, 365.5,
            text="yassine.e@aol.com",
            fill="#000000",
            font=("Kanit Regular", int(21.0)))

