# funkcijos

# def pasisveikinti(vardas):
#     print(f'sveikas, {vardas}')
#
# vardas = 'Gintaras'
# pasisveikinti('Tomas')
# pasisveikinti(vardas)
#
# def kvadratu(skaicius):
#     kvadratas = skaicius ** 2
#     print(kvadratas)
#     return kvadratas # return grazina rezultata
#
# kvadratu(2)
# skaicius = kvadratu(5)
# atsakymas = kvadratu(5) + 10 - 2 * 4
#
# print('skaicius per return: ', skaicius)
# print('skaicius per return: ', atsakymas)
#
# def skaiciu_suma(skaicius1, skaicius2, skaicius3 = 1):
#     rezultatas = (skaicius1 + skaicius2 + skaicius3)
#     return rezultatas
#
# print(skaiciu_suma(2, 4, 6))    # skaiciai nurodomi is eile, ir prisiskiria prie kiekvienos reiksmes, jei 3 nenurodom, jis lieka su 10 verte
#
# def daug_kvadratu(*args):   # * zvaigzdute reiskia nerybotas kiekis argumentu
#     for skaicius in args:
#         print(skaicius ** 2)
#
# daug_kvadratu(1, 2, 3, 4, 5)    # cia gali buti ir kintamieji


# list = []
# def daug_kvadratu(list):
#     for skaicius in list:
#         print(skaicius ** 2)
#
# daug_kvadratu(list)    # cia gali buti ir kintamieji

# def spausdinimas(**kwargs):
#     for raktas, reiksme in kwargs.items():
#         print(raktas, reiksme)
#
# spausdinimas(vardas = 'Gintare', lytis = 'moteris', amzius = '33', daigtai = ['kompiuteris', 'pele', 'klaviatura'])

# globalus = 10
#
# def funkcija():
#     global lokalus  # kad funkcija butu globalus ir matytusi uz finkcijos ribu reikia priskirti globalia reiksme
#     lokalus = 10
#
# funkcija()  # pirma reikia issikviesti funkcija
# atsakymas = globalus + lokalus
# print(atsakymas)