import tkinter as tk, random
c = tk.Canvas(width=650, height=200)
c.pack()
def zapalka(x, y):
    c.create_line(x, y, x, y+100, width=5, fill='yellow')
    c.create_oval(x-5, y-5, x+5, y+8, fill='brown', outline='brown')

pocet = 15
hrac = 1
vyhra = False

def push(event):
    global pocet, hrac, vyhra
    if not vyhra:
        if event.char == '1':
            pocet -= 1
        elif event.char == '2':
            pocet -= 2
        elif event.char == '3':
            pocet -= 3
        else:
            return
        if pocet <= 0:
            pocet = 0
            vyhra = True
        else:
            if hrac == 1:
                hrac = 2
            else:
                hrac = 1
    kresli()
    if vyhra:
        c.create_text(325,100,text="vyhral hrač čislo "+str(hrac), font="Arial 25")

def kresli():
    c.delete('all')
    c.create_text(325,20,text=("ťaha hrač: "+str(hrac)), font="Arial 15")
    c.create_text(325,40,text=("počet zápaliek: "+str(pocet)), font="Arial 15")
    for i in range(pocet):
        zapalka(20+i*40, 75)

kresli()

c.bind_all('<Key>', push)

c.mainloop()