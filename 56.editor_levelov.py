import tkinter as tk
stv = 20
n = 10
c = tk.Canvas(width=stv*n,height=stv*n)
c.pack()

mapa = [["#fff" for _ in range(n)] for _ in range(n)]

for x in range(n):
    for y in range(n):
        c.create_rectangle(x*stv,y*stv,(x+1)*stv,(y+1)*stv, fill=mapa[x][y], tags="stv"+str(x)+str(y))

def klik(event):
    global mapa
    x, y = event.x // stv, event.y // stv
    farba = entry.get()
    c.itemconfig('stv' + str(x) + str(y), fill=farba)
    mapa[x][y] = farba

def save():
    v = open("editor_levelov1_vystup.txt", "w")
    print(mapa)
    for y in range(n):
        for x in range(n):
            v.write(mapa[x][y]+" "*(8-len(mapa[x][y])))
        v.write("\n")
    v.close()

btn = tk.Button(text="save", command=save)
btn.pack()

entry = tk.Entry()
entry.pack()

c.bind("<Button-1>", klik)

c.mainloop()