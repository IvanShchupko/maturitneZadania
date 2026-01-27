from random import randint

vyhra = []
opakovanie = False
while not opakovanie:
    vyhra = sorted([randint(1,49),randint(1,49),randint(1,49),randint(1,49),randint(1,49),randint(1,49)])
    opakovanie = True
    for num in range(5):
        if vyhra[num] == vyhra[num+1]:
            opakovanie = False
            
udaje = open('loteria_1.txt', 'r')

vitazi = [0,]*7 #prave 0, 1, 2, 3, 4, 5, 6 uhadnutych cisiel
tipy = []
for riadok in udaje:
    riadok = riadok.strip().split()
    riadok = [ int(x) for x in riadok ]
    tipy.append((riadok))

    uhadnute = 0
    for tip in tipy[-1]:
        if tip in vyhra:
            uhadnute += 1
    vitazi[uhadnute] += 1
udaje.close()

for i in range(7):
    print(vitazi[i],'ucastnikov uhadli',i)