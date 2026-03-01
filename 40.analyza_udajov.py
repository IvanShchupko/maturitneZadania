info = open("spokojnost_1.txt", "r")

spok = []
pracovneHodiny = []

den = 0
hodina = -1
vyjadarenia = 0

for line in info:
    spok.append(line.strip().split()[0])
    minuty = (int(spok[-1][3:])/60)
    spok[-1] = spok[-1][:2]
    if spok[-1][0] == '0':
        spok[-1] = int(spok[-1][1])
    else:
        spok[-1] = int(spok[-1])
    if spok[-1] not in pracovneHodiny:
        pracovneHodiny.append(spok[-1])
    
    if hodina > spok[-1]+minuty:
        den += 1
        print(str(den) + ". deň - počet reakcií: " + str(vyjadarenia))
        vyjadarenia = 0
    hodina = spok[-1]+minuty
    vyjadarenia += 1

info.close()

pracovneHodiny = sorted(pracovneHodiny)

print("Celkový počet vyjadrení je " + str(len(spok)))

for hodina in pracovneHodiny:
    reakcii = spok.count(hodina)
    print("Hodina: " + str(hodina) + " Reakcií zákazníkov: " + str(reakcii))

print("Počet dní: " + str(den))