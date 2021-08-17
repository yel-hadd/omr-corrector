from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("800x500")
window.configure(bg = "#ffffff")
canvas2 = Canvas(
    window,
    bg = "#ffffff",
    height = 500,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas2.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas2.create_image(
    400.0, 250.0,
    image=background_img)

canvas2.create_text(
    377.0, 167.5,
    text = "Titre du 1er chapitre",
    fill = "#000000",
    font = ("Kanit-Light", int(13.17255973815918)))

canvas2.create_text(
    377.0, 251.5,
    text = "Titre du 2eme chapitre",
    fill = "#000000",
    font = ("Kanit-Light", int(13.17255973815918)))

canvas2.create_text(
    342.0, 335.5,
    text = "Titre du 3eme chapitre",
    fill = "#000000",
    font = ("Kanit-Light", int(13.17255973815918)))

canvas2.create_text(
    585.5, 167.0,
    text = "Nombre des questions",
    fill = "#000000",
    font = ("Kanit-Light", int(13.17255973815918)))

canvas2.create_text(
    585.5, 251.0,
    text = "Nombre des questions",
    fill = "#000000",
    font = ("Kanit-Light", int(13.17255973815918)))

canvas2.create_text(
    585.5, 335.0,
    text = "Nombre des questions",
    fill = "#000000",
    font = ("Kanit-Light", int(13.17255973815918)))

canvas2.create_text(
    440.5, 416.0,
    text = "Ajouter un Barème personalisé",
    fill = "#000000",
    font = ("Kanit-Light", int(13.17255973815918)))

canvas2.create_text(
    207.0, 190.5,
    text = "Chapitre 1:",
    fill = "#000000",
    font = ("Kanit-SemiBold", int(13.17255973815918)))

canvas2.create_text(
    211.5, 274.5,
    text = "Chapitre 2:",
    fill = "#000000",
    font = ("Kanit-SemiBold", int(13.17255973815918)))

canvas2.create_text(
    207.0, 358.5,
    text = "Chapitre 3:",
    fill = "#000000",
    font = ("Kanit-SemiBold", int(13.17255973815918)))

im0 = PhotoImage(file = f"img0.png")
bu0 = Button(
    image = im0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

bu0.place(
    x = 66, y = 31,
    width = 160,
    height = 38)

im1 = PhotoImage(file = f"img1.png")
bu1 = Button(
    image = im1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

bu1.place(
    x = 633, y = 38,
    width = 25,
    height = 25)

im2 = PhotoImage(file = f"img2.png")
bu2 = Button(
    image = im2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

bu2.place(
    x = 669, y = 38,
    width = 25,
    height = 25)

im3 = PhotoImage(file = f"img3.png")
bu3 = Button(
    image = im3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

bu3.place(
    x = 705, y = 38,
    width = 25,
    height = 25)

ent0_img = PhotoImage(file = f"img_textBox0.png")
ent0_bg = canvas2.create_image(
    374.5, 198.5,
    image = ent0_img)

ent0 = Entry(
    bd = 0,
    bg = "#eeeeee",
    highlightthickness = 0)

ent0.place(
    x = 287.0116558074951, y = 183,
    width = 174.97668838500977,
    height = 29)

ent1_img = PhotoImage(file = f"img_textBox1.png")
ent1_bg = canvas2.create_image(
    374.5, 282.5,
    image = ent1_img)

ent1 = Entry(
    bd = 0,
    bg = "#eeeeee",
    highlightthickness = 0)

ent1.place(
    x = 287.0116558074951, y = 267,
    width = 174.97668838500977,
    height = 29)

ent2_img = PhotoImage(file = f"img_textBox2.png")
ent2_bg = canvas2.create_image(
    374.5, 366.5,
    image = ent2_img)

ent2 = Entry(
    bd = 0,
    bg = "#eeeeee",
    highlightthickness = 0)

ent2.place(
    x = 287.0116558074951, y = 351,
    width = 174.97668838500977,
    height = 29)

ent3_img = PhotoImage(file = f"img_textBox3.png")
ent3_bg = canvas2.create_image(
    587.0, 198.5,
    image = ent3_img)

ent3 = Entry(
    bd = 0,
    bg = "#eeeeee",
    highlightthickness = 0)

ent3.place(
    x = 528.0116558074951, y = 183,
    width = 117.97668838500977,
    height = 29)

ent4_img = PhotoImage(file = f"img_textBox4.png")
ent4_bg = canvas2.create_image(
    587.0, 282.5,
    image = ent4_img)

ent4 = Entry(
    bd = 0,
    bg = "#eeeeee",
    highlightthickness = 0)

ent4.place(
    x = 528.0116558074951, y = 267,
    width = 117.97668838500977,
    height = 29)

ent5_img = PhotoImage(file = f"img_textBox5.png")
ent5_bg = canvas2.create_image(
    587.0, 366.5,
    image = ent5_img)

ent5 = Entry(
    bd = 0,
    bg = "#eeeeee",
    highlightthickness = 0)

ent5.place(
    x = 528.0116558074951, y = 351,
    width = 117.97668838500977,
    height = 29)

im4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = im4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 408, y = 440,
    width = 136,
    height = 34)

im5 = PhotoImage(file = f"img5.png")
bu5 = Button(
    image = im5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

bu5.place(
    x = 255, y = 440,
    width = 136,
    height = 34)

canvas2.create_text(
    399.0, 87.0,
    text = "Ajout Des Chapitres",
    fill = "#000000",
    font = ("Kanit-Regular", int(28.404987335205078)))

canvas2.create_text(
    399.5, 129.0,
    text = "un moyen rapide et efficace pour générer les feuilles d'examen",
    fill = "#4b4a4a",
    font = ("Lato-SemiBold", int(13.300724983215332)))

ch1c = BooleanVar()
ch2c = BooleanVar()
ch3c = BooleanVar()

cbu1 = Checkbutton(window,variable=ch1c, onvalue=True, offvalue=False, command=btn_clicked)

cbu1.place(x=136, y=180)

cbu2 = Checkbutton(window,variable=ch2c, onvalue=True, offvalue=False, command=btn_clicked)

cbu2.place(x=137, y=265)

cbu3 = Checkbutton(window,variable=ch3c, onvalue=True, offvalue=False, command=btn_clicked)

cbu3.place(x=137, y=345)

"""def check_c(c1, c2,c3):
    if (c3 is True) and ((c1 is not True) or (c2 is not True)):
        canvas2.ch3c = False
        canvas2.ch2c = False
    if (c2 is True) and (c1 is not True):
        canvas2.ch3c = False
        canvas2.ch2c = False"""



window.resizable(False, False)
window.mainloop()
