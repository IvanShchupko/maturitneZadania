""" subor = open('hada.txt', 'r')
subor2 = open('hada kompresia.txt', 'w')
pocet = 0
max = 0
def komresia(s):
    if s == "":
        return
    s = s + '.'
    pismeno = s[0]
    pocet = 0
    vystup = 0
    for znak in s:
        if znak == pismeno:
            pocet += 1
        else:
            vystup = vystup + "{} {}".format(pismeno, pocet)
            pismeno = znak
            pocet = 1
        return vystup
    
for riadok in subor:
    riadok = riadok.strip()
    print(riadok)
    riadok2 = komresia(riadok)
    subor2.write(riadok2)
    print(riadok2)
    if len(riadok) > max:
        max = len(riadok)
    pocet += 1

komresia()

print('pocet riadkov v subore: ' + pocet)
print('pocet krokov v najdlhsej hre: ' + max)
subor.close()
subor2.close() """

import tkinter
canvas = tkinter.Canvas(width=400, height=400)
canvas.pack()

def posun():
    global xhlava, yhlava, narazil, chod, smer
    xhlava += sx
    yhlava  += sy
    z = canvas.coords('hada')
    zx = z[::2]
    zy = z[1::2]
    i = 0
    while i < len(zx) and not narazil:
        if zx[i] == xhlava and zy[i] == yhlava:
            narazil = True
        i += 1
    if not narazil:
        z.append(xhlava)
        z.append(yhlava)
        chod = chod + smer
        canvas.coords('hada', z)
        canvas.after(10, posun)

def klaves(event):
    global sx, sy, smer
    if event.keysym == 'Left':
        sx, sy = -1, 0
        smer = 'L'
    if event.keysym == 'Right':
        smer = 'R'
        sx, sy = 1, 0
    if event.keysym == 'Up':
        smer = 'U'
        sx, sy = 0, -1
    if event.keysym == 'Down':
        smer = 'D'
        sx, sy = 0, 1

def save():
    hada = open('hada.txt', 'w')
    hada.write('\n' + chod)
    hada.close()

narazil = False
xhlava, yhlava = 200, 200
sx, sy = 0, -1
smer = 'H'
chod = ''


canvas.create_line(xhlava,yhlava-sy, xhlava, yhlava, tags='hada')
posun()

button1 = tkinter.Button(text='save', command=save)
button1.pack()

canvas.bind_all('<Key>', klaves)

canvas.mainloop()

