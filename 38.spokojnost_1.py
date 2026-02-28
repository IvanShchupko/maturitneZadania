info = open("spokojnost_1.txt", "r")

spok = []
pracovneHodiny = []
celkovyPocetVyjadreni = 0

for line in info:
    celkovyPocetVyjadreni += 1
    spok.append(line.strip().split())
    spok[-1][0] = spok[-1][0][:2]
    if spok[-1][0][0] == '0':
        spok[-1][0] = int(spok[-1][0][1])
    else:
        spok[-1][0] = int(spok[-1][0])
    if spok[-1][0] not in pracovneHodiny:
        pracovneHodiny.append(spok[-1][0])

pracovneHodiny = sorted(pracovneHodiny)

print("Celkový počet vyjadrení je " + str(celkovyPocetVyjadreni))
maxSpokojnych = [0,25]
maxNespokojnych = [0,25]

for hodina in pracovneHodiny:
    spokojne = 0
    nespokojne = 0
    for hlas in spok:
        if hlas[0] == hodina:
            if hlas[1] == "nie":
                nespokojne += 1
            else:
                spokojne += 1

    spokojnost = spokojne / (spokojne + nespokojne)

    print("Počas " + str(hodina)+ " je " + "{:.1%}".format(spokojnost) + " percent spokojných zákazníkov.")

    if maxSpokojnych[0] < spokojne:
        maxSpokojnych = spokojne, hodina
    if maxNespokojnych[0] < nespokojne:
        maxNespokojnych = nespokojne, hodina

print("Počas " + str(maxSpokojnych[1]) + " je najviac spokojných zákazníkov a ich je " + str(maxSpokojnych[0]))
print("Počas " + str(maxNespokojnych[1]) + " je najviac spokojných zákazníkov a ich je " + str(maxNespokojnych[0]))