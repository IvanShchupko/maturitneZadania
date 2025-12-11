import tkinter as tk
from random import *

rozmer, r = 500, 20
n = 4
dx, dy = 2, 0
hra = True

c = tk.Canvas(width=rozmer, height=rozmer)
c.pack()

zrut = c.create_oval(5, 5, r*2+5, r*2+5, fill='blue', tags='zrut')

jablka = []

def stlac(event):
    global dx, dy
    if event.char == 'w':
        dx, dy = 0, -2
    elif event.char == 's':
        dx, dy = 0, 2
    elif event.char == 'a':
        dx, dy = -2, 0
    elif event.char == 'd':
        dx, dy = 2, 0

for i in range(n):
    x = randrange(r, rozmer-r)
    y = randrange(r, rozmer-r)
    
    apple_id = c.create_oval(x-r, y-r, x+r, y+r, fill='red', tags='jablko'+str(i))
    jablka.append((apple_id, c.coords(apple_id)))

def animacia():
    global hra, jablka
    c.move('zrut', dx, dy)
    xz1, yz1, xz2, yz2 = c.coords('zrut')

    new_list = []
    for apple_id, (xj1, yj1, xj2, yj2) in jablka:
        
        if not (xz2 < xj1 or xz1 > xj2 or yz2 < yj1 or yz1 > yj2):
            c.delete(apple_id)
            continue
        new_list.append((apple_id, (xj1, yj1, xj2, yj2)))

    jablka = new_list

    if jablka:
        c.after(10, animacia)
    else:
        c.create_text(250,250,text='You won!1!', font="Arial 40")

animacia()

c.bind_all('<Key>', stlac)
c.mainloop()
