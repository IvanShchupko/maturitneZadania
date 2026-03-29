import random as r

s = open("obesenec.txt", "r")
slova = s.readlines()
s.close()

slovo = slova[r.randrange(len(slova))].strip()
uhadnute = "."*len(slovo)

sansa = 10
def hadaj():
    global uhadnute, sansa
    pismeno = input(uhadnute + ': ')
    if pismeno in slovo and pismeno not in uhadnute and len(pismeno)==1:
        nove_uhadnute=''
        for znak in slovo:
            if znak in uhadnute or znak == pismeno:
                nove_uhadnute += znak
            else:
                nove_uhadnute += '.'
        uhadnute = nove_uhadnute
    
    if pismeno not in slovo or len(pismeno) != 1:
        sansa += -1
        print("mate este " + str(sansa) + 'zivotov')
    if uhadnute == slovo:
        print(slovo)
        print("Stihol si")
    elif sansa < 1:
        print("Nestihol si")
    else:
        hadaj()

hadaj()