import tkinter as tk

f = open("obrys_obrazka_1.txt", "r")
s,v = f.readline().strip().split()
s,v = int(s), int(v)
f.close()

c = tk.Canvas(width=s, height=v, bg="white")
c.pack()

def bod(x,y):
    c.create_rectangle(x, y, x+1, y+1, fill="black", outline="black")

def vykresli(far):
    f = open("obrys_obrazka_1.txt", "r")
    f.readline()
    y = 1
    for line in f:
        line = line.strip().split()
        pos = 0
        for j in range(len(line)):
            if j % 2 == far:
                bod(pos,y)
            pos += int(line[j])
        y += 1
    f.close()

def inak():
    vykresli(1)

vykresli(0)

button = tk.Button(text="inak", command=inak)
button.pack()

c.mainloop()