# def sks(args):
#     kiekis = len(args)
#     if kiekis % 2 == 0:
#         x = kiekis // 2
#         return int(args[:4]) == int(args[4:])   # gauname True arba False jei skaiciu kiekis lyginis
#     else:
#         psk = args[:-1]
#         kiekis = len(psk)
#         x = kiekis // 2
#         return int(args[:4]) == int(psk[4:])    # gauname True arba False, bet ivestu skaiciu kiekis nelyginis, tai pries tai atimame, ir priskiriame nauja kintamaji
#
# ss = input('Ivesk skaiciu seka: ')
# sks(ss)
# print(sks(ss))

# sioje uzduoty irasom skaiciu seka, ir atskirdami kiekviena skaiciu paraso gretimus skaicius

# def yzy(args):
#     for i in range(len(args)):
#         x = int(args[i])
#         print('Skaicius ', x, 'turi salia', x-1, 'ir', x+1)
#
# sk = input('Ivesk skaiciu seka: ')
# yzy(sk)
