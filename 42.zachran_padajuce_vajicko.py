import tkinter as tk, random as r
c = tk.Canvas(width=400, height=400)
c.pack()

def nova_hra():
    global pismeno, koniec, x, y
    koniec = False
    x, y = r.randint(20,380), 30
    pismeno = chr(r.randint(97,122))

def hra():
    global y, koniec
    y += 5
    c.delete("vajco")
    c.create_oval(x-10,y+15,x+10,y-15, tags="vajco")
    c.create_text(x,y, text=pismeno, font="Arial 15", tags="vajco")
    if y < 400 and not koniec:
        c.update()
        c.after(100, hra)


def stlacit(event):
    global koniec
    if event.char == pismeno:
        koniec == True
        nova_hra()

nova_hra()
hra()

c.bind_all("<Key>", stlacit)

c.mainloop()