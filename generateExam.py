import qrcode as qr
import os
from PIL import Image, ImageFont, ImageDraw
from bidi.algorithm import get_display
import arabic_reshaper
import img2pdf
import openpyxl as opxl
import transliteration as tl
import regex as re
from datetime import datetime


r = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def SwitchFrThreeChoices(argument):
    switcher = {
        5: "./model/fr/5x3.jpg",
        6: "./model/fr/6x3.jpg",
        7: "./model/fr/7x3.jpg",
        8: "./model/fr/8x3.jpg",
        9: "./model/fr/9x3.jpg",
        10: "./model/fr/10x3.jpg",
        11: "./model/fr/11x3.jpg",
        12: "./model/fr/12x3.jpg",
        13: "./model/fr/13x3.jpg",
        14: "./model/fr/14x3.jpg",
        15: "./model/fr/15x3.jpg",
        16: "./model/fr/16x3.jpg",
        17: "./model/fr/17x3.jpg",
        18: "./model/fr/18x3.jpg",
        19: "./model/fr/19x3.jpg",
        20: "./model/fr/20x3.jpg",
    }
    return switcher.get(argument)

def SwitchFrFourChoices(argument):
    switcher = {
        5: "./model/fr/5x4.jpg",
        6: "./model/fr/6x4.jpg",
        7: "./model/fr/7x4.jpg",
        8: "./model/fr/8x4.jpg",
        9: "./model/fr/9x4.jpg",
        10: "./model/fr/10x4.jpg",
        11: "./model/fr/11x4.jpg",
        12: "./model/fr/12x4.jpg",
        13: "./model/fr/13x4.jpg",
        14: "./model/fr/14x4.jpg",
        15: "./model/fr/15x4.jpg",
        16: "./model/fr/16x4.jpg",
        17: "./model/fr/17x4.jpg",
        18: "./model/fr/18x4.jpg",
        19: "./model/fr/19x4.jpg",
        20: "./model/fr/20x4.jpg",
    }
    return switcher.get(argument)

def SwitchFrFiveChoices(argument):
    switcher = {
        5: "./model/fr/5x5.jpg",
        6: "./model/fr/6x5.jpg",
        7: "./model/fr/7x5.jpg",
        8: "./model/fr/8x5.jpg",
        9: "./model/fr/9x5.jpg",
        10: "./model/fr/10x5.jpg",
        11: "./model/fr/11x5.jpg",
        12: "./model/fr/12x5.jpg",
        13: "./model/fr/13x5.jpg",
        14: "./model/fr/14x5.jpg",
        15: "./model/fr/15x5.jpg",
        16: "./model/fr/16x5.jpg",
        17: "./model/fr/17x5.jpg",
        18: "./model/fr/18x5.jpg",
        19: "./model/fr/19x5.jpg",
        20: "./model/fr/20x5.jpg",
    }
    return switcher.get(argument)

def SwitchArThreeChoices(argument):
    switcher = {
        5: "./model/ar/ar5x3.jpg",
        6: "./model/ar/ar6x3.jpg",
        7: "./model/ar/ar7x3.jpg",
        8: "./model/ar/ar8x3.jpg",
        9: "./model/ar/ar9x3.jpg",
        10: "./model/ar/ar10x3.jpg",
        11: "./model/ar/ar11x3.jpg",
        12: "./model/ar/ar12x3.jpg",
        13: "./model/ar/ar13x3.jpg",
        14: "./model/ar/ar14x3.jpg",
        15: "./model/ar/ar15x3.jpg",
        16: "./model/ar/ar16x3.jpg",
        17: "./model/ar/ar17x3.jpg",
        18: "./model/ar/ar18x3.jpg",
        19: "./model/ar/ar19x3.jpg",
        20: "./model/ar/ar20x3.jpg",
    }
    return switcher.get(argument)

def SwitchArFourChoices(argument):
    switcher = {
        5: "./model/ar/ar5x4.jpg",
        6: "./model/ar/ar6x4.jpg",
        7: "./model/ar/ar7x4.jpg",
        8: "./model/ar/ar8x4.jpg",
        9: "./model/ar/ar9x4.jpg",
        10: "./model/ar/ar10x4.jpg",
        11: "./model/ar/ar11x4.jpg",
        12: "./model/ar/ar12x4.jpg",
        13: "./model/ar/ar13x4.jpg",
        14: "./model/ar/ar14x4.jpg",
        15: "./model/ar/ar15x4.jpg",
        16: "./model/ar/ar16x4.jpg",
        17: "./model/ar/ar17x4.jpg",
        18: "./model/ar/ar18x4.jpg",
        19: "./model/ar/ar19x4.jpg",
        20: "./model/ar/ar20x4.jpg",
    }
    return switcher.get(argument)

def SwitchArFiveChoices(argument):
    switcher = {
        5: "./model/ar/ar5x5.jpg",
        6: "./model/ar/ar6x5.jpg",
        7: "./model/ar/ar7x5.jpg",
        8: "./model/ar/ar8x5.jpg",
        9: "./model/ar/ar9x5.jpg",
        10: "./model/ar/ar10x5.jpg",
        11: "./model/ar/ar11x5.jpg",
        12: "./model/ar/ar12x5.jpg",
        13: "./model/ar/ar13x5.jpg",
        14: "./model/ar/ar14x5.jpg",
        15: "./model/ar/ar15x5.jpg",
        16: "./model/ar/ar16x5.jpg",
        17: "./model/ar/ar17x5.jpg",
        18: "./model/ar/ar18x5.jpg",
        19: "./model/ar/ar19x5.jpg",
        20: "./model/ar/ar20x5.jpg",
    }
    return switcher.get(argument)

def loadAnswerSheet(questions, choices, lang):
    sheet = str
    if lang == 'fr' or lang == 'en' or lang == 'francais' or lang == 'français':
        if choices == 3:
            for x in r:
                if questions == x:
                    sheet = SwitchFrThreeChoices(x)
        elif choices == 4:
            for x in r:
                if questions == x:
                    sheet = SwitchFrFourChoices(x)
        elif choices == 5:
            for x in r:
                if questions == x:
                    sheet = SwitchFrFiveChoices(x)
    elif lang == 'ar' or lang == 'arabic' or lang == 'Arabe' or lang == 'arabe' or lang == 'العربية':
        if choices == 3:
            for x in r:
                if questions == x:
                    sheet = SwitchArThreeChoices(x)
        elif choices == 4:
            for x in r:
                if questions == x:
                    sheet = SwitchArFourChoices(x)
        elif choices == 5:
            for x in r:
                if questions == x:
                    sheet = SwitchArFiveChoices(x)
    return sheet

def count_stdnts(workbook):
    wb = opxl.load_workbook(workbook)
    sh1 = wb['NotesCC']
    v = sh1['D57'].value
    number_of_students = 0
    names_column = sh1['D18':'D180']
    for cell in names_column:
        for x in cell:
            if x.value != None:
                number_of_students += 1
    wb.close()
    return number_of_students

def loadstdntinfo(workbook, number_of_students):
    global num, academie, level, semester, session, _class, direction, subject, school, teacher
    wb = opxl.load_workbook(workbook)
    sh1 = wb['NotesCC']
    names = []
    massar_id = []
    ordinal_number = []

    _class = re.sub(r'\W+', ' ', sh1['I9'].value)  # extraire le nom du classe
    academie = re.sub(r'\W+', ' ', sh1['D7'].value) # extraire le nom de l'académie
    level = re.sub(r'\W+', ' ', sh1['D9'].value)  # extraire le niveau scolaire
    semester = re.sub(r'\W+', ' ', sh1['D11'].value)  # extraire la semester (1 ou 2)
    session = re.sub(r'\W+', ' ', sh1['D13'].value)  # extraire la session
    direction = re.sub(r'\W+', ' ', sh1['I7'].value)  # extraire le nom de direction
    subject = re.sub(r'\W+', ' ', sh1['O11'].value)  # extraire le sujet
    school = re.sub(r'\W+', ' ', sh1['O7'].value)  # extraire le nom de l'école
    teacher = re.sub(r'\W+', ' ', sh1['O9'].value)  # extraire le nom de l'enseignant

    # extraire les noms des etudiants
    names_column = sh1['D18':f'D{18 + number_of_students - 1}']
    for cell in names_column:
        for x in cell:
            names.append(x.value)

    # extraire les identifiants Massar
    massar_column = sh1['C18':f'C{18 + number_of_students - 1}']
    for cell in massar_column:
        for x in cell:
            massar_id.append(x.value)

    for x in range(1, len(names) + 1):
        ordinal_number.append(x)

    if len(names) == len(massar_id) == len(ordinal_number):
        wb.close()
        num = len(names)
        return ordinal_number, names, massar_id, _class, num
    else:
        wb.close()
        return -1

def genQR(order, questions, choices, names, massar_id, _class, num):
    qrFilename = []
    for x in range(0, num):
        qr1 = qr.QRCode(
            error_correction=qr.constants.ERROR_CORRECT_H,
            box_size=40,
            border=4,
        )
        # transliteration
        t1 = tl.only_roman_chars(names[x])
        t2 = tl.only_roman_chars(_class)

        if t1 == False and t2 == False:
            n = tl.transString(names[x], t1)
            c = tl.transString(_class, t2)
            b = 'Both Tra'
            data = f"{order[x]},{n},{massar_id[x]},{questions},{choices},{c},{b}"
        elif t1 == False:
            n = tl.transString(names[x], t1)
            b = 'Name Tra'
            data = f"{order[x]},{n},{massar_id[x]},{questions},{choices},{_class},{b}"
        elif t2 == False:
            c = tl.transString(_class, t2)
            b = 'Classe Tra'
            data = f"{order[x]},{names[x]},{massar_id[x]},{questions},{choices},{c},{b}"
        else:
            data = f"{order[x]},{names[x]},{massar_id[x]},{questions},{choices},{_class}"

        qr1.add_data(data, optimize=True)
        qr1.make(fit=True)
        jpg = qr1.make_image()
        i = 1
        while os.path.exists("./qr/code%s.jpg" % i):
            i += 1
        fileName = ("./qr/code%s.jpg" % i)
        jpg.save(fileName)
        qrFilename.append(fileName)
    return qrFilename

def merge(QR, sheet):
    sheet = Image.open(sheet)
    sheetFileName = []
    for x in range(0, len(QR)):
        i = 1
        while os.path.exists("./sh/sheet%s.jpg" % i):
            i += 1
        fileName = ("./sh/sheet%s.jpg" % i)
        sheetFileName.append(fileName)
        code = Image.open(QR[x]).resize((285, 285))
        sheet.paste(code, (918, 640))
        sheet.save(fileName)
    return sheetFileName

def gentQR(q, c, c1, c2, c3, nbrc):
    qr2 = qr.QRCode(
        error_correction=qr.constants.ERROR_CORRECT_H,
        box_size=40,
        border=4,
    )
    g = [school, _class, teacher, subject, level, semester, direction, academie]
    v = []
    for y in g:
        #y = y.translate({ord(c): " " for c in "!@#$%^&*()[]{};:,./<>?\|`~-=_+"})
        v.append(tl.only_roman_chars(y))

    b = 0
    for x in range(0, 7):
        if v[x] == False:
            b = 1 #1
            g[x] = tl.transString(g[x], False)

    if b == 1:
        data = f'{q},{c},{g[0]},{g[1]},{g[2]},{g[3]},{g[4]},{g[5]},{g[6]},{g[7]},{b},{nbrc},{c1},{c2},{c3}'
                          #[school, _class, teacher, subject, level, semester, direction, academie]
    else:
        data = f'{q},{c},{g[0]},{g[1]},{g[2]},{g[3]},{g[4]},{g[5]},{g[6]},{g[7]},{b},{nbrc},{c1},{c2},{c3}'
    del v
    del g
    qr2.add_data(data, optimize=True)
    qr2.make(fit=True)
    jpg = qr2.make_image()
    jpg.save('./qr/XXXX.jpg')
    return 0

def teacher_sheet(sheet):
    sheet = Image.open(sheet)
    qr = Image.open('./qr/XXXX.jpg').resize((500, 500))
    header = Image.open('./model/theader.jpg')
    i = 1
    while os.path.exists("./sh/t%s.jpg" % i):
        i += 1
    fileName = ("./sh/t%s.jpg" % i)
    sheet.paste(header, (0, 0))
    sheet.paste(qr, (810, 980))
    sheet.save(fileName)
    try:
        os.remove('./qr/XXXX.jpg')
    except:
        return fileName
    return fileName

def add_header_text(sheetFileName, names, order):
    fontsize = 20
    fontsize2 = 25
    regular = ImageFont.truetype('./fonts/font.ttf', fontsize)
    bold = ImageFont.truetype('./fonts/ArialTh.ttf', fontsize2)
    big = ImageFont.truetype('./fonts/ArialTh.ttf', 40)
    x = 0
    list = []

    for x in range(0, len(sheetFileName)):
        i = 0
        while os.path.exists("./sh/sh%s.jpg" % i):
            i += 1
        fileName = ("./sh/sh%s.jpg" % i)
        list.append(fileName)
        path = str(sheetFileName[x])
        im = Image.open(path)
        d1 = ImageDraw.Draw(im)

        name = f'{names[x]}'
        name = arabic_reshaper.reshape(name)
        name = get_display(name)

        classh = f'{_class}'

        semesterh = semester
        semesterh = arabic_reshaper.reshape(semesterh)
        semesterh = get_display(semesterh)

        sessionh = session
        ordinal = str(order[x])

        levelh = level
        levelh = arabic_reshaper.reshape(levelh)
        levelh = get_display(levelh)

        academieh = academie
        academieh = arabic_reshaper.reshape(academieh)
        academieh = get_display(academieh)

        directionh = direction
        directionh = arabic_reshaper.reshape(directionh)
        directionh = get_display(directionh)

        schoolh = school
        schoolh = arabic_reshaper.reshape(schoolh)
        schoolh = get_display(schoolh)

        teacherh = teacher
        teacherh = arabic_reshaper.reshape(teacherh)
        teacherh = get_display(teacherh)

        subjecth = subject
        subjecth = arabic_reshaper.reshape(subjecth)
        subjecth = get_display(subjecth)

        d1.text((1060, 20), name, font=regular, fill=(0, 0, 0), align="R")
        d1.text((1200, 80), classh, font=bold, fill=(0, 0, 0))
        d1.text((1130, 122), semesterh, font=regular, fill=(0, 0, 0))
        d1.text((1100, 182), sessionh, font=bold, fill=(0, 0, 0))
        d1.text((700, 182), ordinal, font=big, fill=(0, 0, 0))
        d1.text((1010, 224), levelh, font=regular, fill=(0, 0, 0))
        d1.text((200, 20), academieh, font=regular, fill=(0, 0, 0))
        d1.text((110, 70), directionh, font=regular, fill=(0, 0, 0))
        d1.text((200, 122), schoolh, font=regular, fill=(0, 0, 0))
        d1.text((190, 172), teacherh, font=regular, fill=(0, 0, 0))
        d1.text((190, 224), subjecth, font=regular, fill=(0, 0, 0))
        im.save(fileName)
    return list

def genPDF(sheetFileName, rep):
    today = datetime.now()
    today = today.strftime("%d%m%Y")
    filename = f"{rep}/Exam_{_class}_{today}.pdf"
    with open(filename, "wb") as f:
        f.write(img2pdf.convert(sheetFileName))

def clean(qr, sheet, header_sheet):
    for f in qr:
        os.remove(f)
    for x in sheet:
        os.remove(x)
    for x in header_sheet:
        os.remove(x)

def load_chapters(guicstring):
    try:
        c = guicstring.split('*')
    except:
        chapters = None
        return chapters
    chapters = []

    for element in c:
        chapters.append(element)

    return chapters


    #ch1_title, ch1_questions, ch2_title, ch2_questions, ch3_title, ch3_questions, ch4_title, ch4_questions

def generateExam(questions, choices, workbook, lang, rep, c1, c2, c3, nbrc):
    sheet = loadAnswerSheet(questions, choices, lang)
    number_of_students = count_stdnts(workbook)
    order, names, massar_id, _class, num= loadstdntinfo(workbook, number_of_students)
    gentQR(questions, choices, c1,c2,c3,nbrc)
    l = teacher_sheet(sheet)
    QR = genQR(order, questions, choices, names, massar_id, _class, num)
    imagelist = merge(QR, sheet)
    imagelist2 = add_header_text(imagelist, names, order)
    imagelist2.insert(0, l)
    genPDF(imagelist2, rep)
    clean(QR, imagelist2, imagelist)
