'''
Cia aprasyta kas veikia siame kode
Zaidzia Algoritmas pries Vartotoja
Teisingai fiksuoja žaidėjo laimėjimą ir stabdo žaidimą
Žaidimas vyksta konsolėje
Sukurtą žaidimą paskelbti github repozitorijoje, nuorodą paskelbti teamsuose, tam skirtoje užduotyje (Assignments)
Kad baigus žaidimą, programa neišsijungtų, o leistų pakartoti žaidimą. Taip pat būtų galimybė išjungti programą
Kad žaidimas skaičiuotų abiejų žaidėjų sesijos laimėjimus.
Leistų žaisti prieš kompiuterį (sukurti logiką, kaip jis elgsis)
'''
import random
import time


def tikrinamx(kartai):

    x = kartai

    '''tikrinu horizontaliai'''
    if 'X' == str(xo[0][0]) and 'X' == str(xo[0][1]) and 'X' == str(xo[0][2]):
        print('>>>>>> X laimejo <<<<<<')
        print()
        return 9
    if 'X' == str(xo[1][0]) and 'X' == str(xo[1][1]) and 'X' == str(xo[1][2]):
        print('>>>>>> X laimejo <<<<<<')
        print()
        return 9
    if 'X' == str(xo[2][0]) and 'X' == str(xo[2][1]) and 'X' == str(xo[2][2]):
        print('>>>>>> X laimejo <<<<<<')
        print()
        return 9

    '''tikrinu vertikaliai'''
    if 'X' == str(xo[0][0]) and 'X' == str(xo[1][0]) and 'X' == str(xo[2][0]):
        print('>>>>>> X laimejo <<<<<<')
        print()
        return 9
    if 'X' == str(xo[0][1]) and 'X' == str(xo[1][1]) and 'X' == str(xo[2][1]):
        print('>>>>>> X laimejo <<<<<<')
        print()
        return 9
    if 'X' == str(xo[0][2]) and 'X' == str(xo[1][2]) and 'X' == str(xo[2][2]):
        print('>>>>>> X laimejo <<<<<<')
        print()
        return 9

    '''tikrinu kryzmai'''
    if 'X' == str(xo[0][0]) and 'X' == str(xo[1][1]) and 'X' == str(xo[2][2]):
        print('>>>>>> X laimejo <<<<<<')
        print()
        return 9
    if 'X' == str(xo[2][0]) and 'X' == str(xo[1][1]) and 'X' == str(xo[0][2]):
        print('>>>>>> X laimejo <<<<<<')
        print()
        return 9
    else:
        return x


def tikrinamo(kartai):

    x = kartai

    '''tikrinu horizontaliai'''
    if 'O' == str(xo[0][0]) and 'O' == str(xo[0][1]) and 'O' == str(xo[0][2]):
        print('>>>>>> O laimejo <<<<<<')
        print()
        return 10
    if 'O' == str(xo[1][0]) and 'O' == str(xo[1][1]) and 'O' == str(xo[1][2]):
        print('>>>>>> O laimejo <<<<<<')
        print()
        return 10
    if 'O' == str(xo[2][0]) and 'O' == str(xo[2][1]) and 'O' == str(xo[2][2]):
        print('>>>>>> O laimejo <<<<<<')
        print()
        return 10

    '''tikrinu vertikaliai'''
    if 'O' == str(xo[0][0]) and 'O' == str(xo[1][0]) and 'O' == str(xo[2][0]):
        print('>>>>>> O laimejo <<<<<<')
        print()
        return 10
    if 'O' == str(xo[0][1]) and 'O' == str(xo[1][1]) and 'O' == str(xo[2][1]):
        print('>>>>>> O laimejo <<<<<<')
        print()
        return 10
    if 'O' == str(xo[0][2]) and 'O' == str(xo[1][2]) and 'O' == str(xo[2][2]):
        print('>>>>>> O laimejo <<<<<<')
        print()
        return 10

    '''tikrinu kryzmai'''
    if 'O' == str(xo[0][0]) and 'O' == str(xo[1][1]) and 'O' == str(xo[2][2]):
        print('>>>>>> O laimejo <<<<<<')
        print()
        return 10
    if 'O' == str(xo[2][0]) and 'O' == str(xo[1][1]) and 'O' == str(xo[0][2]):
        print('>>>>>> O laimejo <<<<<<')
        print()
        return 10
    else:
        return x


def zulikas():

    '''deda vidurini kryziuka tarp kitu kryziuku horizontalioje padetyje'''
    if 'X' == str(xo[0][0]) and 'X' == str(xo[0][2]) and 'X' != str(xo[0][1]) and 'O' != str(xo[0][1]):
        xo[0][1] = 'X'
        return
    if 'X' == str(xo[1][0]) and 'O' == str(xo[1][2]) and 'O' != str(xo[1][1]) and 'X' != str(xo[1][1]):
        xo[1][1] = 'X'
        return
    if 'X' == str(xo[2][0]) and 'X' == str(xo[2][2]) and 'O' != str(xo[2][1]) and 'X' != str(xo[2][1]):
        xo[2][1] = 'X'
        return

    '''deda vidurini kryziuka tarp kitu kryziuku vertikalioje padetyje'''
    if 'X' == str(xo[0][0]) and 'X' == str(xo[2][0]) and 'X' != str(xo[1][0]) and 'O' != str(xo[1][0]):
        xo[1][0] = 'X'
        return
    if 'X' == str(xo[0][1]) and 'X' == str(xo[2][1]) and 'O' != str(xo[1][1]) and 'X' != str(xo[1][1]):
        xo[1][1] = 'X'
        return
    if 'X' == str(xo[0][2]) and 'X' == str(xo[2][2]) and 'O' != str(xo[1][2]) and 'X' != str(xo[1][2]):
        xo[1][2] = 'X'
        return

    '''deda vidurini kryziuka jei kampuose kryziukai'''
    if 'X' == str(xo[0][0]) and 'O' == str(xo[2][2]) and 'X' != str(xo[1][1]) and 'O' != str(xo[1][1]):
        xo[1][1] = 'X'
        return
    if 'X' == str(xo[2][0]) and 'X' == str(xo[0][2]) and 'O' != str(xo[1][1]) and 'X' != str(xo[1][1]):
        xo[1][1] = 'X'
        return

    '''Deda horizontaliai kryziuka desineje puseje'''
    if 'X' == str(xo[0][0]) and 'X' == str(xo[0][1]) and 'X' != str(xo[0][2]) and 'O' != str(xo[0][2]):
        xo[0][2] = 'X'
        return
    if 'X' == str(xo[1][0]) and 'X' == str(xo[1][1]) and 'O' != str(xo[1][2]) and 'X' != str(xo[1][2]):
        xo[1][2] = 'X'
        return
    if 'X' == str(xo[2][0]) and 'X' == str(xo[2][1]) and 'O' != str(xo[2][2]) and 'X' != str(xo[2][2]):
        xo[2][2] = 'X'
        return

    '''Deda horizontaliai kryziuka kaireje puseje'''
    if 'X' != str(xo[0][0]) and 'O' != str(xo[0][0]) and 'X' == str(xo[0][1]) and 'X' == str(xo[0][2]):
        xo[0][0] = 'X'
        return
    if 'X' != str(xo[1][0]) and 'O' != str(xo[1][0]) and 'X' == str(xo[1][1]) and 'X' == str(xo[1][2]):
        xo[1][0] = 'X'
        return
    if 'X' != str(xo[2][0]) and 'O' != str(xo[2][0]) and 'X' == str(xo[2][1]) and 'X' == str(xo[2][2]):
        xo[2][0] = 'X'
        return

    '''deda kryziuka vertikaliai 3 eilute'''
    if 'X' == str(xo[0][0]) and 'X' == str(xo[1][0]) and 'O' != str(xo[2][0]) and 'X' != str(xo[2][0]):
        xo[2][0] = 'X'
        return
    if 'X' == str(xo[0][1]) and 'X' == str(xo[1][1]) and 'O' != str(xo[2][1]) and 'X' != str(xo[2][1]):
        xo[2][1] = 'X'
        return
    if 'X' == str(xo[0][2]) and 'X' == str(xo[1][2]) and 'O' != str(xo[2][2]) and 'X' != str(xo[2][2]):
        xo[2][2] = 'X'
        return

    '''deda kryziuka vertikaliai 1 eilute'''
    if 'X' == str(xo[2][0]) and 'X' == str(xo[1][0]) and 'O' != str(xo[0][0]) and 'X' != str(xo[0][0]):
        xo[0][0] = 'X'
        return
    if 'X' == str(xo[2][1]) and 'X' == str(xo[1][1]) and 'O' != str(xo[0][1]) and 'X' != str(xo[0][1]):
        xo[0][1] = 'X'
        return
    if 'X' == str(xo[2][2]) and 'X' == str(xo[1][2]) and 'O' != str(xo[0][2]) and 'X' != str(xo[0][2]):
        xo[0][2] = 'X'
        return

    '''tikrinu horizontaliai 1 stulpeli'''
    if 'O' != str(xo[0][0]) and 'X' != str(xo[0][0]) and 'O' == str(xo[0][1]) and 'O' == str(xo[0][2]):
        xo[0][0] = 'X'
        return
    if 'O' != str(xo[1][0]) and 'X' != str(xo[1][0]) and 'O' == str(xo[1][1]) and 'O' == str(xo[1][2]):
        xo[1][0] = 'X'
        return
    if 'O' != str(xo[2][0]) and 'X' != str(xo[2][0]) and 'O' == str(xo[2][1]) and 'O' == str(xo[2][2]):
        xo[2][0] = 'X'
        return

    '''tikrinu horizontaliai 2 stulpeli'''
    if 'O' == str(xo[0][0]) and 'O' != str(xo[0][1]) and 'X' != str(xo[0][1]) and 'O' == str(xo[0][2]):
        xo[0][1] = 'X'
        return
    if 'O' == str(xo[1][0]) and 'O' != str(xo[1][1]) and 'O' == str(xo[2][2]) and 'X' != str(xo[1][1]):
        xo[1][1] = 'X'
        return
    if 'O' == str(xo[2][0]) and 'O' != str(xo[2][1]) and 'O' == str(xo[2][2]) and 'X' != str(xo[2][1]):
        xo[2][1] = 'X'
        return

    '''tikrinu horizontaliai 3 stulpeli'''
    if 'O' == str(xo[0][0]) and 'O' == str(xo[0][1]) and 'X' != str(xo[0][2]) and 'O' != str(xo[0][2]):
        xo[0][2] = 'X'
        return
    if 'O' == str(xo[1][0]) and 'O' == str(xo[1][1]) and 'O' != str(xo[1][2]) and 'X' != str(xo[1][2]):
        xo[1][2] = 'X'
        return
    if 'O' == str(xo[2][0]) and 'O' == str(xo[2][1]) and 'O' != str(xo[2][2]) and 'X' != str(xo[2][2]):
        xo[2][2] = 'X'
        return

    '''tikrinu vertikaliai 1 eilute'''
    if 'O' != str(xo[0][0]) and 'X' != str(xo[0][0]) and 'O' == str(xo[1][0]) and 'O' == str(xo[2][0]):
        xo[0][0] = 'X'
        return
    if 'O' != str(xo[0][1]) and 'X' != str(xo[0][1]) and 'O' == str(xo[1][1]) and 'O' == str(xo[2][1]):
        xo[0][1] = 'X'
        return
    if 'O' != str(xo[0][2]) and 'X' != str(xo[0][2]) and 'O' == str(xo[1][2]) and 'O' == str(xo[2][2]):
        xo[0][2] = 'X'
        return

    '''tikrinu vertikaliai 2 eilute'''
    if 'O' == str(xo[0][0]) and 'X' != str(xo[1][0]) and 'O' != str(xo[1][0]) and 'O' == str(xo[2][0]):
        xo[1][0] = 'X'
        return
    if 'O' == str(xo[0][1]) and 'X' != str(xo[1][1]) and 'O' != str(xo[1][1]) and 'O' == str(xo[2][1]):
        xo[1][1] = 'X'
        return
    if 'O' == str(xo[0][2]) and 'X' != str(xo[1][2]) and 'O' != str(xo[1][2]) and 'O' == str(xo[2][2]):
        xo[1][2] = 'X'
        return

    '''tikrinu vertikaliai 3 eilute'''
    if 'O' == str(xo[0][0]) and 'O' == str(xo[1][0]) and 'O' != str(xo[2][0]) and 'X' != str(xo[2][0]):
        xo[2][0] = 'X'
        return
    if 'O' == str(xo[0][1]) and 'O' == str(xo[1][1]) and 'O' != str(xo[2][1]) and 'X' != str(xo[2][1]):
        xo[2][1] = 'X'
        return
    if 'O' == str(xo[0][2]) and 'O' == str(xo[1][2]) and 'O' != str(xo[2][2]) and 'X' != str(xo[2][2]):
        xo[2][2] = 'X'
        return

    '''tikrinu kryzmai desines puses kampinius skaicius'''
    if 'O' == str(xo[0][0]) and 'O' == str(xo[1][1]) and 'O' != str(xo[2][2]) and 'X' != str(xo[2][2]):
        xo[2][2] = 'X'
        return
    if 'O' == str(xo[2][0]) and 'O' == str(xo[1][1]) and 'O' != str(xo[0][2]) and 'X' != str(xo[0][2]):
        xo[0][2] = 'X'
        return

    '''tikrinu kryzmai kaires puses kampinius skaicius'''
    if 'O' != str(xo[0][0]) and 'X' != str(xo[0][0]) and 'O' == str(xo[1][1]) and 'O' == str(xo[2][2]):
        xo[0][0] = 'X'
        return
    if 'O' != str(xo[2][0]) and 'X' != str(xo[2][0]) and 'O' == str(xo[1][1]) and 'O' == str(xo[0][2]):
        xo[2][0] = 'X'
        return

    '''tikrinu kryzmai vidurini skaiciu'''
    if 'O' == str(xo[0][0]) and 'X' != str(xo[1][1]) and 'O' != str(xo[1][1]) and 'O' == str(xo[2][2]):
        xo[1][1] = 'X'
        return
    if 'O' == str(xo[2][0]) and 'X' != str(xo[1][1]) and 'O' != str(xo[1][1]) and 'O' == str(xo[0][2]):
        xo[2][0] = 'X'
        return
    else:
        a = random.randint(0, 2)
        b = random.randint(0, 2)
        deliojam(a, b)


def tikrinu_ivedima():
    ieskom = 0
    while True:
        x = input('Kuri skaiciu pakeisti O-u: ')
        if x.isdigit():
            x = int(x)
            if 0 < x < 10:
                break
            else:
                print('Netinkamas skaicius')
                time.sleep(2)
                spausdinam(xo)
        else:
            print('Ivestas netinkamas simbolis')
            time.sleep(2)
            spausdinam(xo)
    while ieskom == 0:
        for i in range(len(xo)):
            p = 0
            for s in xo[i]:
                if s == str(x):
                    ieskom += 1
                    break
                else:
                    p += 1
        if ieskom != 1:
            print('Langelis uzimtas, pasirinkite kita')
            x = input('Kuri skaiciu pakeisti O-u: ')
            print()
    for i in range(len(xo)):
        p = 0
        for s in xo[i]:
            if s == str(x):
                xo[i][p] = 'O'
                p = 0
                break
            else:
                p += 1


def rezultatas():
    print()
    print("rezultatas")
    print(f'X laimejo {sumx}')
    print(f'O laimejo {sumo}')
    print()
    time.sleep(2)


def spausdinam(lenta):
    for ii in lenta:
        print(ii)
    print()


def deliojam(a, b):
    while xo[a][b] == 'X' or xo[a][b] == 'O':
        a = random.randint(0, 2)
        b = random.randint(0, 2)
    xo[a][b] = 'X'


def pilna_lentele(kartai):
    if kartai == 8:
        print('Zaidimas baigtas!')
        x = gameover()
        return x


def lenta():
    xo = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9']]
    spausdinam(xo)
    return


def gameover():
    print('Kartoti zaidima?')
    print('(1 - Taip) (2 - Ne)')
    var = int(input('Jusu pasirinkimas: '))
    match var:
        case 1:
            rezultatas()
            return 8
        case 2:
            rezultatas()
            exit()


print('Pradeti zaidima 1')
print('Iseiti__________2')
var = int(input('Juru pasirinkimas: '))
p = 0
kartai = 0
o = 0
sumx = 0
sumo = 0
xo = [['1', '2', '3'],
      ['4', '5', '6'],
      ['7', '8', '9']]

if var == 1:
    print()
    print('Kompiuteris valdo X-us')
    print('Jus valdote O-us')
    print()
    time.sleep(2)

while True:
    xo = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9']]
    kartai = 0
    match var:
        case 1:
            for kartai in range(9):
                if kartai % 2 == 0:
                    print('......Pentiumas kaupiasi......')
                    print()
                    time.sleep(1)
                    zulikas()
                    spausdinam(xo)
                    kartai = tikrinamx(kartai)
                    if kartai == 9:
                        sumx += 1
                        kartai = 8
                    pilna_lentele(kartai)
                    if kartai == 8:
                        break
                else:
                    tikrinu_ivedima()
                    spausdinam(xo)
                    kartai = tikrinamo(kartai)
                    if kartai == 10:
                        sumo += 1
                        kartai = 8
                    pilna_lentele(kartai)
                    if kartai == 8: break
        case 2:
            print('Laimingai !')
