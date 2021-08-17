import csv


with open('output_3ch.csv', 'r') as csvfile:
    a = csvfile.readline()
    print(len(a))
    """csv_dict = [row for row in csv.DictReader(csvfile)]
    print(len(csv_dict))
    print(csv_dict)
    csvfile.close()"""


"""
FOR GUI Later
    if (ch1_title and ch1_questions) is not None:
        chapters.append(f'{ch1_title}:{ch1_questions}')
    if (ch2_title and ch2_questions) is not None:
        chapters.append(f'{ch2_title}:{ch2_questions}')
    if (ch3_title and ch3_questions) is not None:
        chapters.append(f'{ch3_title}:{ch3_questions}')
    if (ch4_title and ch4_questions) is not None:
        chapters.append(f'{ch4_title}:{ch4_questions}')
"""