s = open('tabulka_pocetnosti.txt', 'r')
data = s.read().strip()
s.close()
print(data)
nevyskytli = 'Znaky, ktore vobec nevystkytli: '
for i in range(97,123):
    if data.count(chr(i))+data.count(chr(i-32)) == 0:
        nevyskytli = nevyskytli + chr(i) + ' '
    else:
        print(chr(i),'-',str(data.count(chr(i))+data.count(chr(i-32))))
print(nevyskytli)