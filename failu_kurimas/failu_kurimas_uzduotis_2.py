""""2 užduotis
Sukurti programą, kuri:
Leistų vartotojui įvesti norimą eilučių kiekį
Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
Įrašytų įvestą tekstą atskiromis eilutėmis į failą
Patarimai:

Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)"""

import os

print('Veskite tekstas:')
print('=======================================================================')
ivestas_tekstas = ' '
bendra = ''
tekstas = ''

while ivestas_tekstas != '':
    ivestas_tekstas = input('')  # Leistų vartotojui įvesti norimą eilučių kiekį
    bendra += ivestas_tekstas

failas = input('Iveskite failo pavadinima: ')   # Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą

with open(failas + '.txt', 'w') as failas:
    atskirom_eilutem = bendra.split('.')  # Įrašytų įvestą tekstą atskiromis eilutėmis į failą
    for i in atskirom_eilutem:
        tekstas += i + '.' + '\n'
    failas.write(tekstas)
