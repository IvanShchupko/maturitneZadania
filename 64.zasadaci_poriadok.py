import tkinter as tk, random as r
c = tk.Canvas(width=500, height=400, background="#fff")
c.pack()

def oznam(info):
    c.delete("all")
    c.create_text(250,200, text=info, fill="red", font="Arial 20")

def kresli(x,y, usadit, maxx,maxy):
    c.delete("all")
    for iy in range(maxy):
        for ix in range(maxx):
            c.create_rectangle(x+ix*s, y+iy*v, x+(ix+1)*s-10, y+(iy+1)*v-10)
            if usadit != []:
                meno, priezvisko = usadit.pop()
                c.create_text(x+(ix+.5)*s-5, y+(iy+.5)*v-15, text=meno , fill="red", font="Arial 7")
                c.create_text(x+(ix+.5)*s-5, y+(iy+.5)*v+5, text=priezvisko , fill="blue", font="Arial 7")

def spracuj():
    radov = int(entry1.get())
    vrade = int(entry2.get())
    if pocet > radov*vrade:
        oznam("Nedostatok lavic")
    else:
        r.shuffle(studenti)
        kresli(20,20, studenti[:],radov, vrade)

s, v = 50,40
studenti = []
subor = open("zasadaci_poriadok.csv", "r")
for riadok in subor:
    student = riadok.strip().split(';')
    studenti.append((student[0], student[1]))
subor.close()
pocet = len(studenti)

label1 = tk.Label(text="Pocet radov")
label2 = tk.Label(text="Lavic v rade")
label1.pack()
label2.pack()
entry1 = tk.Entry()
entry1.pack()

entry2 = tk.Entry()
entry2.pack()

btn = tk.Button(text="Potvrdit", command=spracuj)
btn.pack()

c.mainloop()