import tkinter as tk
farby = ['blue','green','maroon','purple','red','fuchsia','yellow']
c = tk.Canvas(width=1000,height=120,bg='white')
c.pack()

vyraz = input('zadaj vyraz: ')
ok = True
pocet = 0

for znak in vyraz:
    if znak == '(':
        pocet +=1
    elif znak == ')':
        pocet -= 1
        if pocet<0:
            ok = False
            break

if ok and pocet!=0:
    ok = False

if ok:
    oznam = 'zatvorky sú spravne'
else:
    oznam = 'zatvorkz sú nespravne'
c.create_text(500,90, text=oznam, font='Courier 30')

if ok:
    y = 3
    ktora = -1
    for znak in vyraz:
        if znak == '(':
            ktora += 1
        if znak == '(' or ')':
            c.create_text(y,3,anchor='nw', text=znak, font='Courier 30', fill=farby[ktora])
        else:
            c.create_text(y,3,anchor='nw', text=znak, font='Courier 30', fill='black')
        if znak == ')':
            ktora -= 1
        y +=20

c.mainloop()