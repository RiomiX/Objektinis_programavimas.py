def bandom(args):
    n = 0
    s = 0
    K = 0
    for i in range(10):
        n += 1
        s += (int(args[i])) * n
        if n == 9:
            n = 0
    if s % 11 != 10 and s % 11 == int(args[10]):
        print('Asmens kodas valydus')
    elif s % 11 == 10:
        n = 2
        for i in range(10):
            n += 1
            K += (int(args[i])) * n
            if n == 9:
                n = 0
        if (K % 11) != 10:
            if K % 11 == (int(args[10])):
                print('Asmens kodas valydus')
        elif (K % 11) == 10:
            if 0 == (int(args[10])):
                print('Asmens kodas valydus')
            else:
                print('Deport, a/k invalid')
    else:
        print('Deport, a/k invalid')
    print('Happy End')

ak = input('Iveskite asmens koda: ')
bandom(ak)