s = open('skok_do_dialky.txt', 'r')

krajiny = []
pocty = []
max = 0
vitazi = []

for r in s:
    info = r.strip().split()
    if info[1] not in krajiny:
        krajiny.append(info[1])
        pocty.append(1)
    else:
        pocty[krajiny.index(info[1])] += 1
    for j in range(2,7):
        if int(info[j]) > max:
            max = int(info[j])
            vitazi = []
            vitazi.append(info[0])
        elif int(info[j]) == max:
            vitazi.append(info[0])

print(krajiny)

for k in range(len(krajiny)):
    print(krajiny[k],':',pocty[k])


print('So skokom velkym',str(max),'cm vitazom je:')
for v in vitazi:
    print(v)
