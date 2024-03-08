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
                print("Voitto", voitto)
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

        #
        # KAIKKI KOORDINAATIT SYÖTETÄÄN TEKOÄLYLLE NOLLASTA INDEKSOITUINA!!!
        # KAIKKI KOORDINAATIT TULEE TEKOÄLYLTÄ NOLLASTA INDEKSOITUINA!!!
        # PELILAUTA TEKEE KAIKKI MUUNNOKSET INDEKSOINNIN MUUTOKSISTA!!!
        #
        onnistunut = True
        while True:
            syote = self.kayttoliittyma.pelaajan_siirto_syote(onnistunut)

            hyvaksytty, x, y = self.pelilauta.siirto(syote, self.pelaaja)

            if hyvaksytty:
                self.tekoaly.lisaa_varattu_paikka(x, y)
                self.tekoaly.kasvata_siirtojen_maaraa()
                break

            onnistunut = False

    def tekoalyn_vuoro(self):
        alku = time()
        tekoalyn_siirto, loytynyt, voitto_siirto, voitto_nappi = self.tekoaly.valitse_paras_siirto()
        print(tekoalyn_siirto[0], tekoalyn_siirto[1])

        self.tekoaly.lisaa_varattu_paikka(
            tekoalyn_siirto[0], tekoalyn_siirto[1])
        self.tekoaly.kasvata_siirtojen_maaraa()

        print("aika", time() - alku)

        self.pelilauta.tekoalyn_siirto(tekoalyn_siirto[0], tekoalyn_siirto[1], self.pelilauta.vihu)

    def voiton_tarkistin(self):
        """Tarkastaa onko pelilaudalle tullut voittoa. Viimeisimmäksi pelatun nappulan kohdalta.

        Returns:
            bool, str: False, jos ei voittoa. Voittajan merkki, jos on voitto
        """
        x, y = self.pelilauta.viimeisin_siirto
        voitto = self.tekoaly.voiton_tarkistin(x, y)
        return voitto
