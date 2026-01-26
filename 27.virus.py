from random import shuffle, randrange
input = open('virus.txt', 'r')

text = []
proceseedText = []

for line in input:
    line = line.split()
    text.append(line)
input.close()

if randrange(0,2) == 0:
    shuffle(text)

for line in text:
    if randrange(0,2) == 0:
        shuffle(line)
    proceseedLine = []
    for word in line:
        if randrange(0,2) == 0:
            word = word[::-1]
        proceseedLine.append(word)
    proceseedText.append(' '.join(proceseedLine))

output = open('virus_vystup.txt', 'w')
output.write('\n'.join(proceseedText))
output.close()