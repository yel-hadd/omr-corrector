import cv2
from pyzbar.pyzbar import decode
from PIL import Image
import transliteration as tl
d = cv2.QRCodeDetector()
import codecs
import os







"""qrx = qrtools.QR()
qrx.decode("sh1.jpg")
print(qrx.data)"""
"""values = decode(Image.open('sh1.jpg'))
decoded = values[0].data


v = codecs.decode(decoded)
print(v)"""


def scan_qr(imgx):
    img = cv2.imread(imgx)
    widthImg = img.shape[1]
    heightImg = img.shape[0]
    d = cv2.QRCodeDetector()
    values, pp, ss = d.detectAndDecode(img)
    if len(values) < 1:
        del pp
        del ss
        values = decode(Image.open(imgx))
        if len(values) < 1:
            return 1
        values = values[0].data
        values = codecs.decode(values)
        split = values.split(',')
        if len(split) == 10 and split[9] == '1':
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
            del split, values
        else:
            questions = split[0]
            choices = split[1]
            school = split[2]
            classe = split[3]
            teacher = split[4]
            subject = split[5]
            level = split[6]
            semester = split[7]
            direction = split[8]
            academie = split[9]
            del split, values
            # ques, choice, school, _class, teacher, subject, level, semester, direction, academie
    else:
        del pp
        del ss
        split = values.split(',')
        if len(split) == 10 and split[9] == '1':
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
            del split, values
        else:
            questions = split[0]
            choices = split[1]
            school = split[2]
            classe = split[3]
            teacher = split[4]
            subject = split[5]
            level = split[6]
            semester = split[7]
            direction = split[8]
            academie = split[9]
            del split, values

    return 0



