vstup = open("komprimovany_obrazok_1.txt", "r")

obrazok = []

s, v = vstup.readline().strip().split()
s, v = int(s), int(v)

import tkinter as tk
c = tk.Canvas(width=s, height=v)
c.pack()

def bod(x,y,farba):
    c.create_rectangle(x,y,x+1,y+1,width=0,fill=farba)

for y in range(v):
    riadok = vstup.readline().strip().split()
    linia = []
    for i in range(len(riadok)):
        if i % 2 == 0:
            for i in range(int(riadok[i])):
                linia.append(0)
        else:
            for i in range(int(riadok[i])):
                linia.append(1)
    obrazok.append(linia)

def kresli(biely, cierny):
    for y in range(v):
        for x in range(s):
            if obrazok[y][x] == 1:
                bod(x,y,biely)
            else:
                bod(x,y,cierny)
        c.update()

def negativ():
    kresli("black", "white")

kresli("white", "black")

b = tk.Button(text="Negativ", command=negativ)
b.pack()

c.mainloop()