import tkinter as tk
from random import *
c = tk.Canvas(width=600,height=400, bg='lightblue')
c.pack()

def medzera(event):
    kresli()

def kresli():
    c.delete('all')
    for i in range(20):
        polygon = []

        startX = round(randrange(50,550),-1)
        startY = round(randrange(250,320),-1)

        farba = '#{:02x}{:02x}{:02x}'.format(0, randrange(50,256), 0)

        kopec = randrange(3)
        if kopec == 1:
            y = startY
            for i in range(startX//10+1):
                polygon.append((startX-i*10,y))
                y -= randrange(6)

            polygon.append((0,400))
            polygon.append((600,400))

            y = startY
            zoznamPo = []

            for i in range((600-startX) // 10 + 10):
                zoznamPo.append((startX+i*10,y))
                y -= randrange(6)
            for i in range(len(zoznamPo)):
                polygon.append(zoznamPo[-i-1])

        else:
            y = startY
            for i in range(startX//10+1):
                polygon.append((startX-i*10,y))
                y += randrange(6)

            polygon.append((0,400))
            polygon.append((600,400))

            y = startY

            for i in range((600-startX) // 10 + 10):
                polygon.insert(0,(startX+i*10,y))
                y += randrange(6)
                
        c.create_polygon(polygon,fill=farba, outline='black')

kresli()

c.bind_all("<space>", medzera)

c.mainloop()