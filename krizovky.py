import tkinter as tk
c = tk.Canvas(width=800, height=300)
c.pack()

s = open('/krizovka1-1.txt','r')

riadky = []

riadok = s.readline()
while riadok != '':
    if '\n' in riadok:
        riadky.append(riadok[:-1])
    else:
        riadky.append(riadok)
    riadok = s.readline()

max = 0
for riadok in riadky:
    if int(riadok[0]) > max:
        max = int(riadok[0])

def kresli(text):
    global y
    for riadok in range(len(riadky)):
        y += 30
        for stlpec in range(len(riadky[riadok])-2):
            x1 = x+stlpec*30
            if int(riadky[riadok][0]) != max:
                x1 += (max - int(riadky[riadok][0]))*30
            c.create_rectangle(x1,y,x1+30,y+30)
            if stlpec + 1 == int(riadky[riadok][0]):
                c.create_rectangle(x1,y,x1+30,y+30, fill='grey')
            if text:
                c.create_text(x1+15,y+15,text=riadky[riadok][stlpec+2])

x = 50
y = -10
text = False
kresli(text)
x = 400
y = -10
text = True
kresli(text)

c.mainloop()