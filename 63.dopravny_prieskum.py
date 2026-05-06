zastavky = []
pocet = 0
maxPocet = 0
s = open("dopravny_prieskum.txt", "r")
for riadok in s:
    casti = riadok.strip().split(";")
    nastup = int(casti[0])
    vystup = int(casti[1])
    pocet += nastup - vystup
    maxPocet = max(pocet, maxPocet)
    zastavky.append((casti[2].strip(),pocet,nastup>=10, nastup<3 and vystup<3))
s.close()

print("Zoznam zastavok a pocet cestujucich")
for zastavka in zastavky:
    print(zastavka[0],"-",zastavka[1])
print()

print("Odporucany typ elektricky: ")
if maxPocet > 100:
    print("dlha")
elif maxPocet > 50:
    print("standartna")
else:
    print("kratka")
print()

print("Zastavky s automatom:")
for zastavka in zastavky:
    if zastavka[2]:
        print(zastavka[0])
print()

print("Zastavky na znamenie:")
for zastavka in zastavky:
    if zastavka[3]:
        print(zastavka[0])