import tkinter as tk
c = tk.Canvas(width=400, height=300)
c.pack()

sentence = input('Uvedzte tajomstvo: ')
shelves = [' ','ABC','DEF','GHI','JKL','MNO','PQR','STU','VWX','YZ']
maximum = [0]*10
code = ''
for letter in sentence:
    for shelf in shelves:
        for symbol in shelf:
            if symbol == letter:
                code = code + (str(shelves.index(shelf))*(shelf.find(symbol)+1)) + ' '
                maximum[shelves.index(shelf)] += 1

c.create_text(200,150,text=code,font='Arial 25')

vystup = 'Najčastejšie zvolené políčka: '
for i in range(len(maximum)):
    if max(maximum) == maximum[i]:
        vystup = vystup + str(i) + ' '

print(vystup)
c.mainloop()