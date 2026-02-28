data = open("hlasovanie_1.txt", "r")

hlasy = []
for line in data:
    hlasy.append(line.strip())

data.close()

for i in range(10):
    hlasySubor = open("522"+str(i)+".txt", "w")
    for k in range(len(hlasy)):
        if hlasy[k][-1] == str(i):
            hlasySubor.write(str(k)+'\n')
    hlasySubor.close()