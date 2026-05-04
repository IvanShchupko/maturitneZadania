f = open("lodicky.txt", "r")

s,v = f.readline().strip().split()
s,v = int(s), int(v)

import tkinter as tk, random as r
c = tk.Canvas(width=s*20,height=v*20)
c.pack()

mapa = []
 
for riadok in f:
    riadok = riadok.strip().split()
    mapa.append(riadok)

def kresli():
    global mapa
    c.delete("priestor")
    x,y = 0,0
    for riadok in mapa:
        for kusok in riadok:
            if kusok == "0":
                c.create_rectangle(x*20,y*20,x*20+20,y*20+20,fill="blue", outline="", tags="priestor")
            elif kusok == "1":
                c.create_rectangle(x*20,y*20,x*20+20,y*20+20,fill="grey", outline="", tags="priestor")
            else:
                c.create_rectangle(x*20,y*20,x*20+20,y*20+20,fill="yellow", outline="", tags="priestor")
            x += 1
        x = 0
        y += 1

def lod():
    global mapa
    x,y = 0, 0
    for riadok in mapa:
        miesto = 0
        for kusok in riadok:
            if kusok == "0":
                miesto += 1
            elif kusok == "1" or miesto == -1:
                miesto = 0
            else:
                miesto = -1
            if miesto == 3:
                mapa[y][x-2], mapa[y][x-1], mapa[y][x] = "2","2","2"
                kresli()
                return
            x += 1
        x = 0
        y += 1
    c.create_text(s*10,v*10,text="Pristav je plny!", font="Arial 15")


kresli()

button = tk.Button(text="lodicka", command=lod)
button.pack()

c.mainloop()