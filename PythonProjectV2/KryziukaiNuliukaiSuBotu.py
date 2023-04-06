import random
import time


def spausdinam(lenta):
    for ii in lenta:
        print(ii)


def tiktinam():
    '''tikrinu horizontaliai'''
    if 'X' == str(xo[0][0]) and 'X' == str(xo[0][1]) and 'X' == str(xo[0][2]):
        return print('>>>>>> X laimejo <<<<<<'), exit(time.sleep(2))
    if 'X' == str(xo[1][0]) and 'X' == str(xo[1][1]) and 'X' == str(xo[1][2]):
        return print('>>>>>> X laimejo <<<<<<'), exit(time.sleep(2))
    if 'X' == str(xo[2][0]) and 'X' == str(xo[2][1]) and 'X' == str(xo[2][2]):
        return print('>>>>>> X laimejo <<<<<<'), exit(time.sleep(2))
    '''tikrinu vertikaliai'''
    if 'X' == str(xo[0][0]) and 'X' == str(xo[1][0]) and 'X' == str(xo[2][0]):
        return print('>>>>>> X laimejo <<<<<<'), exit(time.sleep(2))
    if 'X' == str(xo[0][1]) and 'X' == str(xo[1][1]) and 'X' == str(xo[2][1]):
        return print('>>>>>> X laimejo <<<<<<'), exit(time.sleep(2))
    if 'X' == str(xo[0][2]) and 'X' == str(xo[1][2]) and 'X' == str(xo[2][2]):
        return print('>>>>>> X laimejo <<<<<<'), exit(time.sleep(2))
    '''tikrinu kryzmai'''
    if 'X' == str(xo[0][0]) and 'X' == str(xo[1][1]) and 'X' == str(xo[2][2]):
        return print('>>>>>> X laimejo <<<<<<'), exit(time.sleep(2))
    if 'X' == str(xo[2][0]) and 'X' == str(xo[1][1]) and 'X' == str(xo[0][2]):
        return print('>>>>>> X laimejo <<<<<<'), exit(time.sleep(2))
    '''ta pati tik su O'''
    '''tikrinu horizontaliai'''
    if 'O' == str(xo[0][0]) and 'O' == str(xo[0][1]) and 'O' == str(xo[0][2]):
        return print('>>>>>> O laimejo <<<<<<'), exit(time.sleep(2))
    if 'O' == str(xo[1][0]) and 'O' == str(xo[1][1]) and 'O' == str(xo[1][2]):
        return print('>>>>>> O laimejo <<<<<<'), exit(time.sleep(2))
    if 'O' == str(xo[2][0]) and 'O' == str(xo[2][1]) and 'O' == str(xo[2][2]):
        return print('>>>>>> O laimejo <<<<<<'), exit(time.sleep(2))
    '''tikrinu vertikaliai'''
    if 'O' == str(xo[0][0]) and 'O' == str(xo[1][0]) and 'O' == str(xo[2][0]):
        return print('>>>>>> O laimejo <<<<<<'), exit(time.sleep(2))
    if 'O' == str(xo[0][1]) and 'O' == str(xo[1][1]) and 'O' == str(xo[2][1]):
        return print('>>>>>> O laimejo <<<<<<'), exit(time.sleep(2))
    if 'O' == str(xo[0][2]) and 'O' == str(xo[1][2]) and 'O' == str(xo[2][2]):
        return print('>>>>>> O laimejo <<<<<<'), exit(time.sleep(2))
    '''tikrinu kryzmai'''
    if 'O' == str(xo[0][0]) and 'O' == str(xo[1][1]) and 'O' == str(xo[2][2]):
        return print('>>>>>> O laimejo <<<<<<'), exit(time.sleep(2))
    if 'O' == str(xo[2][0]) and 'O' == str(xo[1][1]) and 'O' == str(xo[0][2]):
        return print('>>>>>> O laimejo <<<<<<'), exit(time.sleep(2))


print('Pradeti zaidima 1')
print('Iseiti__________2')
var = int(input('Juru pasirinkimas: '))
p = 0
xo = []

if var == 1:
    xo = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9']]
    spausdinam(xo)

kartai = 1

match var:
    case 1:
        for kartai in range(9):
            if kartai % 2 == 0:
                print('......Pentiumas kaupiasi......')
                time.sleep(2)
                a = random.randint(0, 2)
                b = random.randint(0, 2)
                while xo[a][b] == 'X' or xo[a][b] == 'O':
                    a = random.randint(0, 2)
                    b = random.randint(0, 2)
                xo[a][b] = 'X'
                spausdinam(xo)
                tiktinam()
                if kartai == 8:
                    print('Lentele pilna, niekas nelaimejo!')
                    break
            else:
                try:
                    x = int(input('Kuri skaiciu pakeisti O-u: '))
                except:
                    print('Netinkamas simbolis')
                    time.sleep(2)
                    break
                for i in range(len(xo)):
                    p = 0
                    for s in xo[i]:
                        if s == str(x):
                            xo[i][p] = 'O'
                            p = 0
                        else:
                            p += 1
                spausdinam(xo)
                tiktinam()
                if kartai == 8:
                    print('Lentele pilna, niekas nelaimejo!')
                    break
    case 2:
        print('Laimingai !')
