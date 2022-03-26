import cv2
import numpy as np
import utils
import os
import csv
from shutil import copyfile
from pyzbar.pyzbar import decode
from PIL import Image
import transliteration as tl
import codecs


# why not thread windows
def genAns(imga):
    img = cv2.imread(imga)
    widthImg = img.shape[1]
    heightImg = img.shape[0]
    d = cv2.QRCodeDetector()
    values, pp, ss = d.detectAndDecode(img)
    if len(values) < 1:
        del pp
        del ss
        values = decode(Image.open(imga))
        if len(values) < 1:
            return 1
        values = values[0].data
        values = codecs.decode(values)
        split = values.split(',')
        split[10] = int(split[10])
        if len(split) == 15 and split[10] == 1:
            # [q, c, school, _class, teacher, subject, level, semester, direction, academie]
            questions = int(split[0])
            choices = int(split[1])
            school = tl.transString(split[2], True)
            classe = split[3]
            teacher = tl.transString(split[4], True)
            subject = tl.transString(split[5], True)
            level = tl.transString(split[6], True)
            semester = tl.transString(split[7], True)
            direction = tl.transString(split[8], True)
            academie = tl.transString(split[9], True)
            nbr = int(split[11])
            ch1 = split[12]
            ch2 = split[13]
            ch3 = split[14]
            del split, values
        elif len(split) == 15 and split[10] == 0:
            questions = int(split[0])
            choices = int(split[1])
            school = split[2]
            classe = split[3]
            teacher = split[4]
            subject = split[5]
            level = split[6]
            semester = split[7]
            direction = split[8]
            academie = split[9]
            nbr = int(split[11])
            ch1 = split[12]
            ch2 = split[13]
            ch3 = split[14]
            del split, values
    else:
        del pp
        del ss
        split = values.split(',')
        split[10] = int(split[10])
        if len(split) == 15 and split[10] == 1:
            # [q, c, school, _class, teacher, subject, level, semester, direction, academie]
            questions = int(split[0])
            choices = int(split[1])
            school = tl.transString(split[2], True)
            classe = split[3]
            teacher = tl.transString(split[4], True)
            subject = tl.transString(split[5], True)
            level = tl.transString(split[6], True)
            semester = tl.transString(split[7], True)
            direction = tl.transString(split[8], True)
            academie = tl.transString(split[9], True)
            nbr = int(split[11])
            ch1 = split[12]
            ch2 = split[13]
            ch3 = split[14]
            del split, values
        elif len(split) == 15 and split[10] == 0:
            questions = int(split[0])
            choices = int(split[1])
            school = split[2]
            classe = split[3]
            teacher = split[4]
            subject = split[5]
            level = split[6]
            semester = split[7]
            direction = split[8]
            academie = split[9]
            nbr = int(split[11])
            ch1 = split[12]
            ch2 = split[13]
            ch3 = split[14]
            del split, values

    imgContours = img.copy()
    imgBiggestContours = img.copy()

    # Prétraitement d’image
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # grayscale
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1) # blur
    imgCanny = cv2.Canny(imgBlur, 10, 50) # canny

    # Detection des Contours
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    bb = cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 2)

    # Trouver les rectangles
    rectCon = utils.rectContours(contours)
    biggestContour = utils.getCornerPoints(rectCon[0]) #rectangle de marquage
    gradePoints = utils.getCornerPoints(rectCon[1])

    if biggestContour.size != 0 and gradePoints.size != 0:
        cv2.drawContours(imgBiggestContours, biggestContour, -1, (0, 255, 0), 20)
        cv2.drawContours(imgBiggestContours, gradePoints, -5, (0, 0, 255), 20)
        biggestContour = utils.reorder(biggestContour)
        gradePoints = utils.reorder(gradePoints)

        pt1 = np.float32(biggestContour)
        pt2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
        matrix = cv2.getPerspectiveTransform(pt1, pt2)
        imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

        ptg1 = np.float32(gradePoints)
        ptg2 = np.float32([[0, 0], [325, 0], [0, 150], [325, 150]])
        matrixG = cv2.getPerspectiveTransform(ptg1, ptg2)
        imgGradeDisplay = cv2.warpPerspective(img, matrixG, (325, 150))

        # apply threshold
        imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
        imgThresh = cv2.threshold(imgWarpGray, 200, 255, cv2.THRESH_BINARY_INV)[1]
        boxes = utils.splitBoxes(imgThresh, choices, questions)

        # Compter les pixels non nuls et détecter les cellules vides et pleines

        myPixelVal = np.zeros((questions, choices))
        empty = np.zeros((questions, choices))
        Full = np.zeros((questions, choices)) #creation d une liste bidimensionnel
        countC = 0
        countR = 0
        for image in boxes:
            totalPixel = cv2.countNonZero(image)
            myPixelVal[countR][countC] = totalPixel
            if myPixelVal[countR][countC] < image.shape[0] * image.shape[1] * 40 / 100: # 30%
                empty[countR][countC] = 1
                Full[countR][countC] = 0
            else:
                empty[countR][countC] = 0
                Full[countR][countC] = 1
            countC += 1
            if countC == choices:
                countR += 1
                countC = 0
        return Full, school, classe, teacher, subject, level, semester, direction, academie, nbr, ch1, ch2, ch3
    else:
        return 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

def correctExam(imgx, ans, bareme, rep, nbrc, ch1, ch2, ch3):
    img = cv2.imread(imgx)
    d = cv2.QRCodeDetector()
    values, pp, ss = d.detectAndDecode(img)

    if len(values) < 1:
        del pp
        del ss
        values = decode(Image.open(imgx))
        if len(values) < 1:
            return 5
        values = values[0].data
        values = codecs.decode(values)
        split = values.split(',')
        if len(split) > 6:
            if split[6] == 'Name Tra':
                name = tl.transString(split[1], True)  # !!!!!!!
                order = split[0]
                massar = split[2]
                questions = int(split[3])
                choices = int(split[4])
                classe = split[5]
                nfo = [order, name, massar, classe]
            elif split[6] == 'Classe Tra':
                classe = tl.transString(split[5], True)  # !!!!!!!
                name = split[1]
                order = split[0]
                massar = split[2]
                questions = int(split[3])
                choices = int(split[4])
                nfo = [order, name, massar, classe]
            elif split[6] == 'Both Tra':
                classe = tl.transString(split[5], True)
                name = tl.transString(split[1], True)
                order = split[0]
                massar = split[2]
                questions = int(split[3])
                choices = int(split[4])
                nfo = [order, name, massar, classe]

    if len(values) > 1:
        split = values.split(',')
        if len(split) > 6:
            if split[6] == 'Name Tra':
                name = tl.transString(split[1], True)  # !!!!!!!
                order = split[0]
                massar = split[2]
                questions = int(split[3])
                choices = int(split[4])
                classe = split[5]
                nfo = [order, name, massar, classe]
            elif split[6] == 'Classe Tra':
                classe = tl.transString(split[5], True)  # !!!!!!!
                name = split[1]
                order = split[0]
                massar = split[2]
                questions = int(split[3])
                choices = int(split[4])
                nfo = [order, name, massar, classe]
            elif split[6] == 'Both Tra':
                classe = tl.transString(split[5], True)
                name = tl.transString(split[1], True)
                order = split[0]
                massar = split[2]
                questions = int(split[3])
                choices = int(split[4])
                nfo = [order, name, massar, classe]
        else:
            order = split[0]
            name = split[1]
            massar = split[2]
            questions = int(split[3])
            choices = int(split[4])
            classe = split[5]
            nfo = [order, name, massar, classe]

    if bareme == None:
        bareme = []
        for x in range(0, questions):
            bareme.append(1)

    nchapters = int(nbrc)
    chap1 = ch1
    chap2 = ch2
    chap3 = ch3

    if nbrc == 0:
        chap1 = None
        chap2 = None
        chap3 = None
    else:
        if chap1 == 'None':
            chap1 = None
        if chap2 == 'None':
            chap2 = None
        if chap3 == 'None':
            chap3 = None

    a = ((chap1 is not None) and (chap2 is None) and (chap3 is None) is True)
    b = ((chap1 and chap2 is not None) and (chap3 is None)) is True
    c = ((chap1 and chap2 and chap3) is not None) is True

    grading = int
    score = float
    sumscore = float

    widthImg = img.shape[1]
    heightImg = img.shape[0]
    imgContours = img.copy()
    imgBiggestContours = img.copy()
    nbrChoices = np.sum(ans, axis=1)
    nbrChoices = nbrChoices.tolist()

    # Prétraitement d’image
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # grayscale
    imgBlur = cv2.GaussianBlur(imgGray, (5, 5), 1)  # blur
    imgCanny = cv2.Canny(imgBlur, 10, 50)  # canny

    # Detection des Contours
    contours, hierarchy = cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    bb = cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 2)
    # Trouver les rectangles
    rectCon = utils.rectContours(contours)
    biggestContour = utils.getCornerPoints(rectCon[0])  # rectangle de marquage
    gradePoints = utils.getCornerPoints(rectCon[1])
    qrPoints = utils.getCornerPoints(rectCon[2])  # rectangle de QR

    if biggestContour.size != 0 and gradePoints.size != 0:
        cv2.drawContours(imgBiggestContours, biggestContour, -1, (0, 255, 0), 20)
        cv2.drawContours(imgBiggestContours, gradePoints, -5, (0, 0, 255), 20)
        cv2.drawContours(imgBiggestContours, qrPoints, -5, (0, 0, 255), 20)
        biggestContour = utils.reorder(biggestContour)
        gradePoints = utils.reorder(gradePoints)
        qrPoints = utils.reorder(qrPoints)

        pt1 = np.float32(biggestContour)
        pt2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
        matrix = cv2.getPerspectiveTransform(pt1, pt2)
        imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))

        ptg1 = np.float32(gradePoints)
        ptg2 = np.float32([[0, 0], [325, 0], [0, 150], [325, 150]])
        matrixG = cv2.getPerspectiveTransform(ptg1, ptg2)
        imgGradeDisplay = cv2.warpPerspective(img, matrixG, (325, 150))


        # apply threshold
        imgWarpGray = cv2.cvtColor(imgWarpColored, cv2.COLOR_BGR2GRAY)
        imgThresh = cv2.threshold(imgWarpGray, 200, 255, cv2.THRESH_BINARY_INV)[1]
        boxes = utils.splitBoxes(imgThresh, choices, questions)

        # Compter les pixels non nuls et détecter les cellules vides et pleines

        myPixelVal = np.zeros((questions, choices))
        empty = np.zeros((questions, choices))
        Full = np.zeros((questions, choices))  # creation d une liste bidimensionnel
        countC = 0
        countR = 0
        for image in boxes:
            totalPixel = cv2.countNonZero(image)
            myPixelVal[countR][countC] = totalPixel
            if myPixelVal[countR][countC] < image.shape[0] * image.shape[1] * 40 / 100:  # 30%
                empty[countR][countC] = 1
                Full[countR][countC] = 0
            else:
                empty[countR][countC] = 0
                Full[countR][countC] = 1
            countC += 1
            if countC == choices:
                countR += 1
                countC = 0

        # Grading
        grading = []
        score = []
        gradingType = 1  # 0==moderate 1==strict

        # Strict Grading
        if gradingType == 1:
            grading = (ans == Full).all(axis=1)
            for item in range(questions):
                if grading[item] == True:
                    score.append(bareme[item])
                else:
                    score.append(0)
            sumscore = sum(score)

        # Moderate Grading
        elif gradingType == 0:
            grading = np.zeros((questions, choices))
            score = []
            for j in range(questions):
                for i in range(choices):
                    if ans[j][i] == Full[j][i] and Full[j][i] and empty[j][i] == 0:
                        grading[j][i] = bareme[j] / nbrChoices[j]
                    else:
                        grading[j][i] = 0
            score = np.sum(grading, axis=1)
            sumscore = float(sum(score))

        if nchapters == 1:
            m1 = ch1.split(':')

            m1[1] = int(m1[1])

            if int(m1[1]) > questions:
                pass

            hx = score

            ch1_g = hx[:int(m1[1])]
            ch1_s = sum(ch1_g)

            nfo.append(ch1_s)
            nfo.append(sumscore)

            headers = ["Numéro d'ordre", 'Nom Complet','Code Massar','Classe',f'{m1[0]}','Note']

            if os.path.isdir(rep):
                path = f"{rep}/résultats_{classe}_1c.csv"
            else:
                os.mkdir(rep)
                path = f"{rep}/résultats_{classe}_1c.csv"

            if not os.path.isfile(path):
                open(path, 'a').close()

            with open(path, "r", encoding="utf-8", newline='') as fp:
                g = fp.readline()
                g = len(g)

            with open(path, "a", encoding="utf-8", newline='') as fp:
                wr = csv.writer(fp, dialect='excel')
                if g != 0:
                    wr.writerow(nfo)
                else:
                    wr.writerow(headers)
                    wr.writerow(nfo)

            s_bareme = sum(bareme)

            return path, s_bareme

        elif nchapters == 2:
            m1 = ch1.split(':')
            m2 = ch2.split(':')

            m1[1] = int(m1[1])
            m2[1] = int(m2[1])

            if (m1[1] + m2[1]) > questions:
                pass

            hx = score

            ch1_g = hx[:int(m1[1])]
            ch1_s = sum(ch1_g)
            hx = hx[int(m1[1]):]

            ch2_g = hx[:int(m2[1])]
            ch2_s = sum(ch2_g)
            del hx

            nfo.append(ch1_s)
            nfo.append(ch2_s)
            nfo.append(sumscore)

            headers = ["Numéro d'ordre", 'Nom Complet', 'Code Massar', 'Classe', f'{m1[0]}', f'{m2[0]}', 'Note']

            if os.path.isdir(rep):
                path = f"{rep}/résultats_{classe}_2c.csv"
            else:
                os.mkdir(rep)
                path = f"{rep}/résultats_{classe}_2c.csv"

            if not os.path.isfile(path):
                open(path, 'a').close()

            with open(path, "r", encoding="utf-8", newline='') as fp:
                g = fp.readline()
                g = len(g)

            with open(path, "a", encoding="utf-8", newline='') as fp:
                wr = csv.writer(fp, dialect='excel')
                if g != 0:
                    wr.writerow(nfo)
                else:
                    wr.writerow(headers)
                    wr.writerow(nfo)

            s_bareme = sum(bareme)

            return path, s_bareme

        elif nchapters == 3:
            m1 = ch1.split(':')
            m2 = ch2.split(':')
            m3 = ch3.split(':')

            m1[1] = int(m1[1])
            m2[1] = int(m2[1])
            m3[1] = int(m3[1])

            if (m1[1] + m2[1] + m3[1]) > questions:
                pass

            hx = score

            ch1_g = hx[:int(m1[1])]
            ch1_s = sum(ch1_g)
            hx = hx[int(m1[1]):]

            ch2_g = hx[:int(m2[1])]
            ch2_s = sum(ch2_g)
            hx = hx[int(m2[1]):]

            ch3_g = hx[:int(m3[1])]
            ch3_s = sum(ch3_g)
            del hx

            nfo.append(ch1_s)
            nfo.append(ch2_s)
            nfo.append(ch3_s)
            nfo.append(sumscore)

            headers = ["Numéro d'ordre", 'Nom Complet', 'Code Massar', 'Classe', f'{m1[0]}', f'{m2[0]}',f'{m3[0]}', 'Note']

            if os.path.isdir(rep):
                path = f"{rep}/résultats_{classe}_3c.csv"
            else:
                os.mkdir(rep)
                path = f"{rep}/résultats_{classe}_3c.csv"

            if not os.path.isfile(path):
                open(path, 'a').close()

            with open(path, "r", encoding="utf-8", newline='') as fp:
                g = fp.readline()
                g = len(g)

            with open(path, "a", encoding="utf-8", newline='') as fp:
                wr = csv.writer(fp, dialect='excel')
                if g != 0:
                    wr.writerow(nfo)
                else:
                    wr.writerow(headers)
                    wr.writerow(nfo)

            s_bareme = sum(bareme)

            return path, s_bareme

        elif nchapters == 0:
            nfo.append(sumscore)
            if os.path.isdir(rep):
                path = f"{rep}/résultats_{classe}.csv"
            else:
                os.mkdir(rep)
                path = f"{rep}/résultats_{classe}.csv"

            if not os.path.isfile(path):
                copyfile('./src/output.csv', path)

            with open(path, "a", encoding="utf-8", newline='\n') as fp:
                wr = csv.writer(fp, dialect='excel')
                wr.writerow(nfo)

            s_bareme = sum(bareme)

            return path, s_bareme
    else:
        return 5