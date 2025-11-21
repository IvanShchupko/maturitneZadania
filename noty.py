#c, d, e, f, g, a, h

import tkinter
canvas = tkinter.Canvas(width=400, height=800)
canvas.pack()

subor = open('noty.txt', 'r')

cisloNoty = 0
list = subor.readline()
pocet = 0
noty = ['c', 'd', 'e', 'f', 'g', 'a', 'h']
level = [5,10,15,20,25,30,35,40]

def pole():
    global pocet
    for i in range(1,5):
        canvas.create_line(0,160*pocet+30*i,400,160*pocet+30*i)
    pocet += 1

def kresli(level):
    global pocet, cisloNoty
    cisloNoty += 1
    canvas.create_oval(30*cisloNoty-10,160*pocet+140-level*2,30*cisloNoty+10,160*pocet+160-level*2)
    if cisloNoty%13 == 0:
        pole()
        cisloNoty = 0

for znak in list:
    for i in noty:
        if i == znak:
            kresli(level[noty.index(i)])

pole()

subor.close()
canvas.mainloop()

""" import tkinter
canvas = tkinter.Canvas(width=420,height=420)
canvas.pack()
SIRKA = 400
stupnica = 'cdefgah'

def osnova(x, y, dlzka):
    for i in range(5):
        canvas.create_line(x, y+i*10, x+dlzka, y+i*10)

def nacitaj_noty(nazov_suboru):
    subor = open(nazov_suboru, 'r')
    return subor.readline().strip()

def kresli_notu(x, y):
    canvas.create_oval(x-5,y-3,x+5,y+3)

def vyska(nota):
    return stupnica.find(nota) * 5

def kresli(noty):
    notax = 20
    osnovay = 10
    osnova(0, osnovay, SIRKA)
    pocet = 0
    for nota in noty:
        kresli_notu(notax, osnovay + 5*10 - vyska(nota))
        notax += 20
        pocet += 1
        if pocet+1 == SIRKA // 20:
            osnovay += 100
            notax = 20
            pocet = 0
            osnova(0, osnovay, SIRKA)

noty = nacitaj_noty('noty.txt')
kresli(noty)

canvas.mainloop() """

""" import tkinter as tk

subor = open('noty.txt', 'r')
noty = subor.readline()

c = tk.Canvas(width=400, height=600)
c.pack()
spacing, y, count = 15, 20, 0

count = len(noty)
length = count//(360//31)

for i in range(length+1):
    for j in range(5):
        c.create_line(0, y + j*spacing, 400, y+j*spacing, width=2)
    y += 5*spacing + 20

x, y = 20, 15
for note in noty:
    match note:
        case 'c':
            notey = spacing*5
        case 'd':
            notey = spacing*4.5
        case 'e':
            notey = spacing*4
        case 'f':
            notey = spacing*3.5
        case 'g':
            notey = spacing*3
        case 'a':
            notey = spacing*2.5
        case 'h':
            notey = spacing*2

    c.create_oval(x-6,y+notey-3, x+16, y+notey+13, width=2)
    c.create_oval(x-2,y+notey-3, x+12, y+notey+13, width=2)
    c.create_oval(x-3,y+notey-3, x+13, y+notey+13, width=2)

    if x < 380:
        x += 30
    else:
        x = 20
        y += 5*spacing + 20

c.mainloop() """