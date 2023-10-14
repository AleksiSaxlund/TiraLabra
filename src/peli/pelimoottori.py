from random import randint
from time import time
from peli.kayttoliittyma import Kayttoliittyma
from peli.pelilauta import Pelilauta
from tekoaly.minimax import MiniMax


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
        vuoro = 1

        while True:
            print(vuoro)
            voitto = self.voiton_tarkistin()
            if voitto in ("X", "O"):
                print("voitto", voitto)
                break

            self.kayttoliittyma.tulosta_pelilauta(self.pelilauta.lauta)

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

            if " " in syote:
                siirto = syote.split(" ")
                if len(list(siirto)) == 2:
                    if siirto[0].isnumeric() and siirto[1].isnumeric():
                        x, y = int(siirto[0]) - 1, int(siirto[1]) - 1

                        if self.pelilauta.siirto(x, y, self.pelaaja):
                            self.tekoaly.lisaa_varattu_paikka(x, y)
                            break
            onnistunut = False

    def tekoalyn_vuoro(self):
        """Väliaikainen "tekoälyn" vuoro.
        """
        alku = time()
        tekoalyn_siirto = self.tekoaly.valitse_paras_siirto()
        print(tekoalyn_siirto)

        self.tekoaly.lisaa_varattu_paikka(tekoalyn_siirto[0], tekoalyn_siirto[1])

        self.pelilauta.siirto(tekoalyn_siirto[0], tekoalyn_siirto[1], self.pelilauta.vihu)
        loppu = time()
        print("Aikaa meni:", loppu - alku)

    def voiton_tarkistin(self):
        """Tarkastaa onko pelilaudalle tullut voittoa.

        Returns:
            bool, str: False, jos ei voittoa. Voittajan merkki, jos on voitto
        """
        x, y = self.pelilauta.viimeisin_siirto
        print(self.pelilauta.viimeisin_siirto)
        lauta = self.pelilauta.lauta
        # vaaka
        for i in range(1, 6):
            if y - 5 + i >= 0 and y + i <= 25:
                jono = lauta[x][y - 5 + i: y + i]
                if len(set(jono)) == 1:
                    return lauta[x][y]

        # pysty
        for i in range(1, 6):
            jono = []
            if x - 5 + i >= 0:
                for j in range(5):
                    if x + i <= 25:
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
                    if x + i <= 25 and y + j <= 24:
                        jono.append(lauta[x - 5 + i + j][y - 5 + i + j])
                    else:
                        break

            if len(set(jono)) == 1 and "_" not in jono and len(jono) == 5:
                return lauta[x][y]

        # diagonaali vasemmalta ylös
        for i in range(1, 6):
            jono = []
            if x - i >= -1 and y + i <= 25:
                for j in range(5):
                    if x + 5 - i <= 24 and y - 5 + i >= 0:
                        jono.append(lauta[x + 5 - i - j][y - 5 + i + j])
                    else:
                        break

                if len(set(jono)) == 1 and "_" not in jono and len(jono) == 5:
                    return lauta[x][y]

        return False


if False:
    asd = PeliMoottori()
