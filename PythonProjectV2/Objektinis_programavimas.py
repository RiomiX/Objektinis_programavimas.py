#
# 1 uzduotis is https://github.com/DonatasNoreika/python1lygis/wiki/Objektinis-programavimas-(I-dalis),-klas%C4%97s
#
# class sakinys:
#     def __init__(self, tekstas):
#         self.tekstas = tekstas
#
#     def atbulai(self):
#         return self.tekstas[::-1]
#
#     def mazos(self):
#         return self.tekstas.lower()
#
#     def didr(self):
#         return self.tekstas.upper()
#
#     def sym(self):
#         x = int(len(self.tekstas))
#         return x
#
#     def pkz(self):
#         x = input('Kuri zodi pakeisti: ')
#         y = input('I koki: ')
#         z = self.tekstas.replace(x, y)
#         return z
#
#     def kiek(self):
#         sk = 0
#         dr = 0
#         mr = 0
#         z = self.tekstas
#         for i in z:
#             if i.isdigit():
#                 sk += 1
#             if i.isupper():
#                 dr += 1
#             if i.islower():
#                 mr += 1
#
#         g = self.tekstas.split()
#         print(len(g))
#         print(sk)
#         print(dr)
#         print(mr)
#
# opa = input('Ivesk teksta: ')
# opa2 = sakinys(opa)
# print(opa)
# print(opa2.atbulai())
# print(opa2.mazos())
# print(opa2.didr())
# print(opa2.sym())
# print(opa2.pkz())
# opa2.kiek()

# destytojo uzuomena
# class Sakinys:
#     def __init__(self, tekstas):
#         self.tekstas = tekstas
#
#     def atbulai(self):
#         return self.tekstas[::-1]
#
#     def mazosiomis(self):
#         return self.tekstas.lower()

# sakinys1 = Sakinys("Code Academy")
# print(sakinys1.atbulai())
# print(sakinys1.mazosiomis())

# 2 uzduotis

# import datetime
#
# class sukaktis:
#     def __init__(self, mt, mn, dn, vl, mnt, skd):
#         self.mt = mt
#         self.mn = mn
#         self.dn = dn
#         self.vl = vl
#         self.mnt = mnt
#         self.skd = skd
#         skirtumas = datetime.datetime.today() - datetime.datetime(self.mt, self.mn, self.dn, self.vl, self.mnt, self.skd)
#         print('Metu: ', skirtumas.days // 365, 'Savaiciu: ', skirtumas.days // 7, 'Dienu: ', skirtumas, 'Valandu: ', skirtumas.days * 24)
#         mr = 2000
#         if self.mt > mr:
#             while mr != self.mt and mr < self.mt:
#                 mr += 4
#                 if mr == self.mt:
#                     print('Metai keliamieji')
#                 else:
#                     print('Metai nekeliamieji')
#         if self.mt < mr:
#             while mr != self.mt and mr > self.mt:
#                     mr -= 4
#             if mr == self.mt:
#                 print('Metai keliamieji')
#             else:
#                 print('Metai nekeliamieji')
#         print('Nustatyta data: ', self.mt, self.mn, self.dn, self.vl, self.mnt, self.skd)
#         atimam = datetime.datetime(self.mt, self.mn, self.dn) - datetime.timedelta(days=14)
#         print('Atimta 14 dienu:', atimam)
#         pridedam = datetime.datetime(self.mt, self.mn, self.dn) + datetime.timedelta(days=15)
#         print('Prideta 15 dienu', pridedam)
#
#
# vestuves = sukaktis(1990, 12, 5, 12, 55, 59)

# 3_1 uzduotis

# class sakinys:
#     def __init__(self, tekstas):
#         self.tekstas = tekstas
#
#     def atbulai(self):
#         return self.tekstas[::-1]
#
#     def mazos(self):
#         return self.tekstas.lower()
#
#     def didr(self):
#         return self.tekstas.upper()
#
#     def sym(self):
#         x = int(len(self.tekstas))
#         return x
#
#     def pkz(self):
#         x = input('Kuri zodi pakeisti: ')
#         y = input('I koki: ')
#         z = self.tekstas.replace(x, y)
#         return z
#
#     def kiek(self):
#         sk = 0
#         dr = 0
#         mr = 0
#         z = self.tekstas
#         for i in z:
#             if i.isdigit():
#                 sk += 1
#             if i.isupper():
#                 dr += 1
#             if i.islower():
#                 mr += 1
#         g = self.tekstas.split()
#         print('Zodziu tekste: ', len(g))
#         print('Skaiciu tekste: ', sk)
#         print('Dideliu raidziu: ',dr)
#         print('Mazu raidziu: ',mr)
#
# opa = input('Ivesk teksta: ')
# if 0 == int(len(opa)):
#     opa = 'Zen of Python'
#     opa2 = sakinys(opa)
# else:
#     opa2 = sakinys(opa)
# print(opa)
# print(opa2.atbulai())
# print(opa2.mazos())
# print(opa2.didr())
# print(opa2.sym())
# print(opa2.pkz())
# opa2.kiek()

# 3_2 uzduotis

# import datetime
#
# class sukaktis:
#     def __init__(self, mt, mn, dn, vl, mnt, skd):
#         self.mt = mt
#         self.mn = mn
#         self.dn = dn
#         self.vl = vl
#         self.mnt = mnt
#         self.skd = skd
#         skirtumas = datetime.datetime.today() - datetime.datetime(self.mt, self.mn, self.dn, self.vl, self.mnt, self.skd)
#         print('Metu: ', skirtumas.days // 365, 'Savaiciu: ', skirtumas.days // 7, 'Dienu: ', skirtumas, 'Valandu: ', skirtumas.days * 24)
#         mr = 2000
#         if self.mt > mr:
#             while mr != self.mt and mr < self.mt:
#                 mr += 4
#                 if mr == self.mt:
#                     print('Metai keliamieji')
#                 else:
#                     print('Metai nekeliamieji')
#         if self.mt < mr:
#             while mr != self.mt and mr > self.mt:
#                     mr -= 4
#             if mr == self.mt:
#                 print('Metai keliamieji')
#             else:
#                 print('Metai nekeliamieji')
#         print('Nustatyta data: ', self.mt, self.mn, self.dn, self.vl, self.mnt, self.skd)
#         atimam = datetime.datetime(self.mt, self.mn, self.dn) - datetime.timedelta(days=14)
#         print('Atimta 14 dienu:', atimam)
#         pridedam = datetime.datetime(self.mt, self.mn, self.dn) + datetime.timedelta(days=14)
#         print('Prideta 15 dienu', pridedam)
#
#
# vestuves = input('Ivesti data: ')
# if 0 == int(len(vestuves)):
#     gim = sukaktis(1987, 9, 2, 22, 40, 59)
# else:
#     vestuves = sukaktis(1990, 12, 5,12, 12 ,59)

# 4 uzduotis

# Esme uzduoties tokia, panaudoti __str__ funkcija, apacioje pavyzdis is manim parasyto kodo,
# kuris padeda is neaiskios teksto eilutes, tiksliau is atminties vietos istraukti atsakyma
# teksto pavydalu o ne koduote

# def __str__(self):
# return f'Vardas: {self.vardas}, Valandinis: {self.valandos_ikainis}, pradeda darba nuo: {self.dirba_nuo}'

# import datetime
#
#
# class Darbuotojas:
#     def __init__(self, vardas, valandos_ikainis, dirba_nuo):
#         self.vardas = vardas
#         self.valandos_ikainis = valandos_ikainis
#         # data = datetime.datetime.strptime(dirba_nuo, '%Y, %m, %d')
#         self.dirba_nuo = dirba_nuo
#
#     def __str__(self):
#         return f'Vardas: {self.vardas}, Valandinis: {self.valandos_ikainis}, pradeda darba nuo: {self.dirba_nuo}'
#
#     def dirba_dienu(self):
#         data = datetime.datetime.today()
#         pdata = datetime.datetime.strptime(self.dirba_nuo, '%Y-%m-%d')  # labais varbu tiksliai nurodyti laiko formata
#         atidirbo = data - pdata  # kitaip uzsikrusy ieskoti galu
#         return atidirbo.days
#
#     def atlyginimas(self):
#         bendra = int(self.dirba_dienu()) * 8 * int(self.valandos_ikainis)
#         return bendra
#
#
# class NormalusDarbuotojas(Darbuotojas):
#
#     def dirba_dienu(self):
#         data = datetime.datetime.today()
#         pdata = datetime.datetime.strptime(self.dirba_nuo, '%Y-%m-%d')
#         kazkas = data - pdata
#         ats = round(kazkas.days / 7 * 5)
#         return ats
#
#     def atlyginimas(self):
#         salga = self.dirba_dienu() * 5 * 8 * int(self.valandos_ikainis)
#         return salga
#
#
# zm1 = Darbuotojas('Pranas', '5', '2023-03-06')
# zm2 = NormalusDarbuotojas('Vladukas', '15', '2023-03-06')
# zm3 = NormalusDarbuotojas('Petriukas', '7', '2023-03-08')
# zm4 = Darbuotojas('Tadikas', '20', '2023-02-12')
# zm5 = NormalusDarbuotojas('Untanas', '11', '2020-01-01')
#
# print(f'Zmogus vardu {zm5.vardas} dirbdamas {zm5.dirba_dienu()} ir gauna {zm5.atlyginimas()} kapeiku')
# print(f'Zmogus vardu {zm4.vardas} dirbdamas {zm4.dirba_dienu()} ir gauna {zm4.atlyginimas()} kapeiku')







# 5 užduotis:
# Padaryti minibiudžeto programą, kuri:
# Leistų vartotojui įvesti pajamas
# Leistų vartotojui įvesti išlaidas
# Leistų vartotojui parodyti pajamų/išlaidų balansą
# Leistų vartotojui parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis)
# Leistų vartotojui išeiti iš programos
# Rekomendacija, kaip galima būtų padaryti:
# Programa turi turėti klasę Irasas, kuri turėtų argumentus tipas (Pajamos arba Išlaidos) ir suma. Galima prirašyti str metodą, kuris gražintų, kaip bus atvaizduojamas spausdinamas objektas.
# Programa turi turėti klasę Biudzetas, kurioje būtų:
# Metodas init, kuriame sukurtas tuščias sąrašas zurnalas, į kurį bus dedami sukurti pajamų ir išlaidų objektai
# Metodas prideti_pajamu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų pajamų objektą ir įdėtų jį į biudžeto žurnalą
# Metodas prideti_islaidu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų išlaidų objektą ir įdėtų jį į biudžeto žurnalą
# Metodas gauti_balansą(self), kuris gražintų žurnale laikomų pajamų ir išlaidų balansą.
# Metodas parodyti_ataskaita(self), kuris atspausdintų visus pajamų ir išlaidų įrašus (nurodydamas kiekvieno įrašo tipą ir sumą).



class Irasas:  # klasę Irasas, kuri turėtų argumentus tipas (Pajamos arba Išlaidos) ir suma. Galima prirašyti str metodą, kuris gražintų, kaip bus atvaizduojamas spausdinamas objektas.

    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma

    def __str__(self):
        return f'{self.tipas}: {self.suma}'


class Biudzetas:

    def __init__(self):   # kuriame sukurtas tuščias sąrašas zurnalas, į kurį bus dedami sukurti pajamų ir išlaidų objektai
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma):   # kuris priimtų paduotą sumą, sukurtų pajamų objektą ir įdėtų jį į biudžeto žurnalą
        pajamos = Irasas('Pajamos', suma)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma):  # kuris priimtų paduotą sumą, sukurtų išlaidų objektą ir įdėtų jį į biudžeto žurnalą
        islaidos = Irasas('Islaidos', suma)
        self.zurnalas.append(islaidos)

    def gauti_balansą(self):    # kuris gražintų žurnale laikomų pajamų ir išlaidų balansą
        suma = 0
        for irasas in self.zurnalas:
            if irasas.tipas == 'Pajamos':
                suma += irasas.suma
            if irasas.tipas == 'Islaidos':
                suma -= irasas.suma
        print('Balansas', suma)

    def parodyti_ataskaita(self):   # kuris atspausdintų visus pajamų ir išlaidų įrašus (nurodydamas kiekvieno įrašo tipą ir sumą).
        for i in self.zurnalas:
             print(i)


biudzetas = Biudzetas()

while True:
    print('============================================================================')
    print('Pasirinkite viena is punktu:')
    print('1. Ivesti pajamas...')
    print('2. Ivesti islaidas...')
    print('3. Parodyti pajamu/islaidu balansa...')
    print('4. Parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis...')
    print('5. Iseiti')
    print('============================================================================')
    var = int(input('Jusu pasirinkimas: '))
    match var:
        case 1:
            # tipas = input('Kokios pajamos: ')
            suma = float(input('Pajamu suma: '))
            biudzetas.prideti_pajamu_irasa(suma)
        case 2:
            # tipas = input('Kokios islaidos: ')
            suma = float(input('Gautos islaido: '))
            biudzetas.prideti_islaidu_irasa(suma)
        case 3:
            biudzetas.gauti_balansą()
        case 4:
            print('Biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis')
            biudzetas.parodyti_ataskaita()
        case 5:
            break