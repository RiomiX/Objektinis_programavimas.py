import string

# 1 uzduotis
import string


# def sk_suma(sk1, sk2, sk3):
#     suma = sk1 + sk2 + sk3
#     return suma
#
# print(sk_suma(5, 6, 7))
# print(sk_suma(1, 1, 1))

# saraso skaiciu suma


# 2 uzduotis

# def sar_suma(list):
#     suma = 0
#     for i in list:
#         suma += int(i)
#     print(suma)
#     return suma
#
# list = [1, 5, 6, 7, 8]
# atsakymas = sar_suma(list)

# 3 uzduotis Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).

# def did_sk(*args):
#     minsk = 0
#     maxsk = 0
#     for i in args:
#         if i > maxsk:
#             maxsk = i
#         if minsk == 0 or i < minsk:
#             minsk = i
#     print(maxsk)
#     print(minsk)
#
#
# did_sk(1, 5, 6, 2, 9, 4)

# 4 Gražintų paduotą stringą atbulai.

# def atbulai(*args):
#     sks = args[-1]
#     print(sks[::-1])
#
# sk = '1, 2, 3, 4, 5, 6, 7'
# atbulai(sk)

# 5 Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.

# def zsk(*args):
#     mr = 0
#     dr = 0
#     skk = 0
#     num = ''.join(args)
#     niam = num.split()
#     for i in num:
#         if i.islower():
#             mr += 1
#         if i.isupper():
#             dr += 1
#         if i.isdigit():
#             skk += 1
#     print("Mazuju raidziu: ", mr)
#     print("Didziuju raidziu: ", dr)
#     print('Skaiciu kiekis: ', skk)
#     print('Zodziu yra: ', len(niam))
#
# var = input('Iveskite: ')
# zsk(var)

# 6 Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.

# def unikal(args):
#     global pvz
#     pvz = ''.join(set(args))
#     print(pvz)
#     return pvz
#
# zsj = input('Ivesk: ')
# unikal(zsj)
# zsj = pvz
# print(zsj)

# 7 Gražintų, ar paduotas skaičius yra pirminis.

# def pirm(args):
#     if args % 2 == 0 or args % 3 == 0:
#         print('Tai ne pirminis skaicius')
#     elif args // args == 1 and args // 1 == args:
#         print('pirminis')
#
# sk = int(input('Ivesk skaiciu: '))
# pirm(sk)

# 8 Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo

# def atbulai(args):
#     pvz = args.split()
#     print(pvz[::-1])
#
# tarkim = input('Varai: ')
# atbulai(tarkim)

# 9 Gražina, ar paduoti metai yra keliamieji, ar ne.

# def kelmet(args):
#     mr = 2000
#     if args > mr:
#         while mr != args and mr < args:
#             mr += 4
#         if mr == args:
#             print('Metai keliamieji')
#         else:
#             print('Metai nekeliamieji')
#             quit()
#     if args < mr:
#         while mr != args and mr > args:
#             mr -= 4
#         if mr == args:
#             print('Metai keliamieji')
#         else:
#             print('Metai nekeliamieji')
#             quit()
#
# msk = int(input('Metai: '))
# kelmet(msk)

# 10 Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.

# def sukt(args):
#     import datetime
#     x = datetime.date
#     print(x)
#
# lk = int(input('Laikas: '))
# sukt(lk)