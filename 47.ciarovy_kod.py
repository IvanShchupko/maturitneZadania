import tkinter as tk, random as r
c = tk.Canvas(width=200, height=200)
c.pack()

s = open("ciarovy_kod_1.txt", "r")
kody = s.readlines()
s.close()

kod = str(r.randint(10000000, 99999999))
print(kod)
kody.insert(0, kod)

def kresli(x, y, kod):
    c.create_text(x+35,y+70,text=kod,font="Arial 10")
    for i in range(len(kod)):
        x2 = x+i*10
        y2 = y + 60
        if i == 0 or i == len(kod)-1:
            y2 = y + 80
        c.create_line(x2,y,x2,y2, width=int(kod[i]))

kresli(10,10,kody.pop(0).strip())

def stvorica(event):
    global kody
    c.delete("all")
    kresli(10,10,kody.pop(0).strip())
    kresli(10,110,kody.pop(0).strip())
    kresli(110,10,kody.pop(0).strip())
    kresli(110,110,kody.pop(0).strip())


c.bind_all("<space>", stvorica)

c.mainloop()