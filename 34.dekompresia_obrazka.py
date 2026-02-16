vstup = open("dekompresia_obrazka_1.txt", "r")
vystup = open("dekompresia_obrazka_vystup.txt", "w")

def spracuj_riadok(riadok):
    riadok = riadok.strip().split()
    for i in range(len(riadok)):
        if i % 2 == 0:
          vystup.write('0'*int(riadok[i]))
        else:
           vystup.write('1'*int(riadok[i]))
    vystup.write("\n")


s, v = vstup.readline().strip().split()

vystup.write(s + " " + v + "\n")

s, v =  int(s), int(v)

for i in range(v):
   spracuj_riadok(vstup.readline())