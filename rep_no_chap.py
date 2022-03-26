import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import pandas as pd
import fsspec
import pandas.plotting._matplotlib
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image, ImageFont, ImageDraw
import img2pdf
import os
import matplotlib.backends.backend_tkagg
matplotlib.use('tkagg')


def percentage(part, whole):
    percentage = 100 * float(part) / float(whole)
    return str(percentage) + "%"

def no_chapters(path, rep, sbareme, _class, semester, level, academie, direction, school, subject, teacher):
    df = pd.read_csv(path, delimiter=',')
    classe = df['Classe'].iat[0]
    del df['Code Massar']
    del df["Numéro d'ordre"]
    del df['Classe']
    df = df.sort_values('Note', ascending=True)
    df = df.reset_index(drop=True)
    nbr_stdnts = len(df['Note'])

    a3la = float(df['Note'].iat[-1])
    adna = float(df['Note'][0])
    mo3adal_classe = sum(df['Note']) / nbr_stdnts
    mo3adal_classe = float("{:.2f}".format(mo3adal_classe))

    first_n = float(df['Note'].iat[-1])
    first_name = arabic_reshaper.reshape(df['Nom Complet'].iat[-1])
    first_name = get_display(first_name)

    scnd_n = float(df['Note'].iat[-2])
    scnd_name = arabic_reshaper.reshape(df['Nom Complet'].iat[-2])
    scnd_name = get_display(scnd_name)

    third_n = float(df['Note'].iat[-3])
    third_name = arabic_reshaper.reshape(df['Nom Complet'].iat[-3])
    third_name = get_display(third_name)

    h = []
    for value in df['Nom Complet']:
        g = arabic_reshaper.reshape(value)
        ar = get_display(g)
        h.append(ar)
    del df['Nom Complet']
    df['Nom Complet'] = h

    df_top = df.columns

    # number of occurences
    hh = df['Note'].value_counts().sort_values(ascending=True)
    ax = hh.plot.bar(title='Un titre ici', figsize=(13, 7), edgecolor="#000000")
    ax.grid(axis='y')
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    occpath = './report/3c/5.png'
    plt.savefig(occpath, dpi=120, bbox_inches='tight')
    del hh
    plt.close()

    # categories
    notes = df['Note']
    box1 = []
    box2 = []
    box3 = []
    box4 = []

    mo3adal = 0
    n_mo3adal = 0

    for item in notes:
        if item >= (sbareme * 0.5):
            mo3adal += 1
        if item < (sbareme * 0.5):
            n_mo3adal += 1
        if item <= (sbareme * 0.25):
            box1.append(item)
        elif (sbareme * 0.5) >= item > (sbareme * 0.25):
            box2.append(item)
        elif (sbareme * 0.75) >= item > (sbareme * 0.5):
            box3.append(item)
        elif item > (sbareme * 0.75):
            box4.append(item)

    bbox = [len(box1), len(box2), len(box3), len(box4)]
    labels = ['0%<<n<<25%', '25%<<n<<50%', '50%<<n<<75%', '75%<<n<<100%']
    colors = ['#FF0000', '#F08080', '#0DA89F', '#00766F', ]
    explode = [0, 0, 0, 0.1]
    zero_index = []
    for element in bbox:
        if element == 0:
            m = bbox.index(element)
            zero_index.append(m)
            del labels[m]
            del colors[m]
            del explode[m]

    for element in zero_index:
        del bbox[element]

    plt.title('Classification des etudiant selon leurs note')
    plt.pie(bbox, labels=labels, colors=colors, wedgeprops={'edgecolor': '#ffffff'}, autopct='%1.1f%%',
            explode=explode, startangle=90)
    piepath = './report/3c/6.png'
    plt.savefig(piepath, dpi=160, bbox_inches='tight')
    plt.close()

    # horizontal bar chart
    plt.figure(1)
    ax = df.plot.barh(x='Nom Complet', y='Note', rot=1, align='edge', width=0.5, figsize=(10, 15),
                      color='#0DA89F', title='Un titre ici 2', edgecolor="#000000")
    ax.grid(axis='x')
    #ax.xaxis.set_major_locator(MaxNLocator(integer=True)) #
    plt.xticks(rotation=45, fontsize=12) #
    plt.yticks(fontsize=12) #
    plt.ylabel(None)
    mainbarpath = './report/3c/1.png'
    plt.savefig(mainbarpath, dpi=120, bbox_inches='tight')
    plt.close()

    df = df.sort_values(df_top[0], ascending=True)
    df = df.reset_index(drop=True)

    # generating the report
    fontsize = 25
    numbers = 50
    regular = ImageFont.truetype('./fonts/font.ttf', fontsize)
    latin = ImageFont.truetype('./fonts/Kanit-Regular.ttf', fontsize)
    numeral = ImageFont.truetype('./fonts/AnonymousPro-Regular.ttf', numbers)

    # first page
    i1 = Image.open('./model/report/1.png')
    classh = f'{_class}'
    semesterh = semester
    semesterh = arabic_reshaper.reshape(semesterh)
    semesterh = get_display(semesterh)
    levelh = level
    levelh = arabic_reshaper.reshape(levelh)
    levelh = get_display(levelh)
    academieh = arabic_reshaper.reshape(academie)
    academieh = get_display(academieh)
    directionh = arabic_reshaper.reshape(direction)
    directionh = get_display(directionh)
    schoolh = arabic_reshaper.reshape(school)
    schoolh = get_display(schoolh)
    teacherh = arabic_reshaper.reshape(teacher)
    teacherh = get_display(teacherh)
    subjecth = arabic_reshaper.reshape(subject)
    subjecth = get_display(subjecth)
    d1 = ImageDraw.Draw(i1)
    d1.text((1184, 463), classh, font=latin, fill=(0, 0, 0))
    d1.text((204, 539), semesterh, font=regular, fill=(0, 0, 0))
    d1.text((161, 129), levelh, font=regular, fill=(0, 0, 0))
    d1.text((1078, 48), academieh, font=regular, fill=(0, 0, 0))
    d1.text((987,129), directionh, font=regular, fill=(0, 0, 0))
    d1.text((106, 45), schoolh, font=regular, fill=(0, 0, 0))
    d1.text((1100, 540), teacherh, font=regular, fill=(0, 0, 0))
    d1.text((135, 457), subjecth, font=regular, fill=(0, 0, 0))
    d1.text((1208, 855), str(nbr_stdnts), font=numeral, fill=(0, 0, 0))
    d1.text((979, 855,), str(mo3adal), font=numeral, fill=(0, 0, 0))
    d1.text((753, 855), str(n_mo3adal), font=numeral, fill=(0, 0, 0))
    d1.text((500, 855), str(a3la), font=numeral, fill=(0, 0, 0))
    d1.text((310, 855), str(adna), font=numeral, fill=(0, 0, 0))
    d1.text((100, 855), str(mo3adal_classe), font=numeral, fill=(0, 0, 0))
    num = ImageFont.truetype('./fonts/AnonymousPro-Regular.ttf', 45)
    d1.text((541, 1065), first_name, font=regular, fill=(0, 0, 0))
    d1.text((110, 1065), str(first_n), font=num, fill=(0, 0, 0))
    d1.text((541, 1149), scnd_name, font=regular, fill=(0, 0, 0))
    d1.text((110, 1149), str(scnd_n), font=num, fill=(0, 0, 0))
    d1.text((541, 1228), third_name, font=regular, fill=(0, 0, 0))
    d1.text((110, 1228), str(third_n), font=num, fill=(0, 0, 0))

    d1.text((842, 1520), percentage(len(box1), nbr_stdnts), font=numeral, fill=(0, 0, 0))
    d1.text((600, 1520), percentage(len(box2), nbr_stdnts), font=numeral, fill=(0, 0, 0))
    d1.text((361, 1520), percentage(len(box3), nbr_stdnts), font=numeral, fill=(0, 0, 0))
    d1.text((114, 1520), percentage(len(box4), nbr_stdnts), font=numeral, fill=(0, 0, 0))

    d1.text((945, 1743), percentage(mo3adal, nbr_stdnts), font=numeral, fill=(0, 0, 0))
    d1.text((292, 1743), percentage(n_mo3adal, nbr_stdnts), font=numeral, fill=(0, 0, 0))

    paths = ['./sheetz/1.png', './sheetz/2.png', './sheetz/3.png']
    i1.save(paths[0])
    del i1
    del d1

    # second page
    i2 = Image.open('./model/report/2.png')
    occplot = Image.open(occpath)
    pieplot = Image.open(piepath)
    i2.paste(occplot, (80, 271))
    i2.paste(pieplot, (360, 1121))
    i2.save(paths[1])
    del i2
    del occplot
    del pieplot

    # 3rd page
    i3 = Image.open('./model/report/3.png')
    mainplot = Image.open(mainbarpath)
    i3.paste(mainplot, (187, 296))
    i3.save(paths[2])
    del i3
    del mainplot

    i = 1
    paths2 = []
    for element in paths:
        im = Image.open(element)
        rgb_im = im.convert('RGB')
        filename = f'{i}.jpg'
        rgb_im.save(filename, quality=100)
        paths2.append(filename)
        i += 1

    filename = f"{rep}/rapport_{classe}.pdf"
    with open(filename, "wb") as f:
        f.write(img2pdf.convert(paths2))

    try:
        for file in paths:
            os.remove(file)
    except:
        pass

    try:
        for file in paths2:
            os.remove(file)
    except:
        pass
    return 0
