'''5 užduotis:
Padaryti minibiudžeto programą, kuri:

Leistų vartotojui įvesti pajamas
Leistų vartotojui įvesti išlaidas
Leistų vartotojui parodyti pajamų/išlaidų balansą
Leistų vartotojui parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis)
Leistų vartotojui išeiti iš programos
Rekomendacija, kaip galima būtų padaryti:
Programa turi turėti klasę Irasas, kuri turėtų argumentus tipas (Pajamos arba Išlaidos) ir suma. Galima prirašyti str metodą, kuris gražintų, kaip bus atvaizduojamas spausdinamas objektas.
Programa turi turėti klasę Biudzetas, kurioje būtų:
Metodas init, kuriame sukurtas tuščias sąrašas zurnalas, į kurį bus dedami sukurti pajamų ir išlaidų objektai
Metodas prideti_pajamu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų pajamų objektą ir įdėtų jį į biudžeto žurnalą
Metodas prideti_islaidu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų išlaidų objektą ir įdėtų jį į biudžeto žurnalą
Metodas gauti_balansą(self), kuris gražintų žurnale laikomų pajamų ir išlaidų balansą.
Metodas parodyti_ataskaita(self), kuris atspausdintų visus pajamų ir išlaidų įrašus (nurodydamas kiekvieno įrašo tipą ir sumą).'''

class Irasas:
    def __init__(self, suma):
        self.suma = suma

    def __str__(self):
        return f'{self.suma}'

class Biudzetas:
    def __init__(self):
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma):
        pajamos = Irasas(suma)
        self.zurnalas.append(pajamos)

    def prideti_islaidu_irasa(self, suma):
        islaidos = Irasas(suma)
        self.zurnalas.append(islaidos)

    def gauti_balansą(self):
        suma = 0
        for i in self.zurnalas:
            suma += i
        for i in self.zurnalas:
            suma -= i
        print('Balansas: ', suma)



biudzetas = Biudzetas()

while True:
    var = int(input('Pasirinkite varianta: '))
    match var:
        case 1:
            suma = float(input('Iveskite pajamu suma: '))
            biudzetas.prideti_pajamu_irasa(suma)
        case 2:
            suma = float(input('Iveskite islaidu suma'))
            biudzetas.prideti_islaidu_irasa(suma)
        case 3:
            print('Balansas: ', biudzetas.gauti_balansą())

