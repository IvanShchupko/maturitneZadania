import tkinter as tk
c = tk.Canvas(width=600, height=300, bg='white')
c.pack()

pocetradov = 10
VEL = 40
busx, busy = 50, 50
volne, obsadene = pocetradov*4, 0

def pocty():
    global volne, obsadene
    c.delete("text")
    c.create_text(busx, 250, text="Pocet volnych: " + str(volne), font="Arial 15", anchor="sw", tags="text")
    c.create_text(busx, 270, text="Pocet obsadenych: " + str(obsadene), font="Arial 15", anchor="sw", tags="text")
    c.create_text(busx, 290, text="Pocet volnych pri ulicke: ", font="Arial 15", anchor="sw", tags="text")

def zafarbi(sedadlo, farba):
    c.itemconfig('sedadlo_' + str(sedadlo), fill=farba)
    
def kresli(x, y, pocet):
    cislo = 0
    for i in range(pocet):
        for j in range(4):
            cislo += 1
            c.create_rectangle(x+i*VEL, y+j*VEL, x+(i+1)*VEL-10, y+(j+1)*VEL-10, fill="lightgreen", tags='sedadlo_'+str(cislo))
            c.create_text(x+i*VEL+VEL/2-5, y+j*VEL+VEL/2-5, text=cislo)

def klik(event):
    global volne, obsadene
    if (busx < event.x < busx + VEL * pocetradov and busy < event.y < busy + VEL * 4):
        ix = (event.x - busx) // VEL
        iy = (event.y - busy) // VEL
        sedadlo = ix * 4 + iy + 1
        if c.itemcget("sedadlo_"+str(sedadlo),"fill") == "lightgreen":
            zafarbi(sedadlo, 'red')
            volne += -1
            obsadene += 1
        else:
            zafarbi(sedadlo, 'lightgreen')
            volne += 1
            obsadene += -1
        pocty()
        print(sedadlo)

def save():
    print("save")

pocty()
kresli(busx, busy, pocetradov)

c.bind('<Button-1>', klik)

button = tk.Button("save", command=save)
button.pack()

c.mainloop()