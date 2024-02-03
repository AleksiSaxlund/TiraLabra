
class Pelilauta():
    """Pelilautaa esittävä luokka.
    """

    def __init__(self, pelaajan_merkki: str, ai_vs_ai: bool):
        self.laudan_koko = 20
        self.viimeisin_siirto = 1, 1
        if not ai_vs_ai:
            self.nappulat(pelaajan_merkki)

        self.luo_pelilauta()

    def nappulat(self, pelaajan_merkki: str):
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
        for i in range(self.laudan_koko):
            rivi = []
            ([rivi.append("_") for j in range(self.laudan_koko)])
            self.lauta.append(rivi)
        
        self.a = [
            ['O','O','_','_','O','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_'],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_']]

    def siirto(self, syote: str, nappula: str):
        """Tekee siirron pelilaudalle. Varmistaa ensin, että siirto on laillinen.
            Muokkaa myös pelaajan syötteen sopivaan formaattiin.

        Args:
            syote (str): Raaka syöte pelaajalta.
            nappula (str): Siirrettävä nappula.

        Returns:
            bool: True, jos onnistuis. False, jos ei.
        """
        if nappula in ("X", "O"):

            if " " in syote:
                siirto = syote.split(" ")
                if len(list(siirto)) == 2:
                    if siirto[0].isnumeric() and siirto[1].isnumeric():
                        x, y = int(siirto[0]) - 1, int(siirto[1]) - 1

                        if x < self.laudan_koko and y < self.laudan_koko and x >= 0 and y >= 0 and self.lauta[x][y] == "_":
                            self.lauta[x][y] = nappula
                            self.viimeisin_siirto = x, y
                            return True, x, y

        return False, None, None
