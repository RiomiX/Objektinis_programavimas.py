def bandom(args):
    mas = []
    n = 0
    s = 0
    # args = input('Asmens kodas: ')
    print(args[1])
    mas.append(int(args))
    print(mas)
    quit()
    # for i in range(11):
    #     mas.append(int(args[i]))
    for i in range(10):
        n += 1
        s += (int(mas[i] * n))
        if n == 9:
            n = 0
    if s % 11 != 10 and s % 11 == int(mas[10]):
        K = s
        print('Asmens kodas valydus')
    elif s % 11 == 10:
        n = 2
        K = 0
        for i in range(10):
            n += 1
            mas.append(int(args[i]))
            K += int(i) * n
            if n == 9:
                n = 0
        if K % 11 != 10 and K % 11 == int(mas[10]):
            K = K % 11
        elif K % 11 == 10:
                K = 0
        else:
            print('Deport, a/k invalid')
    else:
        print('Deport, a/k invalid')
    print('Happy End')

ak = input('Iveskite asmens koda: ')
bandom(ak)