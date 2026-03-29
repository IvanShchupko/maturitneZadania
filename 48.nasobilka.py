import random as r

priklady = []
odpovede = []

for i in range(10):
    x, y = r.randrange(101), r.randrange(101)
    priklady.append(str(x)+"*"+str(y))
    odpovede.append(str(x*y))

dobre = 0
kola = 0
while len(priklady)>0:
    priklad = priklady.pop(0)
    odpoved = odpovede.pop(0)
    odpovedZiaka = input('Zadaj preklad slova ' + priklad + ': ')
    kola += 1
    if odpovedZiaka != odpoved:
        priklady.append(priklad)
        odpovede.append(odpoved)
        print("Nespravne")
    elif kola > 10:
        print("Spravne")
    else:
        print("Spravne")
        dobre += 1
print("Pocet spravnych odpovedi: " + str(dobre))