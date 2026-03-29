import tkinter as tk, random as r
c = tk.Canvas(width=200, height=500)
c.pack()

slova = ('python', 'knedla', 'simon', 'filip', 'brokolica')

def nova_hra():
    global vx, vy, uhadnute, slovo
    vx, vy = r.randint(10,150), 0
    slovo = slova[r.randrange(len(slova))]
    uhadnute = '*'*len(slovo)

def prekresli():
    c.delete('slovo')
    c.create_text(vx, vy, text=uhadnute, font='Arial 20', anchor='nw', tags='slovo')

def padanie():
    global vy
    vy += 5
    prekresli()
    if vy<500 and uhadnute!=slovo:
        c.after(500, padanie)
    elif uhadnute != slovo:
        c.create_text(100,250, text="Neuhadol si!", font='Arial 15')
    else:
        c.create_text(100,250, text="Vyhral si!", font='Arial 15')

def klaves(event):
    global uhadnute
    if event.char in slovo and not event.char in uhadnute:
        nove_uhadnute=''
        for znak in slovo:
            if znak in uhadnute or znak == event.char:
                nove_uhadnute += znak
            else:
                nove_uhadnute += '*'
        uhadnute = nove_uhadnute

slovo = ''
uhadnute = ''
vx, vy = 0, 0

nova_hra()
padanie()

c.bind_all('<Key>', klaves)

c.mainloop()