import random
action = input("Do you want to encrypt(yes) or to decipher(whatever)? ")

vstup = open('vstupny_text.txt', 'r')

vystup = ''
for line in vstup:
    if action == 'encrypt':
        newLine = chr(96+random.randint(1,25))
    else:
        newLine = line[0]
    for symbol in line:
        if 'a' <= symbol <= 'z':
            symbol = chr(ord(symbol)-ord(newLine[0])+96)
            if ord(symbol) < 97:
                symbol = chr(ord(symbol)+26)
        newLine = newLine + symbol
    vystup = vystup + newLine
vstup.close()
print(vystup)

vystupText = open('mojZasifrovany_text_2.txt', 'w')
vystupText.write(vystup)
vystupText.close()