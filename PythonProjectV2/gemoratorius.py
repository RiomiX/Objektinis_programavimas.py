def bandom(args):
    import random
    bingo = 0
    vm = mas1[0]
    while bingo == 0:
        mas = []
        n = 0
        s = 0
        mas.append(vm)
        ml = random.randint(1, 99)
        if ml < 10:
            mas.append(0)
            mas.append(ml)
        else:
            mas.append(ml)
        mnl = random.randint(1, 12)
        if mnl < 10:
            mas.append(0)
            mas.append(mnl)
        else:
            mas.append(mnl)
        if mnl < 29:
            dl = random.randint(1, 28)
            if dl < 10:
                mas.append(0)
                mas.append(dl)
            else:
                mas.append(dl)
        else:
            dl = random.randint(1, 28)
            if dl < 10:
                mas.append(0)
                mas.append(dl)
            else:
                mas.append(dl)
        el = random.randint(1, 999)
        if el < 10:
            mas.append(0)
            mas.append(0)
            mas.append(el)
        elif el < 100:
            mas.append(0)
            mas.append(el)
        else:
            mas.append(el)
        kl = random.randint(0, 9)
        mas.append(kl)
        mas2 = ''.join(map(str, mas))
        print(mas2)
        K = mas2[-1]
        for i in range(10):
            n += 1
            s += (int(mas2[i])) * n
            if n == 9:
                n = 0
        if s % 11 != 10 and s % 11 == K:
            print('Asmens kodas valydus')
            bingo += 1
        elif s % 11 == 10:
            n = 2
            sumka = 0
            for i in range(10):
                n += 1
                sumka += (int(mas2[i])) * n
                if n == 9:
                    n = 0
            if sumka % 11 != 10 and sumka % 11 == K:
                bingo += 1
                print('Asmens kodas valydus')
            elif (sumka % 11) == 10 and 0 == (int(mas2[10])):
                print('Asmens kodas valydus')
                bingo += 1
        mas.clear()
    print('Happy End')


mas1 = []

print('Pasirinkite lyti: 1 - Vyras, 2 - Moteris')
ak = int(input('Jusu pasirinkimas: '))
print('Pasirinkite kuriame amziuje gymes(-usi):')
print('1 - XIXa, 2 - XXa, 3 - XXIa')
ak2 = int(input('Jusu pasirinkimas: '))
if ak == 1:
    if ak2 == 1:
        mas1.append(1)
    if ak2 == 2:
        mas1.append(3)
    if ak2 == 3:
        mas1.append(5)
if ak == 2:
    if ak2 == 1:
        mas1.append(2)
    if ak2 == 2:
        mas1.append(4)
    if ak2 == 3:
        mas1.append(6)

bandom(mas1)
