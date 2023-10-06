
class Pelilauta():
    """Pelilautaa esittävä luokka.
    """

    def __init__(self, pelaajan_merkki: str, ai_vs_ai: bool):
        self.laudan_koko = 25
        self.viimeisin_siirto = 1, 1
        if not ai_vs_ai:
            self.nappulat(pelaajan_merkki)

        self.luo_pelilauta()

    def nappulat(self, pelaajan_merkki):
        """Määrittää pelaajan, ja tekoälyn nappulan.

        Args:
            pelaajan_merkki (str): X tai O. Riippuen pelaajan valinnasta
        """
        merkit = ["X", "O"]
        merkit.remove(pelaajan_merkki)
        self.pelaajan_merkki = pelaajan_merkki
        self.vihu = merkit[0]

    def luo_pelilauta(self):
        """Luo pelilautaa esittävän matriisin.
        """
        self.lauta = []
        # self.lauta.append([str(n) for n in range(1, 25)])
        for i in range(self.laudan_koko):
            rivi = []
            ([rivi.append("_") for j in range(self.laudan_koko)])
            self.lauta.append(rivi)

    def siirto(self, x: str , y: str, nappula: str):
        """Tekee siirron pelilaudalle. Varmistaa ensin, että siirto on laillinen.
            Muokkaa myös pelaajan syötteen sopivaan formaattiin.

        Args:
            koordinaatit (str): Raaka syöte pelaajalta.
            nappula (str): Siirrettävä nappula.

        Returns:
            bool: True, jos onnistuis. False, jos ei.
        """
        if nappula in ("X", "O"):

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
