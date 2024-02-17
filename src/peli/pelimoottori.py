from peli.kayttoliittyma import Kayttoliittyma
from peli.pelilauta import Pelilauta
from tekoaly.minimax import MiniMax
from time import time


class PeliMoottori():
    """Pelimoottori luokka. Vastaa pelin pyörittämisestä.
    """

    def __init__(self):
        self.kayttoliittyma = Kayttoliittyma()
        self.pelaaja = self.kayttoliittyma.alku()
        self.pelilauta = Pelilauta(self.pelaaja, False)
        self.tekoaly = MiniMax(self.pelilauta.lauta, self.pelaaja)
        self.peli_kierros()

    def peli_kierros(self):
        """Vastaa peli kierrosta. Poistuu tästä vasta kun on tullut voitto.
        """
        vuoro = 1

        while True:
            self.kayttoliittyma.tulosta_pelilauta(self.pelilauta.lauta)
            voitto = self.voiton_tarkistin()
            if voitto in ("X", "O"):
                print("voitto", voitto)
                break

            if vuoro == 1:
                if self.pelaaja == "X":
                    self.pelaajan_vuoro()
                else:
                    self.tekoalyn_vuoro()

            elif vuoro == -1:
                if self.pelaaja == "O":
                    self.pelaajan_vuoro()
                else:
                    self.tekoalyn_vuoro()

            vuoro *= -1

    def pelaajan_vuoro(self):
        """Kysyy pelaajalta syötettä niin kauan kunnes saa laillisen syötteen.
        """
        onnistunut = True
        while True:
            syote = self.kayttoliittyma.pelaajan_siirto_syote(onnistunut)

            hyvaksytty, x, y = self.pelilauta.siirto(syote, self.pelaaja)

            if hyvaksytty:
                self.tekoaly.lisaa_varattu_paikka(x-1, y-1)
                break

            onnistunut = False

    def tekoalyn_vuoro(self):
        alku = time()
        tekoalyn_siirto, loytynyt, voitto_siirto, voitto_nappi = self.tekoaly.valitse_paras_siirto()
        print(tekoalyn_siirto[0], tekoalyn_siirto[1])

        self.tekoaly.lisaa_varattu_paikka(
            tekoalyn_siirto[0], tekoalyn_siirto[1])
        print("aika", time() - alku)
        print("loytynyt voitto?", loytynyt)
        print("voitto siirto:", voitto_siirto, "napille:", voitto_nappi)

        self.pelilauta.tekoalyn_siirto(tekoalyn_siirto[0], tekoalyn_siirto[1], self.pelilauta.vihu)

    def voiton_tarkistin(self):
        """Tarkastaa onko pelilaudalle tullut voittoa. Viimeisimmäksi pelatun nappulan kohdalta.

        Returns:
            bool, str: False, jos ei voittoa. Voittajan merkki, jos on voitto
        """
        x, y = self.pelilauta.viimeisin_siirto
        lauta = self.pelilauta.lauta
        # vaaka
        for i in range(1, 6):
            if y - 5 + i >= 0 and y + i <= 20:
                jono = lauta[x][y - 5 + i: y + i]
                if len(set(jono)) == 1:
                    return lauta[x][y]

        # pysty
        for i in range(1, 6):
            jono = []
            if x - 5 + i >= 0:
                for j in range(5):
                    if x + i <= 20:
                        jono.append(lauta[x - 5 + i + j][y])
                    else:
                        break

            if len(set(jono)) == 1 and "_" not in jono and len(jono) == 5:
                return lauta[x][y]

        # diagonaali vasemmalta alaspäin
        for i in range(1, 6):
            jono = []
            if x - 5 + i >= 0:
                for j in range(5):
                    if x + i <= 20 and y + j <= 19:
                        jono.append(lauta[x - 5 + i + j][y - 5 + i + j])
                    else:
                        break

            if len(set(jono)) == 1 and "_" not in jono and len(jono) == 5:
                return lauta[x][y]

        # diagonaali vasemmalta ylös
        for i in range(1, 6):
            jono = []
            if x - i >= -1 and y + i <= 20:
                for j in range(5):
                    if x + 5 - i <= 19 and y - 5 + i >= 0:
                        jono.append(lauta[x + 5 - i - j][y - 5 + i + j])
                    else:
                        break

                if len(set(jono)) == 1 and "_" not in jono and len(jono) == 5:
                    return lauta[x][y]

        return False
