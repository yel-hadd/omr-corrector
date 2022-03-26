from tkinter import ttk

def btn_clicked():
    print('HI')

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

    def quitf(self):
        self.quit()

    def btn_clicked(self):
        print('Hi')

    def __init__(self, container):
        super().__init__(container)

        self.container = container

        self.canvas = Canvas(
            bg="#ffffff",
            height=500,
            width=800,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        self.canvas.place(x=0, y=0)
        self.chap_cb = BooleanVar()

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
            220, 175,
            text="Nombre de questions (5 - 20)",
            fill="#000000",
            font=("Kanit Light", 15))

        self.canvas.create_text(
            532, 175,
            text="Nombre de choix (3 - 5)",
            fill="#000000",
            font=("Kanit Light", 15))

        self.canvas.create_text(
            170.0, 252.0,
            text="Langue (fr ou ar)",
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
            709, 356,
            text="Ajouter des unités",
            fill="#000000",
            font=("Kanit Light", 11))

        self.canvas.create_text(
            402.0, 115,
            text="générer les feuilles d'examen",
            fill="#000000",
            font=("Kanit Regular", 24))

        """self.canvas.create_text(
            402.0, 138,
            text="un moyen rapide et efficace pour générer les feuilles d'examen",
            fill="#4b4a4a",
            font=("Lato SemiBold", 14))"""

        self.img0 = PhotoImage(file=f"./src/generate/img0.png")
        b0 = Button(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Home,None,None,None,None,None),
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
            command=lambda: container.show_frame(Home,None,None,None,None,None),
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
            command=lambda: container.show_frame(Correct,None,None,None,None,None),
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

        self.cbu1 = Checkbutton(self.canvas, variable=self.chap_cb, bg='#00766F', onvalue=True, offvalue=False)
        self.cbu1.place(x=607, y=347)

    def gen_button(self):
        self.question = int(self.entry0.get())
        self.choice = int(self.entry1.get())
        self.lang = str(self.entry2.get())
        self.excel = str(self.entry4.get())
        self.output = str(self.entry3.get())
        if self.chap_cb.get() == False:
            messagebox.showinfo(title="Veuillez patienter",
                                 message="La tâche est en cours de traitement")
            gen.generateExam(self.question, self.choice, self.excel, self.lang, self.output, None, None, None, 0)
            messagebox.showinfo(title='succès',
                                message='tâche accomplie avec succès')
        elif self.chap_cb.get() == True:
            self.container.show_frame(Chapters, self.question, self.choice, self.excel, self.lang,
                              self.output)

from home import Home
from chapters import Chapters
from correct import Correct
import generateExam as gen
from tkinter import *
from tkinter import filedialog, messagebox
