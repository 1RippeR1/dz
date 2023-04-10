def function():
    stop = ''
    name1 = input()
    spisok_predmet1 = []
    while stop != 'stop':
        predmet1 = input('Тут')
        spisok_predmet1.append(predmet1)
        stop = predmet1

    return spisok_predmet1,name1
x1,x2 = function()
slovar1 = {}
spisok1 = x1
slovar1[x2] = x1
print(slovar1)
x1,x2 = function()
slovar2 = {}
spisok2 = x1
slovar2[x2] = x1
print(slovar2)
x1,x2 = function()
slovar3 = {}
spisok3 = x1
slovar3[x2] = x1
print(slovar3)
print(slovar1,slovar2,slovar3)
slovar4 = []
for k,v in slovar1.items():
    if v not in slovar4:
        slovar4.append(v)

for k,v in slovar2.items():
    if v not in slovar4:
        slovar4.append(v)
for k,v in slovar3.items():
    if v not in slovar4:
        slovar4.append(v)
slovar5 = []
for i in slovar4:
    for i2 in i:
        slovar5.append(i2)
print(set(slovar5))




for sdfs in spisok3:
    if sdfs not in spisok2:
        spisok2.append(sdfs)
spisok9 = []
for sas in spisok1:
    if sas not in spisok2:
        spisok9.append(sas)
for sdfs in spisok3:
    if sdfs not in spisok1:
        spisok1.append(sdfs)
spisok10 = []
for sas in spisok2:
    if sas not in spisok1:
        spisok10.append(sas)
for sdfs in spisok3:
    if sdfs not in spisok2:
        spisok1.append(sdfs)
spisok11 = []
for sas in spisok3:
    if sas not in spisok1:
        spisok11.append(sas)
print(f'уникальные предметы для первого{spisok9}')
print(f'уникальные предметы для второго{spisok10}')
print(f'уникальные предметы для третьего{spisok11}')