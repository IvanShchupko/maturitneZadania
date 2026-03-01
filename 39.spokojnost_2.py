info = open("spokojnost_1.txt", "r")

spok = []
pracovneHodiny = []

for line in info:
    spok.append(line.strip().split())
    spok[-1][0] = spok[-1][0][:2]
    if spok[-1][0][0] == '0':
        spok[-1][0] = int(spok[-1][0][1])
    else:
        spok[-1][0] = int(spok[-1][0])
    if spok[-1][0] not in pracovneHodiny:
        pracovneHodiny.append(spok[-1][0])

pracovneHodiny = sorted(pracovneHodiny)

print("Celkový počet vyjadrení je " + str(len(spok)))
maxNespokojnych = [0,25]

celkovyPocetNespokojnych = 0

import tkinter as tk
sirka, vyska = 480, 520
c = tk.Canvas(width=sirka, height=vyska)
c.pack()

pocetHodin = 24
for i in range(pocetHodin):
    nespokojne = 0
    if i in pracovneHodiny:
        nespokojne = spok.count([i, "nie"])
        celkovyPocetNespokojnych += nespokojne
        print("Počas " + str(i)+ " hodiny bolo " + str(nespokojne) + " nespokojných zákazníkov.")
        if maxNespokojnych[0] < nespokojne:
            maxNespokojnych = nespokojne, i
    c.create_rectangle(1+i*20,vyska-20,i*20+19,vyska-20-nespokojne*80, fill="red")
    c.create_text(10+i*20,vyska-10, text=str(i), font="Arial 10")
print("Celkový počet negatívnych vyjadrení je " + str(celkovyPocetNespokojnych))
print("Počas " + str(maxNespokojnych[1]) + " je najviac spokojných zákazníkov a ich je " + str(maxNespokojnych[0]))

c.mainloop()