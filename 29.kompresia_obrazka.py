info = open('kompresia_obrazka_1.txt', 'r')

sirka, vyska = info.readline().strip().split()
sirka, vyska = int(sirka), int(vyska)

print('Sirka obrazka -', str(sirka,),', Vyska obrazka -',str(vyska),', Pocet bodov -',str(sirka*vyska))

def spracuj_riadok(riadok):
    kompresia = '0 '
    pocet = 0
    nula = True
    for znak in riadok.strip():
        odstup = len(str(pocet)) + 1
        if nula and int(znak) == 0:
            pocet += 1
            kompresia = kompresia[:-odstup] + str(pocet) + ' '
        elif not nula and int(znak) == 1:
            pocet += 1
            kompresia = kompresia[:-odstup] + str(pocet) + ' '
        elif not nula and int(znak) == 0:
            kompresia = kompresia + '1 '
            pocet = 1
            nula = True
        elif nula and int(znak) == 1:
            kompresia = kompresia + '1 '
            pocet = 1
            nula = False
    return kompresia.strip()

vystup = open('kompresia_obrazka_vystup.txt', 'w')
vystup.write(str(sirka)+' '+str(vyska)+'\n')
for riadok in info:
    vystup.write(spracuj_riadok(riadok)+'\n')
    print(spracuj_riadok(riadok))
info.close()
vystup.close()