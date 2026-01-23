key = input("Write your key: ").lower()
key_currentLetter = 0
action = input("Do you want to encrypt or to decipher the text(encrypt/decipher): ")

vstup = open('vstupny_text.txt', 'r')

vystup = ''
for line in vstup:
    for symbol in line:
        if action == 'encrypt':
            if 'a' <= symbol <= 'z':
                symbol = chr(ord(symbol)+ord(key[key_currentLetter])-96)
                if ord(symbol) > 122:
                    symbol = chr(ord(symbol)-26)
                    
                key_currentLetter += 1
                if key_currentLetter > len(key)-1:
                    key_currentLetter = 0
                    
        elif action == 'decipher':
            if 'a' <= symbol <= 'z':
                symbol = chr(ord(symbol)-ord(key[key_currentLetter])+96)
                if ord(symbol) < 97:
                    symbol = chr(ord(symbol)+26)
                    
                key_currentLetter += 1
                if key_currentLetter > len(key)-1:
                    key_currentLetter = 0
        vystup = vystup + symbol
vstup.close()
print(vystup)

vystupText = ('zasifrovany_text_1.txt', 'w')
vystupText.write(vystup)
vystupText.close()