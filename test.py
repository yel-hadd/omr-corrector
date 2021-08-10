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
    values = decode(Image.open(imgx))
    values = values[0].data
    values = codecs.decode(values)
    split = values.split(',')
    print(split[6])
    return 0

"""    if len(split) > 5:
        if split[5] == 'Name Tra':
            name = tl.transString(split[1], True)  # !!!!!!!
            order = split[0]
            massar = split[2]
            questions = int(split[3])
            choices = int(split[4])
            classe = split[5]
            nfo = [order, name, massar, classe]
        elif split[5] == 'Classe Tra':
            classe = tl.transString(split[5], True)  # !!!!!!!
            name = split[1]
            order = split[0]
            massar = split[2]
            questions = int(split[3])
            choices = int(split[4])
            nfo = [order, name, massar, classe]
        elif split[5] == 'Both Tra':
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
        nfo = [order, name, massar, classe]"""




g = scan_qr('./sh/sh1.jpg')
print(g)

#tl.transString('b$rY', tl.only_roman_chars('b$rY')
