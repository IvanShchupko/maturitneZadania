hlasovanie = open('hlasovanie_1.txt', 'r')
vypadnutiSubor = open('hlasovanie_vypadnuti.txt', 'r')

info = []
vypadnuti = []
poctyHlasov = [0]*10
najmensi = [9999,'']
najmensiVypadnuti = [9999,'']


for hlas in hlasovanie:
    info.append(int(hlas.strip()))
hlasovanie.close()

for vypadnuty in vypadnutiSubor:
    vypadnuti.append(int(vypadnuty.strip()))
vypadnutiSubor.close()

for hlas in info:
    if 5220 <= hlas <= 5229:
        poctyHlasov[hlas-5220] += 1

print('Celkovy pocet hlasov:',str(len(info)))
for i in range(10):
    print('522'+str(i),':',poctyHlasov[i])
    if najmensiVypadnuti[0] > poctyHlasov[i] and 5220+i not in vypadnuti:
        najmensiVypadnuti[0] = poctyHlasov[i]
        najmensiVypadnuti[1] = '522'+str(i)
    elif najmensi[0] > poctyHlasov[i]:
        najmensi[0] = poctyHlasov[i]
        najmensi[1] = '522'+str(i)

print(najmensi[1],'dostal najmenej hlasov('+str(najmensi[0])+') a nepostupuje do dalsieho kola')
print(najmensiVypadnuti[1],'dostal najmenej hlasov('+str(najmensiVypadnuti[0])+') a nepostupuje do dalsieho kola(ignoruje súťažiacich, ktorí už vypadli)')