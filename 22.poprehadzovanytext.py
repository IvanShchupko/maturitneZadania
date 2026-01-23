import random

def pomiesaj(retazec):
    pismenka = list(retazec)
    random.shuffle(pismenka)
    return ''.join(pismenka)

def ocisti_slova(slovo):
    ciste_slovo = ''
    zly_zaciatok = ''
    zly_koniec = ''
    i = 0
    while slovo[i] in vynechat:
        zly_zaciatok += slovo[i]
        i += 1
    while i < len(slovo) and not (slovo[i] in vynechat):
        ciste_slovo += slovo[i]
        i += 1
    zly_koniec = slovo[i:]
    return zly_zaciatok, ciste_slovo, zly_koniec

vynechat = '1234567890!@#$%^&*()_-+=[]{};:"|\<,>.?/`~'

subor1 = open('poprehadzovany_text_vstup2.txt', 'r')
subor2 = open('poprehadzovany_text_vystup2.txt', 'w')

for riadok in subor1:
    print(riadok, end='')
    slova = riadok.strip().split()
    for i in range(len(slova)):
        pred, stred, koniec = ocisti_slova(slova[i])
        if len(stred) > 2:
            stred = stred[0] + pomiesaj(stred[1:-1]) + stred[-1]
        slova[i] = pred + stred + koniec
    riadok = ' '.join(slova) + '\n'
    print(riadok, end='')
    subor2.write(riadok)

subor1.close()
subor2.close()



""" vstup = open('poprehadzovany_text_vstup2.txt')
text = []
for line in vstup:
    text.append(line.strip().split())
vstup.close()

poprehadzovanyText = ''
for riadok in text:
    for slovo in riadok:
        print(slovo)
        odstup = -1
        while ord(slovo[odstup]) < 97 and ord(slovo[odstup]) > 122:
            odstup = odstup - 1
            print(odstup)
        word = slovo[1] + pomiesaj(slovo[1:odstup]) + slovo[odstup]
        poprehadzovanyText = poprehadzovanyText + word
    poprehadzovanyText = poprehadzovanyText + '\n'
print(poprehadzovanyText) """