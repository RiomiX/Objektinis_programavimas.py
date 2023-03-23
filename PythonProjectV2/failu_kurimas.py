import os

"""Kaip pažiūrėti, ką gali os modulis:"""

print(dir(os))

"""Kaip sužinoti katalogą, kuriame esame:"""

print(os.getcwd())

"""Kaip pakeisti aktyvų katalogą, kuriame esame:"""

os.chdir('C:\\Users\\roman\\My Documents')

print(os.getcwd())

"""Kaip pažiūrėti, kokie failai ir katalogai yra kataloge:"""

print(os.listdir())

"""Kaip sukurti naują katalogą:"""

os.mkdir("Naujas katalogas")

"""arba:"""

os.makedirs("Naujas katalogas/Katalogas kataloge")

print(os.listdir())

"""Kaip sužinoti failo/katalogo informaciją:"""

print(os.stat("Demo Katalogas"))

"""arba:"""

print(os.stat("naujas_tekstas.txt"))

# os.stat_result(st_mode=33206,
# st_ino=11258999068714091, st_dev=987816996,
# st_nlink=1, st_uid=0, st_gid=0, st_size=279,
# st_atime=1553103727, st_mtime=1553072965,
# st_ctime=1553101362)

"""Kaip sužinoti failo dydį:"""

print(os.stat("naujas_tekstas.txt").st_size)

"""Kaip sužinoti kada failas buvo paskutinį kartą modifikuotas:"""

print(os.stat("naujas_tekstas.txt").st_mtime)

"""Pakeitus suprantamu formatu:"""

from datetime import datetime
data = os.stat("naujas_tekstas.txt").st_mtime
print(datetime.fromtimestamp(data))

"""Tekstinių failų kūrimas ir nuskaitymas"""

"""Kaip sukurti tekstinį failą: (jei failo nėra, bus sukurtas naujas, jei yra - bus įrašoma jame)"""

with open("failas.txt", 'w') as failas:
    failas.write("Sveikas, pasauli!")

"""arba (kitas būdas, kurio geriau nenaudoti):"""

failas = open("failas.txt", 'w')
failas.write("Sveikas, pasauli!")
failas.close()


"""Kaip nuskaityti tekstą iš failo:"""

with open("failas.txt", 'r') as failas:
    print(failas.read())
# Sveikas, pasauli!

"""Kaip įrašyti ir nuskaityti failą vienu metu:"""

with open("failas.txt", 'r+') as failas:
    print(failas.read())
    failas.write("Labas rytas, pasauli!")

# Sveikas, pasauli!

with open("failas.txt", 'r') as failas:
    print(failas.read())

#Sveikas, pasauli!Labas rytas, pasauli!

"""Kaip į failą įrašyti lietuviškus rašmenis: Problema:"""

with open("failas.txt", 'w') as failas:
    failas.write("Čia yra pirmas failo sakinys")

# UnicodeEncodeError: 'charmap' codec can't encode character '\u010c' in position 0: character maps to <undefined>

"""Sprendimas:"""

with open("failas.txt", 'w', encoding="utf-8") as failas:
    failas.write("Čia yra pirmas failo sakinys")
# Čia yra pirmas failo sakinys

"""Kaip nuskaityti failą su lietuviškais rašmenimis:"""

with open("failas.txt", 'r') as failas:
    print(failas.read())
# ÄŒia yra pirmas failo sakinys

with open("failas.txt", 'r', encoding="utf-8") as failas:
    print(failas.read())
# Čia yra pirmas failo sakinys

"""Kaip pridėti, o ne perrašyti failo eilutę:

Problema:"""

with open("failas.txt", 'w', encoding="utf-8") as failas:
    failas.write("Čia yra pirmas sakinys \n")

with open("failas.txt", 'w', encoding="utf-8") as failas:
    failas.write("Čia yra antras sakinys \n")
# Čia yra antras sakinys

"""Sprendimas:"""

with open("failas.txt", 'a', encoding="utf-8") as failas:
    failas.write("Čia yra pirmas sakinys \n")

with open("failas.txt", 'a', encoding="utf-8") as failas:
    failas.write("Čia yra antras sakinys \n")

# Čia yra pirmas sakinys
# Čia yra antras sakinys

"""Kaip perrašyti tekstą norimoje vietoje:"""

with open("failas.txt", 'w', encoding="utf-8") as failas:
    failas.write("Test")
    failas.write("Test")

# TestTest

with open("failas.txt", 'w', encoding="utf-8") as failas:
    failas.write("Test")
    failas.seek(0)
    failas.write("BE")
# BEst

"""Kaip nuskaityti failą po vieną eilutę:

Čia yra pirmas sakinys
Čia yra antras sakinys
Čia yra trečias sakinys
Čia yra ketvirtas sakinys
Čia yra penktas sakinys
Čia yra šeštas sakinys
Čia yra septintas sakinys
Čia yra aštuntas sakinys
Čia yra devintas sakinys
Čia yra dešimtas sakinys
"""

with open("failas.txt", 'r', encoding="utf-8") as failas:
    print(failas.readline())
    print(failas.readline())
    print(failas.readline())

# Čia yra pirmas sakinys
# Čia yra antras sakinys
# Čia yra trečias sakinys

"""arba:"""

with open("failas.txt", 'r', encoding="utf-8") as failas:
    print(failas.readlines())

# ['Čia yra pirmas sakinys \n', 'Čia yra antras sakinys \n', 'Čia
# yra trečias sakinys \n', 'Čia yra ketvirtas sakinys \n', 'Čia yra
# penktas sakinys \n', 'Čia yra šeštas sakinys \n', 'Čia yra septintas
# sakinys \n', 'Čia yra aštuntas sakinys \n', 'Čia yra devintas sakinys \
# n', 'Čia yra dešimtas sakinys \n']

"""Iteravimas per failo eilutes:"""

with open("failas.txt", 'r', encoding="utf-8") as failas:
    for eilute in failas:
        print(eilute)

# Čia yra pirmas sakinys

# Čia yra antras sakinys

# Čia yra trečias sakinys

# Čia yra ketvirtas sakinys

"""kad nebūtų tarpų tarp eilučių:"""

with open("failas.txt", 'r', encoding="utf-8") as failas:
    for eilute in failas:
        print(eilute, end="")

# Čia yra pirmas sakinys
# Čia yra antras sakinys
# Čia yra trečias sakinys
# Čia yra ketvirtas sakinys
# Čia yra penktas sakinys
# Čia yra šeštas sakinys
# Čia yra septintas sakinys
# .............

"""Kaip nuskaityti ribotą kiekį duomenų:"""

with open("failas.txt", 'r', encoding="utf-8") as failas:
    print(failas.read(100))

# Čia yra pirmas sakinys
# Čia yra antras sakinys
# Čia yra trečias sakinys
# Čia yra ketvirtas sakinys

print(failas.read(100))

# Čia yra penktas sakinys
# Čia yra šeštas sakinys
# Čia yra septintas sakinys
# Čia yra aštuntas sakinys

print(failas.read(100))

# Čia yra devintas sakinys
# Čia yra dešimtas sakinys

"""Darbas su dviem failais (teksto kopijavimas iš vieno į kitą):"""

with open("failas.txt", 'r') as r_failas:
    with open("failo_kopija.txt", 'w') as w_failas:
        for r_eilute in r_failas:
            w_failas.write(r_eilute)

"""(gauname tekstinio failo kopiją)

Dvejetainių failų kopijavimas:

Problema:
"""

with open("logo.png", 'r') as r_failas:
    with open("logo_kopija.png", 'w') as w_failas:
        for r_eilute in r_failas:
            w_failas.write(r_eilute)

# UnicodeDecodeError: 'charmap' codec can't decode byte 0x9d in position 65: character maps to <undefined>

"""Sprendimas:"""

with open("logo.png", 'rb') as r_failas:
    with open("logo_kopija.png", 'wb') as w_failas:
        for r_eilute in r_failas:
            w_failas.write(r_eilute)

"""(gauname paveikslėlio failo kopiją)
Kaip į failą išsaugoti kintamuosius/objektus
(modulis pickle)
Išsaugome kintamąjį
Įrašymas:
"""

import pickle

a = 1024

with open("a.pkl", "wb") as pickle_out:
    pickle.dump(a, pickle_out)

"""Nuskaitymas:"""

import pickle

with open("a.pkl", "rb") as pickle_in:
    naujas_a = pickle.load(pickle_in)

print(naujas_a)

# 1024
"""Išsaugome masyvą:
Įrašymas:"""

import pickle

zodynas = {1:"Pirmas", 2:"Antras", 3:"Trečias"}

with open("zodynas.pkl", "wb") as pickle_out:
    pickle.dump(zodynas, pickle_out)

"""Nuskaitymas:"""

import pickle

with open("zodynas.pkl", "rb") as pickle_in:
    naujas_zodynas = pickle.load(pickle_in)

print(naujas_zodynas)

# {1: 'Pirmas', 2: 'Antras', 3: 'Trečias'}
"""Išsaugome daug kintamųjų (Pickle):
Įrašymas:"""

a = 10
b = 7
c = 23

with open("abc.pkl", "wb") as pickle_out:
    pickle.dump(a, pickle_out)
    pickle.dump(b, pickle_out)
    pickle.dump(c, pickle_out)

"""Nuskaitymas:"""

with open("abc.pkl", "rb") as pickle_in:
    nauja_a = pickle.load(pickle_in)
    nauja_b = pickle.load(pickle_in)
    nauja_c = pickle.load(pickle_in)

print(nauja_a)
print(nauja_b)
print(nauja_c)

# 10
# 7
# 23

"""arba:"""

import pickle

with open("abc.pkl", "rb") as pickle_in:
    while True:
        try:
            print(pickle.load(pickle_in))
        except EOFError:
            break

# 10
# 7
# 23

"""Pavyzdys su vardų sąrašu:"""

import pickle

while True:
    veiksmas = int(input("Pasirinkite veiksmą: 1 - peržiūrėti, 2 - įrašyti, 3 - išeiti"))
    if veiksmas == 1:
        try:
            with open("zmones.pkl", 'rb') as failas:
                print(pickle.load(failas))
        except:
            print("Nėra tokio failo")
            with open("zmones.pkl", 'wb') as failas:
                zmones = []
                pickle.dump(zmones, failas)
    if veiksmas == 2:
        with open("zmones.pkl", 'rb') as failas:
            zmones = pickle.load(failas)
            vardas = input("Įveskite naują vardą")
            with open("zmones.pkl", 'wb') as failas:
                zmones.append(vardas)
                pickle.dump(zmones, failas)
    if veiksmas == 3:
        print("Programa baigta")
        break

"""Pavyzdys su objektų sarašu:"""

import pickle

class Automobilis:
    def __init__(self, marke, modelis):
        self.marke = marke
        self.modelis = modelis

automobiliai = [Automobilis("Toyota", "Avensis"), Automobilis("Toyota", "Corolla"), Automobilis("Toyota", "Camry")]

with open("automobilis.pkl", "wb") as failas:
    pickle.dump(automobiliai, failas)

with open("automobilis.pkl", "rb") as failas:
    automobiliai = pickle.load(failas)
    for automobilis in automobiliai:
        print("Markė", automobilis.marke)
        print("Modelis", automobilis.modelis)
