"""1 užduotis
Sukurti programą, kuri:

Sukurtų failą „Tekstas.txt“ su pilnu tekstu, gauto python kode paleidus „import this“.
Patarimai:

Naudoti from datetime import datetime, datetime.today()
Kintamajam priskirti sakinį, kuriuo bus operuojama, eilutėmis
Kai kur galima panaudoti funkcijas iš praeitų pamokų
"""
import os
import datetime

opa = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

os.chdir('C:\\Users\\roman\\Documents')

"""Kaip pažiūrėti, kokie failai ir katalogai yra kataloge:"""

print(os.getcwd())

"""Kaip pažiūrėti, kokie failai ir katalogai yra kataloge:"""

print(os.listdir())

"""Kaip sukurti naują katalogą:"""
#
# os.mkdir("Naujas katalogas")

with open("failas.txt", 'w') as failas:     # Sukurtų failą „Tekstas.txt“ su pilnu tekstu, gauto python kode paleidus „import this“.
    failas.write(opa)
    failas.close()

os.chdir('C:\\Users\\roman\\Documents')

with open('failas.txt', 'r') as failas:     # Atspausdintų tekstą iš sukurto failo
    print(failas.read())
    failas.close()

os.chdir('C:\\Users\\roman\\Documents')

with open('failas.txt', 'a') as failas:    # Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
    failas.write(str(datetime.time()))
    failas.close()

os.chdir('C:\\Users\\roman\\Documents')     # Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).

notepad = ''
n = 1

with open('C:\\Users\\roman\\Documents\\failas.txt', 'r') as failas:
    for i in failas:
        notepad += str(n) + ' ' + i
        n += 1
        print(i)

with open('failas.txt', 'w') as failas:
    failas.write(notepad)
    failas.close()

notepad = ''
with open('C:\\Users\\roman\\Documents\\failas.txt', 'r') as failas: # Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
        notepad = failas.read()
        notepad = notepad.replace('Beautiful is better than ugly.', 'Gražu yra geriau nei bjauru.')
        print(notepad)

with open('C:\\Users\\roman\\Documents\\failas.txt', 'w') as failas:
    failas.write(notepad)
    failas.close()

notepad = ''
with open('C:\\Users\\roman\\Documents\\failas.txt', 'r') as failas: # Atspausdintų visą failo tekstą atbulai
    notepad = failas.read()
    failas.close()
    notepad = notepad[::-1]
    print(notepad)

notepad = ''
with open('C:\\Users\\roman\\Documents\\failas.txt', 'r') as failas:    # Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
    notepad = failas.read()
    failas.close()
    zd = len(notepad.split())
    sk = 0
    dr = 0
    mr = 0
    for i in notepad:
        if i.isdigit():
            sk += 1
    for i in notepad:
        if i.isupper():
            dr += 1
    for i in notepad:
        if i.islower():
            mr += 1
    print(zd, sk, dr, mr)

with open('C:\\Users\\roman\\Documents\\failas.txt', 'r') as failas:   #Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS
    notepad = failas.read()
    failas.close()
with open('C:\\Users\\roman\\Documents\\failas2.txt', 'w') as failas2:
    failas2.write(notepad.upper())
    failas2.close()


