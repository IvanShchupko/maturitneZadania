import tkinter as tk, random as r
c = tk.Canvas(width=500,height=200)
c.pack()

delenec = r.randrange(11,20)
delitel = r.randrange(2,9)
farby = ("red", "orange", "yellow", "green", "lightblue", "blue", "fiolet", "brown", "pink", "cyan")
c.create_text(10,50,text=(str(delenec)+" : "+str(delitel)+" ="),font="Arial 40", anchor="w")



def over():
    text = "Nespravne"
    if int(entry.get()) == delenec // delitel:
        text = "Spravne"
    c.create_text(10,100,text=text,font="Arial 40", anchor="w")
    farba = -1
    x = 10
    for i in range(delenec):
        if i % delitel == 0:
            farba += 1
        if i % delitel == 0 and i == delitel*(delenec//delitel):
            x += 20
        c.create_oval(x,170,x+20,190,fill=farby[farba], outline="")
        x += 20

entry = tk.Entry()
entry.pack()
btn = tk.Button(text="Over", command=over)
btn.pack()

c.mainloop()