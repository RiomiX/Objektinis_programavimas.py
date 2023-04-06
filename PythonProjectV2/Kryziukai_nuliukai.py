class Zaidimas:
    def __int__(self):
        self.lentele = []

    def ox(self, ox):
        self.ox = ox
        for i in ox:
            print(i)

    def x(self, x):
        self.x = x
        for i in self.lentele:
            if i == x:
                self.lentele.append(x)
                return self.lentele

xo = [[1,2,3],
      [4,5,6],
      [7,8,9]]

xo = Zaidimas.ox(xo)

while True:
    print('Jusu ejimas: ')
    x = int(input('Kuri skaiciu pakeisti X: '))
    Zaidimas.ox(x)
    break