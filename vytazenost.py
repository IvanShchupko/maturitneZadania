""" s = open('bus_vytazenost.txt', 'r')

capacita = int(s.readline())
info = []
zastavka = 's'
while zastavka != '':
    zastavka = s.readline().strip()
    info.append(zastavka.split())

print('Pocet zastavok na trase autobusu je',str(len(info)))
print(info)
casti = 0
for i in info:
    slovo = ''
    for j in i:
        if casti == 0:
            slovo += '' """

s = open('bus_vytazenost.txt', 'r')
kapacita = int(s.readline())
zoznam = []
pretazene = []
pocet = 0
naj = 0
for r in s:
    u = r.split()
    if len(u) == 3:
        n = u[2]
    else:
        n = u[2] + ' ' + u[3]
    pocet = pocet + int(u[0]) - int(u[1])
    if pocet > kapacita:
        pretazene.append(n)
        if pocet - kapacita > naj:
            naj = pocet - kapacita
    zoznam.append(n)

print('Kapacita busu:',kapacita)
print('Pocet zastavok:',len(zoznam))
print('Zastavky na trase: ', end='')
for zast in zoznam:
    print(zast, end=', ')
print()
print('Bus bol preplneny nad povolenu kapacitu po vyjdeni zo zastavok:')
for zast in pretazene:
    print(zast)
print('Najvacsie pretazenie o', naj, 'ludi.')