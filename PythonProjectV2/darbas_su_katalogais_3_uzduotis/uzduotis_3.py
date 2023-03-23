'''
3 užduotis
Sukurti programą, kuri:

Kompiuterio darbalaukyje (Desktop) sukurtų katalogą „Naujas Katalogas“
Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais
Patarimai:

Failo sukūrimo datą galima pasiekti per os.stat(„Failas.txt“).st_ctime
'''

import os
import datetime

print('Esama nuoroda: ', os.getcwd()) # nuoroda kur dabar randames

if not os.path.isdir('folder'):  # tikriname ar nera katalogo su tokiu pavadinimo
    os.mkdir('folder')          # jeigu nera, sukuriame

os.chdir('folder')              # persikeliame i sukurta kataloga

print('Esama nuoroda: ', os.getcwd()) # nuoroda kur dabar randames

with open('tekstas.txt', 'w') as failas:    # sukuriamas failas tekstas.txt
    failas.write(str(datetime.datetime.today()))    # i tekstini faila itraukiama dabartine data, !!!BUTINA NAUDOTI STR!!!

from datetime import datetime
data = os.stat('tekstas.txt').st_mtime
print(datetime.fromtimestamp(data))     # atspausdina failo sukurimo data, bet pries tai reikia panaudoti konvertacija
