subor = open('objednane_jedla.txt', 'r')
pocet, z, c, m, o = 0, 0, 0, 0, 0
for r in subor:
    pocet += 1
    r = r.strip()
    if r[-1] == 'z':
        z += 1
    elif r[-1] == 'c':
        c += 1
    elif r[-1] == 'm':
        m += 1
    elif r[-1] == 'o':
        o += 1
subor.close()
print("Celkovy pocet objednanych jedal:", pocet)
print("Zelenych je",z,"\n","Cervenych je",c,"\n","Modrych je",m,"\n","Oranzovych je",o)

if z < 20:
    print("Zelenych jediel je menej ako 20")
if c < 20:
    print("Cervenych jediel je menej ako 20")
if m < 20:
    print("Modrych jediel je menej ako 20")
if o < 20:
    print("Oranzovych jediel je menej ako 20")

if z >= 20 and c >= 20 and m >= 20 and o >= 20:
    print("Bol objednany dostatocny pocet jedal kazdeho druhu")