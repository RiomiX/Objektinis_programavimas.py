# 1 užduotis ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Sukurti programą, kuri:
# Turėtų klasę Automobilis
# Automobilis turėtų savybes: metai, modelis, kuro_tipas
# Automobilis turėtų metodus: vaziuoti, stoveti, pildyti_degalu, kurie atitinkamai atspausdintų „Važiuoja“, „Priparkuota“, „Degalai įpilti“
# Sukūrus objektą, automatiškai atspausdintų automobilio metus, modelį ir kuro tipą
# Turėtų klasę Elektromobilis (jo tėvinis objektas – Automobilis)
# Elektromobilis pakeistų Automobilio metodą pildyti_degalu taip, kad jis atspausdintų „Baterija įkrauta“
# Elektromobilis turėtų metodą vaziuoti_autonomiskai, kuris spausdintų „Važiuoja autonomiškai“
# Sukurti norimą Automobilio objektą
# Sukurti norimą Elektromobilio objektą
# Su sukurtu Automobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu
# Su sukurtu Elektromobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu, vaziuoti_autonomiskai

class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas

    def __str__(self):
        return f'Metai {self.metai}, modelis {self.modelis}, kuro tipas {self.kuro_tipas}'

class vidaus_degimo(Automobilis):
    def vaziuoti(self):
        print('vaziuoja')

    def stoveti(self):
        print('Priparkuota')

    def pil_deg(self):
        print('Degalai ipilti')

class elektrinis(Automobilis):
    def vaziuoti(self):
        print('vaziuoja tyliai')

    def stoveti(self):
        print('Priparkuota')

    def pil_deg(self):
        print('Baterija ikrauta')

    def vz_aut(self):
        print('Vaziuoja autonomiskai')

def __str__(self):
    return f'Metai {self.metai}, modelis {self.modelis}, kuro tipas {self.kuro_tipas}'

opel = vidaus_degimo(1900, 'opel', 'malkos')
zaz = elektrinis(2007, 'zaz', 'elektra')
zero = vidaus_degimo(2077, 'zero', 'raketinis kuras')

auto1 = vidaus_degimo(1999, 'Audi', 'Dizel')
auto2 = elektrinis(2010, 'Nissan', 'Batarkes')

print(zaz)
print(zero)
print(opel)
print(zero)
zaz.vz_aut()
print(auto1)
auto1.vaziuoti()
auto1.stoveti()
auto1.pil_deg()
print(auto2)
auto2.vaziuoti()
auto2.stoveti()
auto2.pil_deg()
auto2.vz_aut()


# 2 užduotis +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Sukurti programą, kuri:
# Turėtų klasę Darbuotojas
# Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo
# Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki šiandien (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)
# Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu, paskaičiuotų bendrą atlyginimą (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
# Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų atlyginimą, dirbant darbuotojui 5 dienas per savaitę
# Sukurti norimą Darbuotojo objektą
# Sukurti norimą NormalusDarbuotojas objektą
# Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima


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

# 3 užduotis    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#   Patobulinti objektinio programavimo 1 pamokos biudžeto programą:
#   Sukurti tėvinę klasę Irasas, kurioje būtų savybės suma , iš kurios klasės PajamuIrasas ir IslaiduIrasas paveldėtų visas savybes.
#   Į klasę PajamuIrasas papildomai pridėti savybes siuntejas ir papildoma_informacija, kurias vartotojas galėtų įrašyti.
#   Į klasę IslaiduIrasas papildomai pridėti savybes atsiskaitymo_budas ir isigyta_preke_paslauga, kurias vartotojas galėtų įrašyti.
#   Atitinkamai perdaryti klasės Biudzetas metodus gauti_balansa ir gauti_ataskaita kad pasiėmus įrašą iš žurnalo, atpažintų,
# ar tai yra pajamos ar išlaidos (pvz., panaudojus isinstance() metodą) ir atitinkamai atliktų veiksmus.
#   Padaryti, kad vartotojui (per konsolę) būtų leidžiama įrašyti pajamų ir išlaidų įrašus, peržiūrėti balansą ir ataskaitą.

