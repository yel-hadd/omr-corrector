import random

def gencaptcha():
    operations = ['a', 's']
    a = random.randrange(1, 50)
    b = random.randrange(a, 60)
    o = random.choice(operations)
    while o == 's' and 0 > a-b:
        a = random.randrange(20, 50)
        b = random.randrange(1, 20)
    if o == 'a':
        challenge = f'{a}+{b}='
        answer = int(a+b)
        return challenge, answer
    elif o == 's':
        challenge = str(f'{a}-{b}=')
        answer = int(a-b)
        return challenge, answer
