import tkinter as tk
c = tk.Canvas(width=800, height=250)
c.pack()

c.create_text(400,20,text="Vyber jedla",font="Arial 25")

farby = ["green", "red", "blue", "orange"]
kodyFarieb = ["z", "c", "m", "o"]

for i in range(4):
    c.create_rectangle(50+175*i,50,225+175*i,225, fill=farby[i], outline="")

zapis = open("vyber_jedla.txt", "w")
zapis.close()

def klik(sur):
    x = sur.x
    y = sur.y
    kod = entry.get()
    if kod != "":
        for i in range(4):
            if x > 50+175*i and x < 225+175*i and y > 50 and y < 225:
                zapis = open("vyber_jedla.txt", "a")
                zapis.write(kod + " " + kodyFarieb[i] + "\n")
                zapis.close()


c.bind("<1>", klik)

entry = tk.Entry()
entry.pack()

c.mainloop()