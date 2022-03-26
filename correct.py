import os.path
from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox
import main as m
from report import gen_report as gr
from home import Home
from generate import Generate


def btn_clicked():
    print('HI')

class Correct(ttk.Frame):
    def select_path(self, event):
        self.output_path = str
        self.output_path = filedialog.askdirectory(title= 'Répertoire de sortie')
        self.entry0.delete(0, END)
        self.entry0.insert(0, self.output_path)

    def select_tf(self):
        self.teacher_sheet = filedialog.askopenfilename(title = "Select file",filetypes =(("PNG", "*.png"),("JPG", "*.jpg"),("Image Files","*.*")))

    def select_sf(self):
        self.students_sheet = tuple
        self.students_sheet = filedialog.askopenfilenames(title = "Select file",filetypes =(("PNG", "*.png"),("JPG", "*.jpg"),("Image Files","*.*")))
        self.students_sheet = list(self.students_sheet)

    def quitf(self):
        self.quit()

    def correct_button(self):
        self.canvas.itemconfigure(self.nbox,
                                  text='en cours de traitement, veuillez patienter',
                                  fill='#006400')
        self.canvas.update()

        try:
            ans, sch, cla, tea, sub, lvl, smstr, dir, aca, nbrc, chapt1, chapt2, chap3  = m.genAns(self.teacher_sheet)
        except IndexError:
            messagebox.showerror(title="Error",
                                 message="Can't scan teacher's sheet, please add another image")
            self.canvas.itemconfigure(self.nbox, text='')
            self.canvas.update()
            return 1
        except AttributeError:
            self.canvas.itemconfigure(self.nbox, text='')
            self.canvas.update()
            return 1

        if self.teacher_sheet == None:
            messagebox.showerror(title="Error",
                                 message="Can't scan teacher's sheet, please add another image")
            self.canvas.itemconfigure(self.nbox, text='')
            self.canvas.update()
        if not self.students_sheet:
            messagebox.showerror(title="Empty Fields",
                                 message="Please enter Students sheets")
            self.canvas.itemconfigure(self.nbox, text='')
            self.canvas.update()
            return 1
        if not self.output_path:
            messagebox.showerror(title="Empty Fields",
                                 message="Please select the output path")
            self.canvas.itemconfigure(self.nbox, text='')
            self.canvas.update()

        csv_path = None
        for image in self.students_sheet:
            try:
                csv_path, sbr = m.correctExam(image, ans, None, self.output_path, nbrc, chapt1, chapt2, chap3)
                self.canvas.update()
            except:
                pass

        # no_chapter(path, rep, 20, _class, semester, level, academie, direction, school, subject, teacher)
        if os.path.isfile(csv_path):
            gr(csv_path, self.output_path, nbrc, sbr, cla, smstr, lvl, aca, dir, sch, sub, tea)
            #threading.Thread(target=self.correct_button).start()

        self.canvas.itemconfigure(self.nbox, text='tâche accomplie avec succès')
        self.canvas.update()
        messagebox.showinfo(title='succès',
                            message='tâche accomplie avec succès')
        return 0

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
            401.5, 110,
            text="Corriger un examen",
            fill="#000000",
            font=("Kanit Regular", 25))

        """self.canvas.create_text(
            402.0, 138.5,
            text="un moyen rapide et efficace pour corriger les feuilles d'examen",
            fill="#4b4a4a",
            font=("Lato", 13))"""

        self.nbox = self.canvas.create_text(
            560, 331.5,
            text='',
            fill="#ff0000",
            font=("Kanit Light", 12))

        self.img0 = PhotoImage(file=f"./src/correct/img0.png")
        b0 = Button(
            image=self.img0,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: container.show_frame(Home,None,None,None,None,None),
            relief="flat")

        b0.place(
            x=74, y=23,
            width=162,
            height=39)

        # ! ADD THREADING !#
        self.img1 = PhotoImage(file=f"./src/correct/img1.png")
        b1 = Button(
            image=self.img1,
            borderwidth=0,
            highlightthickness=0,
            #command=self.correct_button,
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
            command=lambda: container.show_frame(Home,None,None,None,None,None),
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
            command=lambda: container.show_frame(Generate,None,None,None,None,None),
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
            x=426, y=164,
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
            x=101, y=164,
            width=280,
            height=128)