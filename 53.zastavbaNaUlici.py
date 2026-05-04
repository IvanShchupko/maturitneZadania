import tkinter as tk

def vykresli():
    s = open("zastavba_na_ulici.txt", "r")
    limit = int(entry.get())
    y = 150
    x = 10
    v2 = 0
    c.delete("all")
    for r in s:
        cisla = r.split()
        sirka = int(cisla[0])
        v = int(cisla[1])
        if v > 0:
            c.create_rectangle(x, y-v, x+sirka, y, fill="grey")
        else:
            c.create_line(x, y, x+sirka, y, width=3, fill="green")
        if v != 0 and v2 !=0 and abs(v - v2) > limit:
            c.create_line(x,y-v, x,y-v2, fill="red", width=3)
        x += sirka
        v2 = v
    s.close()

c = tk.Canvas(width=800, height=200, background="white")
c.pack()

entry = tk.Entry()
entry.pack()

btn = tk.Button(text="Vykresli", command=vykresli)
btn.pack()

c.mainloop()


""" f = open("zastavba_na_ulici.txt", "r")

import tkinter as tk
c = tk.Canvas(width=750, height=150)
c.pack()

xs = []
ys = []

posX, posY = 10,150
for dom in f:
    x, y = dom.strip().split()
    x, y = int(x), int(y)
    xs.append(x)
    ys.append(y)
    c.create_rectangle(posX, posY, posX+x, posY-y, fill="grey")
    if y == 0:
        c.create_line(posX, posY, posX+x, posY, fill="green", width=3)
    posX += x

def vykresli():
    posX = 10
    rozdiel = int(entry.get())
    for i in range(1, len(xs)-1):
        if ys[i] - ys[i-1] > rozdiel:
            c.create_line()

entry = tk.Entry()
entry.pack()

btn = tk.Button(text="vykresli", command=vykresli)
btn.pack()


c.mainloop() """