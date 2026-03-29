import tkinter as tk, random as r
c = tk.Canvas(width=400, height=150)
c.pack()

farby = ["green", "red", "grey", "blue", "orange"]

spravny = r.randint(0,len(farby)-1)
uhadnute = False

c.create_text(200,20, text="Pyrotechnik", font="Arial 15", fill="blue")
c.create_text(200,35, text="oznac spravny kablik", font="Arial 10")

for i in range(len(farby)):
    c.create_rectangle(50,50+i*10,300,60+i*10, fill=farby[i])

cas = 7
def timer():
    global cas, uhadnute
    cas += -1
    if cas == 0:
        c.delete("all")
    elif not uhadnute:
        c.delete("casovac")
        c.create_text(350,75, text=str(cas), font="Arial 30", fill="red", tags="casovac")
        c.after(1000, timer)


def klik(sur):
    global uhadnute
    x = sur.x
    y = sur.y
    for i in range(len(farby)):
        if x > 50 and x < 300 and y > 50+i*10 and y < 60+i*10 and i == spravny:
            uhadnute = True
            c.create_text(200,125, text="Vyhral si!", font="Arial 20")


timer()

c.bind("<1>", klik)

c.mainloop()