
class Pelilauta():
    def __init__(self, pelaajan_merkki: str, ai_vs_ai: bool):
        self.laudan_koko = 25
        self.viimeisin_siirto = 1, 1
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
        #self.lauta.append([str(n) for n in range(1, 25)])
        for i in range(self.laudan_koko):
            rivi = [] #[str(i + 1)]
            ([rivi.append("_") for j in range(self.laudan_koko)])
            self.lauta.append(rivi)
    
    def siirto(self, koordinaatit: str, nappula: str):
        if " " in koordinaatit:
            siirto = koordinaatit.split(" ")
            if siirto[0].isnumeric() and siirto[1].isnumeric():
                x, y = int(siirto[0]) - 1, int(siirto[1]) - 1

                if x < self.laudan_koko and y < self.laudan_koko and x >= 0 and y >= 0 and self.lauta[x][y] == "_":
                    self.lauta[x][y] = nappula
                    self.viimeisin_siirto = x, y
                    return True

        return False


if False:
    asd = Pelilauta("X", False)
    print(asd.siirto(16, 5, "X"))
    print(asd.siirto(16, 5, "Y"))
    for row in asd.lauta:
        print(row)
