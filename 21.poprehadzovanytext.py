from random import *

vstup = open('poprehadzovany_text1_vstup.txt', 'r')
text = []
for line in vstup:
    text.append(line.strip().split())
vstup.close()

vystup = ''
for line in text:
    for word in line:
        newword = list(word[1:-1])
        shuffle(newword)
        newword = word[0] + ''.join(newword) + word[-1]
        vystup = vystup + newword + ' '
    vystup = vystup + '\n'
print(vystup)

vystupT = open('poprehadzovany_text1_vystup.txt', 'w')
vystupT.write(vystup)
vystupT.close()