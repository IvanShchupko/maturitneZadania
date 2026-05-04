s,v = 400,400
d = 50
import tkinter as tk
c = tk.Canvas(width=s, height=v)
c.pack()

def ciara(x1,y1):
    global x, y
    c.create_line(x1,y1, x1+d*smer[0],y1+d*smer[1])
    x += d*smer[0]
    y += d*smer[1]

def otacanie(krat):
    global smer
    if smer == [0,-1]:
        smer = [-1*krat,0]
    elif smer == [-1,0]:
        smer = [0,1*krat]
    elif smer == [0,1]:
        smer = [1*krat,0]
    else:
        smer = [0,-1*krat]

def skuska(p):
    global cykel, opak
    if p == "ciara":
        ciara(x,y)
    elif p == "vlavo" or p == "vpravo":
        krat = 1
        if p == "vpravo":
            krat = -1
        otacanie(krat)
    elif p == "koniecopakuj":
        cykel = False
    else:
        p = p.split()
        opak = int(p[-1])
        cykel = True
    
def kresli():
    global smer, x, y, cykel, opak
    f = open("kresliaci_robot2.txt", "r")
    prikazy = f.readlines()
    f.close()

    x,y,smer = s//2, v//2, [0,-1]
    opak = 0
    cykel = False
    cykelPrikazy = []
    for p in prikazy:
        p = p.strip()
        if not cykel:
            for i in range(opak-1):
                for c in cykelPrikazy:
                    skuska(c)
            cykelPrikazy = []
            opak = 0
            skuska(p)
        else:
            skuska(p)
            if p != "koniecopakuj":
                cykelPrikazy.append(p)

button = tk.Button(text="Kresli", command=kresli)
button.pack()

c.mainloop()

""" 
import tkinter as tk

s, d = 400, 40
c = tk.Canvas(width=s, height=s)
c.pack()

x = y = s // 2
dirs = [(0,-1),(1,0),(0,1),(-1,0)]  # hore, vpravo, dole, vlavo
i = 0  # index smeru

def krok():
    global x, y
    dx, dy = dirs[i]
    nx, ny = x + d*dx, y + d*dy
    c.create_line(x, y, nx, ny)
    x, y = nx, ny

def vykonaj(cmds):
    global i
    stack = []
    out = []

    for cmd in cmds:
        if cmd.startswith("opakuj"):
            stack.append((out, int(cmd.split()[1])))
            out = []
        elif cmd == "koniecopakuj":
            prev, n = stack.pop()
            out = prev + out * n
        else:
            out.append(cmd)

    for cmd in out:
        if cmd == "ciara":
            krok()
        elif cmd == "vlavo":
            i = (i - 1) % 4
        elif cmd == "vpravo":
            i = (i + 1) % 4

def kresli():
    global x, y, i
    x = y = s // 2
    i = 0

    with open("kresliaci_robot2.txt") as f:
        vykonaj([l.strip() for l in f])

tk.Button(text="Kresli", command=kresli).pack()
c.mainloop()
"""