""""2 užduotis
Sukurti programą, kuri:

Įrašytų įvestą tekstą atskiromis eilutėmis į failą
Patarimai:

Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)"""

import os

print('Veskite tekstas:')
print('=======================================================================')
ivestas_tekstas = ' '

while ivestas_tekstas != '':
    ivestas_tekstas = input('')  # Leistų vartotojui įvesti norimą eilučių kiekį

failas = input('Iveskite failo pavadinima: ')   # Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą
with open(failas, 'w') as failas:
    failas.write(ivestas_tekstas)



