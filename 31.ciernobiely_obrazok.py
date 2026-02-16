import tkinter as tk

def bod(x,y,farba):
    c.create_rectangle(x,y,x+1,y+1,width=0,fill=farba)

def vykresli(vsetky_odtiene):
    c.delete('all')
    subor = open('ciernobiely_obrazok_1.txt', 'r')
    riadok = subor.readline()
    y = 0
    for riadok in subor:
        riadok = riadok.strip()
        for i in range(sirka):
            odtien = riadok[i*2:i*2+2]
            if not vsetky_odtiene:
                farba = '#000'
                if odtien > '7f':
                    farba = '#fff'
            else:
                farba = '#'+3*odtien
            bod(i,y,farba)
        c.update()
        y += 1
    subor.close()

def CB():
    vykresli(False)
    
subor = open('ciernobiely_obrazok_1.txt', 'r')
riadok = subor.readline()

sirka, vyska = riadok.strip().split()
sirka, vyska = int(sirka), int(vyska)

c = tk.Canvas(width=sirka, height=vyska, bg = '#fff')
c.pack()

vykresli(True)

b = tk.Button(text = 'CB', command=CB)
b.pack()

c.mainloop()