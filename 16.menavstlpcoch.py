s = open('mena_zamestnancov.txt', 'r')
udaje = []
for r in s:
    udaje.append(r.strip())
s.close()
names = []
surnames = []
lenName = 0
lenSurname = 0
for i in range(len(udaje)//2):
    names.append(udaje[i])
    lenName = max(lenName,len(names[-1]))
    surnames.append(udaje[len(udaje)//2+i])
    lenSurname = max(lenSurname, len(surnames[-1]))
print('Pocet mien v subore je',str(len(names)))
print('Najdlhsie krstne meno ma tolko znakov', str(lenName))
print('Najdlhsie priezvisko ma tolko znakov', str(lenSurname))
v = open('vystup.txt', 'w')
for i in range(len(names)):
    v.write(names[i] + (' ' * (lenName-len(names[i])+1)) + surnames[i]+'\n')
v.close()