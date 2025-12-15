s = open('preklopenie_obrazka.txt', 'r')
info = s.readlines()
s.close()
pixels = info[0].strip().split()
rows = []
for i in range(1, len(info)):
    rows.append(info[i].strip().split())
strana = 5

import tkinter as tk
c = tk.Canvas(width=int(pixels[0])*strana, height=int(pixels[1])*strana)
c.pack()

preklopenie = True
def preklop():
    global preklopenie
    preklopenie = not preklopenie
    c.delete('all')
    for i in range(int(pixels[1])):
        for j in range(int(pixels[0])):
            if preklopenie:
                if rows[i][-j-1] == '1':
                    c.create_rectangle(strana*j,strana*i,strana*j+strana,strana*i+strana, fill='black',outline='')
                else:
                    c.create_rectangle(strana*j,strana*i,strana*j+strana,strana*i+strana, fill='white',outline='')
            else:
                if rows[i][j] == '1':
                    c.create_rectangle(strana*j,strana*i,strana*j+strana,strana*i+strana, fill='black',outline='')
                else:
                    c.create_rectangle(strana*j,strana*i,strana*j+strana,strana*i+strana, fill='white',outline='')
            c.update()

button = tk.Button(command=preklop, text='preklop')
button.pack()

preklop()

c.mainloop()