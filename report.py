import pandas as pd
import os
import ntpath

def sort(path):
    g = ntpath.basename(path)
    a = g.split('.')
    a = a[0]
    b = ntpath.split(path)
    df = pd.read_csv(path, delimiter=',')
    g = df.sort_values("Numéro d'ordre")
    del df
    g.to_excel(f"{b[0]}/{a}.xlsx", index=False)
    g.to_csv(path, index=False)
    return 0

def percentage(part, whole):
    percentage = 100 * float(part) / float(whole)
    return str(percentage) + "%"

def gen_report(path, rep, chapters, bareme, _class, semester, level, academie, direction, school, subject, teacher):
    sort(path)

    if chapters == 0:
        from rep_no_chap import no_chapters
        no_chapters(path, rep, bareme, _class, semester, level, academie, direction, school, subject, teacher)
    elif chapters == 1:
        from rep_one_chap import one_chapter
        one_chapter(path, rep, bareme, _class, semester, level, academie, direction, school, subject, teacher)
    elif chapters == 2:
        from rep_two_chap import two_chapters
        two_chapters(path, rep, bareme, _class, semester, level, academie, direction, school, subject, teacher)
    elif chapters == 3:
        from rep_three_chap import three_chapters
        three_chapters(path, rep, bareme, _class, semester, level, academie, direction, school, subject, teacher)
    else:
        from rep_no_chap import no_chapters
        no_chapters(path, rep, bareme, _class, semester, level, academie, direction, school, subject, teacher)

    os.remove(path)
