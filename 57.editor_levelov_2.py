import tkinter as tk
stv = 20
n = 10
farba = "#00f"
bg = "#fff"
c = tk.Canvas(width=stv*n,height=stv*n, background=bg)
c.pack()

i = 1
for y in range(n):
    for x in range(n):
        c.create_rectangle(x*stv,y*stv,(x+1)*stv,(y+1)*stv, fill=bg, tags="stv"+str(x)+str(y))
        i += 1

prvyKlik = True
x1, y1 = -1, -1
def klik(event):
    global mapa, prvyKlik, x1, y1
    x, y = event.x // stv, event.y // stv
    if prvyKlik:
        x1, y1 = x, y
        c.itemconfig('stv' + str(x) + str(y), fill=farba)
    elif x1 == x:
        zaciatok = min(y,y1)
        koniec = max(y,y1)+1
        for i in range(zaciatok, koniec):
            c.itemconfig('stv' + str(x) + str(i), fill=farba)
    elif y1 == y:
        zaciatok = min(x,x1)
        koniec = max(x,x1)+1
        for i in range(zaciatok, koniec):
            c.itemconfig('stv' + str(i) + str(y), fill=farba)
    else:
        c.itemconfig('stv' + str(x1) + str(y1), fill=bg)
    prvyKlik = not prvyKlik

c.bind("<Button-1>", klik)

c.mainloop()