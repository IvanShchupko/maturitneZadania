import tkinter as tk
c = tk.Canvas(width=510, height=510)
c.pack()

pocty_farieb = [0]*256
def pripocitaj(farba):
    pocty_farieb[int(farba,16)] += 1

subor = open('ciernobiely_obrazok_1.txt', 'r')

sirka, vyska = subor.readline().strip().split()
sirka, vyska = int(sirka), int(vyska)

for y in range(vyska):
    riadok = subor.readline().strip()
    for x in range(sirka):
        pripocitaj(riadok[x*2:x*2+2])
subor.close()

hodnota = 500//max(pocty_farieb)
for i in range(len(pocty_farieb)):
    if pocty_farieb[i] != 0:
        farba = "#%02x%02x%02x" % (i, i, i)
        c.create_rectangle(i*2, 505,i*2+2,505-(pocty_farieb[i]*hodnota), width=0, fill=farba)

c.mainloop()

""" import tkinter as tk
c = tk.Canvas(width=450, height=520, bg='white')
c.pack()

def histogram(hodnoty,mierka):
    for i in range(256):
        c.create_rectangle(i*2, 500, i*2+2, 500-hodnoty[i]/mierka, width=0, fill='grey')

subor = open('ciernobiely_obrazok_1.txt', 'r')
riadok = subor.readline()
s, v = riadok.strip().split()
s, v = int(s), int(v)

odtiene = [0]*256
for riadok in s:
    for i in range(s):
        farba = riadok[i*2:i*2+2]
        dec_farba = int(farba, 16)
        odtiene[dec_farba] += 1
subor.close()

max_vyskyt = max(odtiene)
mierka = (max_vyskyt//500)
histogram(odtiene, mierka)


c.mainloop() """