""" s = open('sutaz_vbehu.txt', 'r')
mena = []
cas = []
min = 9999
najlepsi = ''

for bezec in s:
    mena.append(bezec.strip()[:-3])
    cas.append(int(bezec.strip()[-3:]))
    if cas[-1]<min:
        min = cas[-1]
        najlepsi = mena[-1]

print('Počet zúčastených športovcov:',str(len(mena)))
for i in range(len(mena)):
    print('Súťažiaci',mena[i],'dobehol do cieľa za',str(cas[i]),'sekúnd')
print(najlepsi,str(min//60),'min.',str(min%60),'sek.') """

s = open('sutaz_vbehu.txt', 'r')
sportovci = []
for r in s:
    u = r.strip().split()
    sportovci.append((u[0],int(u[1])))
print('Pocet zaucastenych sportovcov:',len(sportovci))
naj = sportovci[0][1]
for p in sportovci:
    if p[1] < naj:
        naj = p[1]
        vitaz = p[0]
print('Najlepsi sportovec',vitaz,str(naj//60),'min.',str(naj%60),'sek.')
