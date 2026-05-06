def vykres():
    c.delete("all")
    s = open("anketa.txt")
    c.create_text(10, 30, text=s.readline().strip(), font="Arial 15", anchor="w")
    odpovede = ["Ano", "Nie", "Neviem"]
    pocty = s.readline().strip().split()
    pocty[0],pocty[1],pocty[2] = int(pocty[0]),int(pocty[1]),int(pocty[2])
    sum = pocty[0] + pocty[1] + pocty[2]
    s.close()

    y = 70
    for i in range(3):
        farba = "#f00"
        if pocty[i] == max(pocty):
            farba = "#0f0"
        c.create_text(10,y,text=(str(i+1)+") " + odpovede[i] + " - " + str(pocty[i])), font="Arial 15", anchor="w")
        c.create_line(150,y,150+(pocty[i]/sum*350),y, width=30,fill=farba)
        y += 50

def hlas(event):
    if 1 <= int(event.char) <= 3:
        s = open("anketa.txt")
        otazka = s.readline()
        pocty = s.readline().strip().split()
        pocty[0],pocty[1],pocty[2] = int(pocty[0]),int(pocty[1]),int(pocty[2])
        pocty[int(event.char)-1] += 1
        s.close()
        s = open("anketa.txt", "w")
        s.write(otazka)
        s.write(str(pocty[0]) + " " + str(pocty[1]) + " " + str(pocty[2]))
        s.close()
        vykres()

import tkinter as tk
c = tk.Canvas(width=500, height=300)
c.pack()

vykres()

c.bind_all("<Key>", hlas)

c.mainloop()