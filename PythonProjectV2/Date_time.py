# Python DateTime modulis
# Laimei, šiais laikais retai reikia įdiegti sudėtingas funkcijas nuo nulio, 
nes gali padėti daug atvirojo kodo bibliotekų. 
Taip yra neabejotinai „Python“, kuriame standartinėje bibliotekoje yra trys atskiri moduliai, skirti dirbti su datomis ir laiku:

# 1. calendar išveda kalendorių ir teikia funkcijas naudojant idealizuotą Grigaliaus kalendorių.
# 2. DateTime tiekia klases, skirtas manipuliuoti datomis ir laiku.
# 3. time suteikia su laiku susijusias funkcijas, kai datos nereikia.

# Šioje pamokoje daugiausia dėmesio skirsite Python DateTime modulio naudojimui. 
# Pagrindinis „DateTime“ tikslas yra palengvinti prieigą prie objekto atributų, susijusių su datomis ir laiku. 

# „DateTime“ pateikia tris klases, kurias naudoja dauguma žmonių:

# DateTime.date yra idealizuota data, kuri reiškia, kad Grigaliaus kalendorius tęsiasi be galo į ateitį ir praeitį. Šis objektas saugo metus, mėnesį ir dieną kaip atributus.
# DateTime.time yra idealizuotas laikas, kai daroma prielaida, kad per dieną yra 86 400 sekundžių be šuolio sekundžių. Šis objektas saugo valandą, minutę, sekundę, mikrosekundę ir tzinfo (laiko juostos informaciją).
# DateTime.datetime yra datos ir laiko derinys. Jis turi visus abiejų klasių atributus.

# Datetime kintamasis gali išsaugoti datą ir/arba laiką. 
# Jis importuojamas per import datetime

import datetime

# Dabartinė data ir laikas:
data_ir_laikas_dabar = datetime.datetime.today()
data_ir_laikas_dabar_2 = datetime.datetime.now()
print(data_ir_laikas_dabar)
print(data_ir_laikas_dabar_2)

# Tik data:
data_dabar = datetime.date.today()
data_dabar_2 = datetime.datetime.today().date()
print(data_dabar_2)
print(data_dabar)

# Tik laikas:
laikas_dabar = datetime.datetime.today().time()
print(laikas_dabar)

# Nustatome patys data ir laiką
nusistatatome_data_ir_laika = datetime.datetime(1990, 3, 14, 23, 55, 00)
print(nusistatatome_data_ir_laika)

# Nusistatome kokiu formatu bus atspausdinta data ir laikas
print(nusistatatome_data_ir_laika.strftime("%A, %d. %B %Y %I:%M")) #%p = PM/AM

# NAMU DARBAI 
# Datetime formatavimo kodai: https://www.w3schools.com/python/python_datetime.asp 

#Laikas su lietuviškumu:
import locale

# Nusistatome laika patys
locale.setlocale(locale.LC_TIME, 'lt_LT.UTF8')
nustatyta_lietuviska_data_ir_laikas = datetime.datetime(2022, 3, 14, 23, 55, 00)
print(nustatyta_lietuviska_data_ir_laikas.strftime("%A, %d. %B %Y %I:%M ")) #%p - popiet

stringas = nustatyta_lietuviska_data_ir_laikas.strftime("%A, %d %B %Y %I:%M %p") 
print(stringas.capitalize())

# Laikas ir data dabar LT

lietuviska_data_ir_laikas = datetime.datetime.now()
print(lietuviska_data_ir_laikas.strftime("%A, %d. %B %Y %I:%M %p").capitalize())

# Kaip pridėti ar atimti laiką:
dabar = datetime.datetime.now()
print(dabar)

# Jei norime atimti pvz 5 dienas iš dabar
print(dabar - datetime.timedelta(days = 5))

# Jei norime prideti pvz 5 valandas prie dabar
print(dabar + datetime.timedelta(hours = 5))

# Jei norime prideti pvz 20 dienu ir 8 valandas prie dabar
print(dabar + datetime.timedelta(days = 20, hours = 5))

# Kaip sužinoti datų skirtumą (pvz. dienomis):
nepriklausomybes_diena = datetime.datetime(1990, 3, 11)
skirtumas = dabar - nepriklausomybes_diena
print(skirtumas)

# # Kaip įvesti datą/laiką:
# ivesti_data = input("Iveskite data tokiu formatu metai-menuo-diena val:min:s : ")
# data = datetime.datetime.strptime(ivesti_data, "%Y-%m-%d %H:%M:%S")
# skirtumas = (datetime.datetime.now() - data)
# print(skirtumas.days)

# Kaip iš datetime atskirai ištraukti metus, mėnesį, valandas...?
# dabar1 = datetime.datetime.now()

# print(dabar1.year)
# print(dabar1.month)
# print(dabar1.weekday())
# print(dabar1.day)
# print(dabar1.hour)
# print(dabar1.minute)
# print(dabar1.second)
# print(dabar1.microsecond)

# Naudodami timedelta galime pamatuoti, 
# per kiek laiko mūsų kompiuteris susidorojo su užduotimi, 
# pvz.:

pradzia = datetime.datetime.today()
for n in range(10):
    print("Labas")

pabaiga = datetime.datetime.today()
print(f"Programa uztruko {(pabaiga - pradzia).total_seconds()}")

# Taip pat galime į kodą įdėti pauzę:
import time 

for m in range(10):
    print("Labas rytas")
    time.sleep(2)

# # 1 UZDUOTIS Parašyti programą, kuri:
# # Atspausdintų dabartinę datą ir laiką
# # Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
# # Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
# # Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
# # Patarimas: naudoti datetime, timedelta (from datetime import timedelta)
# # https://www.w3schools.com/python/python_datetime.asp


# # 2 UZDUOTIS Parašyti programą, kuri:
# # Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
# # Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
# # Metų
# # Mėnesių
# # Dienų
# # Valandų
# # Minučių
# # Sekundžių
# # Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t.t. 
# # paskaičiuokite apytiksliai.
# # Patarimas: naudoti datetime, .days, .total_seconds()
# # Skaičių suapvalinimo pavyzdys (kurio gali prireikti šioje užduotyje): print(round(skaicius))