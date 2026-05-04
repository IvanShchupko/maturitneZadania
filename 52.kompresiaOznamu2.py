sprava = "Cez vikend je planovana odstavka severnej casti linky"
slova = sprava.split()
print("Oznam pozostava z " + str(len(slova)) + " slov")
stlacena = ""
for slovo in slova:
    stlacena += slovo[0].upper()+slovo[1:].lower()
print("Stlacena sprava: " + stlacena)

print("Na obrazovke: ", end="")
prve = True
for znak in stlacena:
    if "A" <= znak <= "Z":
        if prve:
            prve = False
        else:
            print(end=" ")
    print(znak.upper(), end="")