
class Pelilauta():
    def __init__(self, pelaajan_merkki: str, ai_vs_ai: bool):
        if not ai_vs_ai:
            self.nappulat(pelaajan_merkki)
        
        self.pelilauta()

    def nappulat(self, pelaajan_merkki):
        merkit = ["X", "O"]
        merkit.remove(pelaajan_merkki)
        self.pelaajan_merkki = pelaajan_merkki
        self.vihu = merkit[0]

    def pelilauta(self):
        self.lauta = []
        for i in range(25):
            self.lauta.append(["_" for j in range(25)])
    
    def siirto(self, x: int, y: int, nappula: str):
        if x >= 25 or y >= 25 or x < 0 or y < 0 or self.lauta[x][y] != "_":
            return False
        
        self.lauta[x][y] = nappula
        return True


if True:
    asd = Pelilauta("X", False)
    print(asd.siirto(16, 5, "X"))
    print(asd.siirto(16, 5, "Y"))
    for row in asd.lauta:
        print(row)
