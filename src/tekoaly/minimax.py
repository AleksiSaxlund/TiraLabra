from math import inf
from collections import deque
from random import choice
from tekoaly.heurestiikka import arvioi


class MiniMax():
    """Tekoälystä vastaava luokka.
    """

    def __init__(self, lauta: list, pelaaja: str):
        self.n = len(lauta[0])
        self.tilaa_laudalla = self.n * self.n
        self.pelatut_siirrot = 0
        self.lauta = lauta
        self.tutkittavat_paikat = deque()

        self.ensimmainen_siirto = True

        self.minivoitava = pelaaja
        if self.minivoitava == "X":
            self.maksivoitava = "O"
            self.vuoro = -1
        else:
            self.maksivoitava = "X"
            self.vuoro = -1
    
    def kasvata_siirtojen_maaraa(self):
        """Kasvattaa siirtojen määrää yhdellä.
        """
        self.pelatut_siirrot += 1
    
    def __poista_tutkittavista_paikoista(self, paikka: tuple):
        """Poistaa paikan tutkittavista paikoista.

        Args:
            paikka (tuple): Poistettava paikka
        """
        if paikka in self.tutkittavat_paikat:
            self.tutkittavat_paikat.remove(paikka)

    def lisaa_varattu_paikka(self, x: int, y: int):
        """Lisää paikan varattujen paikojen listaan.

        Args:
            x (int): X-koordinaatti
            y (int): Y-koordinaatti
        """
        viimeksi_pelattu = (x, y)
        self.__poista_tutkittavista_paikoista(viimeksi_pelattu)

        self.tutkittavat_paikat = self.lisaa_tutkittavat_paikat(
            self.tutkittavat_paikat, viimeksi_pelattu, True)


    def lisaa_tutkittavat_paikat(self, tutkittavat_paikat: list, viimeksi_pelattu: tuple, ensimmainen: bool):
        """Lisää tutkittavat paikat annetusta tutkittavat paikat listasta.

        Args:
            tutkittavat_paikat (list): Kopio tutkittavat paikat listasta
            varatut_paikat (list): Lista, jossa on kaikki varatut paikat
            ensimmainen (bool): Onko ensimmäinen iteraatio, vai jokin syvempi kerros.

        Returns:
            list: Lista, johon on lisätty kaikki uudet tutkittavat paikat
        """
        paikka = viimeksi_pelattu

        if ensimmainen:
            for i in range(-2, 3, 2):
                for j in range(-2, 3, 2):
                    if paikka[0] + i >= 0 and paikka[1] + j >= 0 and paikka[0] + i < self.n - 1 and paikka[1] + j < self.n - 1:
                        if (paikka[0] + i, paikka[1] + j) in tutkittavat_paikat:
                            tutkittavat_paikat.remove(
                                (paikka[0] + i, paikka[1] + j))
                        if self.lauta[paikka[0] + i][paikka[1] + j] == "_":
                            tutkittavat_paikat.appendleft(
                                (paikka[0] + i, paikka[1] + j))

        for i in range(-1, 2):
            for j in range(-1, 2):
                if paikka[0] + i >= 0 and paikka[1] + j >= 0 and paikka[0] + i < self.n - 1 and paikka[1] + j < self.n - 1:
                    if (paikka[0] + i, paikka[1] + j) in tutkittavat_paikat:
                        tutkittavat_paikat.remove(
                            (paikka[0] + i, paikka[1] + j))
                    if self.lauta[paikka[0] + i][paikka[1] + j] == "_":
                        tutkittavat_paikat.appendleft(
                            (paikka[0] + i, paikka[1] + j))

        return tutkittavat_paikat

    def valitse_paras_siirto(self):
        self.voitto_loytynyt = False
        self.voitto_siirto = (-1, -1)
        self.voitto_nappi = "_"

        paras_arvo = -inf
        paras_siirto = (-1, -1)
        syvyys = 3

        alpha = -inf
        beta = inf

        self.alkuperainen_syvyys = syvyys
        self.loydetty = inf

        # Tekoälyn ensimmäinen siirto kovakoodattu tulemaan aina keskelle tai pelaajan lähelle.
        if self.ensimmainen_siirto:
            self.ensimmainen_siirto = False

            if len(self.tutkittavat_paikat) > 0:
                paikka = choice(self.tutkittavat_paikat)
                return paikka, self.voitto_loytynyt, self.voitto_siirto, self.voitto_nappi
            else:
                return ((self.n // 2, self.n // 2), self.voitto_loytynyt, self.voitto_siirto, self.voitto_nappi)

        # Tarkistaa onko voittoa yhden siirron päässä.
        for paikka in self.tutkittavat_paikat:
            if self.lauta[paikka[0]][paikka[1]] == "_":
                self.lauta[paikka[0]][paikka[1]] = self.maksivoitava
                voitto = self.voiton_tarkistin(paikka[0], paikka[1])
                self.lauta[paikka[0]][paikka[1]] = "_"

            if voitto == self.maksivoitava:
                return paikka, True, paikka, self.maksivoitava

        # Siirron valitsija itsessään. Käy läpi kaikki tutkittavat paikat ja valitsee niistä parhaan.
        for paikka in self.tutkittavat_paikat:
            if self.lauta[paikka[0]][paikka[1]] == "_":
                print(f"Ladataan... {round((self.tutkittavat_paikat.index(paikka) / len(self.tutkittavat_paikat)) * 100)}%")

                self.lauta[paikka[0]][paikka[1]] = self.maksivoitava

                viimeksi_pelattu = paikka
                tutkittavat_paikat_kopio = self.lisaa_tutkittavat_paikat(self.tutkittavat_paikat.copy(),
                                                                         viimeksi_pelattu, False)

                siirron_arvo = self.minimax(self.lauta, syvyys, alpha, beta, self.vuoro, paikka,
                                            tutkittavat_paikat_kopio)

                self.lauta[paikka[0]][paikka[1]] = "_"
                if siirron_arvo > paras_arvo:
                    alpha = siirron_arvo
                    paras_arvo = siirron_arvo
                    paras_siirto = paikka

        return paras_siirto, self.voitto_loytynyt, self.voitto_siirto, self.voitto_nappi

    def siirtoja_jaljella(self, syvyys: int):
        """Tarkistaa onko pelilaudalla siirtoja jäljellä.

        Args:
            syvyys (int): Syvyys, johon asti minimax on tarkastellut siirtoja.

        Returns:
            Bool: Onko laudalla tilaa.
        """
        if self.pelatut_siirrot + syvyys < self.tilaa_laudalla - 1:
            return True
        return False

    def voiton_tarkistin(self, x, y):
        """Tarkastaa onko pelilaudalle tullut voittoa viimeisimpänä tehdystä siirrosta.

        Returns:
            bool, str: False, jos ei voittoa. Voittajan nappula, jos voitto
        """

        tarkistettava = self.lauta[x][y]

        if tarkistettava == "_":
            return False

        # vaaka
        loydot = 0
        for i in range(-4, 5):
            
            if y + i >= 0 and y + i < self.n:
                if self.lauta[x][y + i] == tarkistettava:
                    loydot += 1

                    if loydot == 5:
                        return tarkistettava
                else:
                    loydot = 0

        # pysty
        loydot = 0
        for i in range(-4, 5):
            
            if x + i >= 0 and x + i < self.n:
                if self.lauta[x + i][y] == tarkistettava:
                    loydot += 1

                    if loydot == 5:
                        return tarkistettava
                else:
                    loydot = 0

        # diagonaali vasemmalta alaspäin
        loydot = 0
        for i in range(-4, 5):

            if x + i >= 0 and y + i >= 0 and x + i < self.n and y + i < self.n:
                if self.lauta[x + i][y + i] == tarkistettava:
                    loydot += 1

                    if loydot == 5:
                        return tarkistettava
                else:
                    loydot = 0

        # diagonaali vasemmalta ylös
        loydot = 0
        for i in range(-4, 5):

            if x - i >= 0 and y + i >= 0 and x - i < self.n and y + i < self.n:
                if self.lauta[x - i][y + i] == tarkistettava:
                    loydot += 1

                    if loydot == 5:
                        return tarkistettava
                else:
                    loydot = 0

        return False

    def minimax(self, lauta: list, syvyys: int, alpha: int, beta: int, vuoro: int, paikka: tuple,
                tutkittavat_paikat: list):
        """Minimaxin rekursiivinen funktio itsessään.

        Args:
            lauta (list): Pelilauta
            syvyys (int): Pelipuun tämänhetkinen syvyys.
            alpha (int): alfa arvo
            beta (int): beetta arvo
            vuoro (int): Kumman vuoro. 1 = maksimoitava ja -1 = minivoitava.
            paikka (tuple): tutkittava paikka
            tutkittavat_paikat (list): kaikki tutkittavat paikat
            varatut_paikat (list): kaikki paikat, joissa on jo nappula

        Returns:
            int: Palauttaa siirron arvon.
        """
        voitto = self.voiton_tarkistin(paikka[0], paikka[1])
        if voitto != False:
            self.loydetty = min(self.loydetty, syvyys)
            self.voitto_siirto = (paikka[0], paikka[1])
            self.voitto_nappi = voitto
            self.voitto_loytynyt = True

            if voitto == self.maksivoitava:
                return 10**5 - (self.alkuperainen_syvyys - syvyys)
            return -10**5 + (self.alkuperainen_syvyys - syvyys)

        if syvyys == 0:
            if vuoro == 1:
                return arvioi(lauta, self.maksivoitava)
            return - arvioi(lauta, self.minivoitava)

        if not self.siirtoja_jaljella(syvyys):
            return 0

        if vuoro == 1:
            paras = -inf

            for paikka in tutkittavat_paikat:

                if lauta[paikka[0]][paikka[1]] != "_":
                    continue
                else:
                    lauta[paikka[0]][paikka[1]] = self.maksivoitava

                    tutkittavat_paikat_kopio = self.lisaa_tutkittavat_paikat(tutkittavat_paikat.copy(),
                                                                             paikka, False)

                    arvo = self.minimax(lauta, syvyys-1, alpha, beta, vuoro*-1, paikka,
                                        tutkittavat_paikat_kopio)

                    paras = max(arvo, paras)
                    alpha = max(alpha, arvo)

                    lauta[paikka[0]][paikka[1]] = "_"
                    if beta <= alpha:
                        break

            return paras

        else:
            paras = inf

            for paikka in tutkittavat_paikat:

                if lauta[paikka[0]][paikka[1]] != "_":
                    continue
                else:
                    lauta[paikka[0]][paikka[1]] = self.minivoitava

                    tutkittavat_paikat_kopio = self.lisaa_tutkittavat_paikat(tutkittavat_paikat.copy(),
                                                                             paikka, False)

                    arvo = self.minimax(lauta, syvyys-1, alpha, beta, vuoro*-1, paikka,
                                        tutkittavat_paikat_kopio)

                    paras = min(arvo, paras)
                    beta = min(beta, arvo)

                    lauta[paikka[0]][paikka[1]] = "_"
                    if beta <= alpha:
                        break
            return paras

