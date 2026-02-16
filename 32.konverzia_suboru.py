def spracuj_riadok(vstup):
    pocet = len(vstup)//2
    vystup = ''
    for i in range(pocet):
        odtien = vstup[i*2:i*2+2]
        farba = '0'
        if odtien > '7f':
            farba = '1'
        vystup += farba + ' '
    return vystup + '\n'

subor = open('ciernobiely_obrazok_1.txt', 'r')
konverzia = open('konverzia_suboru_1_vystup.txt', 'w')

sirka, vyska = subor.readline().strip().split()
konverzia.write(sirka+' '+vyska+'\n')
sirka, vyska = int(sirka), int(vyska)

for y in range(vyska):
    konverzia.write(spracuj_riadok(subor.readline()))

subor.close()
konverzia.close()

print("obrazok ma rozmery {}x{} bodov".format(sirka,vyska))
print("obrazok ma tolko pixelov {}".format(sirka*vyska))

""" subor = open('ciernobiely_obrazok_1.txt', 'r')
vystup = open('konverzia_suboru_1_vystup.txt', 'w')

sirka, vyska = subor.readline().strip().split()
vystup.write(sirka+' '+vyska+'\n')
sirka, vyska = int(sirka), int(vyska)

y = 0
for riadok in subor:
    riadok = riadok.strip()
    for i in range(sirka):
        odtien = riadok[i*2:i*2+2]
        farba = '0'
        if odtien > '7f':
            farba = '1'
        vystup.write(farba + ' ')
    vystup.write('\n')
    y += 1
    
subor.close()
vystup.close() """