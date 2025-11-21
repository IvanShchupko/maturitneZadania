subor = open('meteo_stanice.txt', 'r')

pocet = 0
teploty = []
max = -285
maxKod = ''
sum = 0

for riadok in subor:
    pocet += 1
    if riadok[21] == '+':
        teplota = float(riadok[22:24] + '.' + riadok[25])
    else:
        teplota = float(riadok[21:24] + '.' + riadok[25])

    if max < teplota:
        max = teplota
        maxKod = riadok[0:3]
    sum += teplota

    teploty.append(teplota)

ave = sum / pocet

print("Pocet merani: " + str(pocet))
print(teploty)
print("Najvyssia namerana teplota: " + str(max))
print("Kod najteplejsie stanice: " + maxKod)
print("Priemerna teplota vsetkych stanic: " + str(ave)[:5])

subor.close()

""" subor = open('meteo_stanice.txt', 'r')

pocet = 0
zoz = []
teploty = []
ibateploty = []
for r in subor:
    info = r.strip()
    teplota = info[21:26]
    teplota = float(teplota.replace(',', '.')) #riadok A
    teploty.append((teplota, info[0:3]))
    ibateploty.append(teplota)
    print(teplota)
    pocet += 1
    zoz.append(info)
subor.close()

print("Pocet merani: ", pocet)
print("Max bolo v stanici: " , max(teploty)[1])
priemer = sum(ibateploty)/len(teploty)
print('Priemerna teplots bola: {:5.2f} stupnov'.format(priemer))

subor.close() """