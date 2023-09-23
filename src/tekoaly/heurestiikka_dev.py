
def etsi_jonot(lauta):
    n = len(lauta)
    laudan_arvo = 0

    # vaaka tarkistus
    for i in range(n):
        for j in range(n - 4):
            jono = lauta[i][j : j + 5]

    # pysty tarkistus
    for i in range(n):
        for j in range(n - 4):
            jono = []
            for x in range(5):
                jono.append(lauta[j + x][i])
    
    # diagonaali vasemmalta alas tarkistus
    for i in range(n - 4):
        for j in range(n - 4):
            jono = []
            for x in range(5):
                jono.append(lauta[i + x][j + x])

    # diagonaali oikealta alas tarkistus
    for i in range(n - 4):
        for j in range(n - 1, 3, -1):
            jono = []
            for x in range(5):
                jono.append(lauta[i + x][j - x])

def arvioi_jono(jono, koordinaatti1: tuple, koordinaatti2: tuple):
    pass


lauta = [[(i, j) for j in range(6)] for i in range(6)]
[print(a) for a in lauta]

etsi_jonot(lauta)