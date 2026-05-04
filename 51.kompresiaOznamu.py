sprava = "Cez vikend je planovana odstavka severnej casti linky"
slova = sprava.split()
print("Oznam pozostava z " + str(len(slova)) + " slov")
stlacena = ""
velke = True
for slovo in slova:
    if velke:
        stlacena += slovo.upper()
        velke = False
    else:
        stlacena += slovo.lower()
        velke = True
print("Stlacena sprava: " + stlacena)

print("Na obrazovke: ", end="")
velke = True
for znak in stlacena:
    if velke != ("A" <= znak <= "Z"):
        print(end=" ")
        velke = not velke
    print(znak.upper(), end="")

""" v = "Cez vikend je planovana odstavka severnej casti linky"
v = v.strip().split()

print("Oznam pozostava z " + str(len(v)) + " slov")

stlaceny = ""
lower = False
for slovo in v:
    if lower:
        slovo = slovo.lower()
    else:
        slovo = slovo.upper()
    lower = not lower
    stlaceny = stlaceny+slovo

print(stlaceny)

vystup = ""
pred = 66
for znak in stlaceny:
    if 65 < pred < 90 and 97 < ord(znak) < 122 or 65 < ord(znak) < 90 and 97 < pred < 122:
        vystup = vystup + " "
    pred = ord(znak)
    vystup = vystup + znak.upper()

print(vystup) """