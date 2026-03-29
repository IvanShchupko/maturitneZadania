s = open('ucenie_sa_slovicok.txt', 'r')
slovicka = s.readlines()
sk = slovicka[::2]
en = slovicka[1::2]
s.close()
jazyk = input('Ak ti mam zadavat slovenske slova zadaj A: ')
slovenske = jazyk = 'A'
a,b = en[:],sk[:]
if slovenske:
    a,b = b,a
zle = 0
while len(a)>0:
    slovo1 = a.pop(0).strip()
    slovo2 = b.pop(0).strip()
    odpoved = input('Zadaj preklad slova ' + slovo1 + ': ')
    if odpoved != slovo2:
        a.append(slovo1)
        b.append(slovo2)
        zle += 1
        print("Nespravne")
    else:
        print("Spravne")
print("Pocet nespravnych odpovedi: " + str(zle))