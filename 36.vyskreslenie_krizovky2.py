import tkinter as tk
c = tk.Canvas(width=550, height=250)
c.pack()

def kresli(x, y, pos, text):
    doubleCheck = True
    for i in range(len(text)):
        if text[i] != pos or not doubleCheck:
            c.create_rectangle(x+i*20,y,x+20+i*20,y+20, fill="white")
            
            c.create_rectangle(250+x+i*20,y,250+x+20+i*20,y+20, fill="white")
            c.create_text(250+x+10+i*20,y+10,text=text[i], font="Arial 15")
        else:
            doubleCheck = False
            c.create_rectangle(x+i*20,y,x+20+i*20,y+20, fill="grey")
            
            c.create_rectangle(250+x+i*20,y,250+x+20+i*20,y+20, fill="grey")
            c.create_text(250+x+10+i*20,y+10,text=text[i], font="Arial 15")

udaje = open("krizovka2-2.txt", "r")

tajnicka = list(udaje.readline().strip())

policka = []
maxLen = 0
for line in udaje:
    policka.append(line.strip())
    if maxLen < len(policka[-1]):
        maxLen = len(policka[-1])

for i in range(len(tajnicka)):
    k = 0
    kod = tajnicka[i]
    sym = ''
    while kod != sym:
        sym = policka[i][k]
        k += 1
    kresli((maxLen-k+1)*20,(i+1)*20, kod, policka[i])

c.mainloop()