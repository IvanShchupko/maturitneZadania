""" import tkinter as tk, random
c = tk.Canvas(width=700,height=650)
c.pack()

def lodicka(x,y):
    plachta = random.randint(-3,3)
    c.create_line(x,y,x,y-25,x+10+plachta,y-10,x,y-5)
    c.create_polygon(x-20,y,x+20,y,x+10,y+8,x-10,y+8)

def nakresli_lodicky():
    for i in range(15):
        lodicka(pozicie[i],i*40+40)
    c.create_line(650,0,650,650, fill='red', width=3)

def vyhra(cislo):
    global start
    start = False
    c.create_text(350,350, font='Ariel 20', fill='red', text='vyhrala lodicka cislo '+str(cislo+1))

def preteky():
    if start:
        c.delete('all')
        for i in range(len(pozicie)):
            pozicie[i] += random.randint(1,10)
            if pozicie[i]>650:
                vyhra[i]
        nakresli_lodicky()
        c.after(100, preteky)

def klik(sur):
    global start
    if not start:
        start = True
        preteky()

pozicie = [20]*15
start = False
nakresli_lodicky()

c.bind('<Button-1>', klik)

c.mainloop() """

""" import tkinter as tk, random
c = tk.Canvas(width=700,height=800)
c.pack()

c.create_line(660,0,660,800, fill='red')

lode = [[20,0]]*15

def lodicka(x,y):
    plachta = random.randint(-3,3)
    c.create_line(x,y,x,y-25,x+10+plachta,y-10,x,y-5)
    c.create_polygon(x-20,y,x+20,y,x+10,y+8,x-10,y+8)

def start():
    for i in range(15):
        o = 700//14*i
        lode[i][1] = o
    print(lode)
    kresli()

def kresli():
    for i in range(15):
        lodicka(lode[i][0], lode[i][1])

start()

c.mainloop() """
