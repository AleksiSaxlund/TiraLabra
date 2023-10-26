from math import inf
from collections import deque
from tekoaly.heurestiikka import arvioi


class MiniMax():
    """Tekoälystä vastaava luokka.
    """

    def __init__(self, lauta: list, pelaaja: str):
        self.n = len(lauta[0])
        self.siirtojen_maara = self.n * self.n
        self.pelatut_siirrot = 0
        self.lauta = lauta
        self.varatut_paikat = []
        self.tutkittavat_paikat = deque([])

        self.minivoitava = pelaaja
        if self.minivoitava == "X":
            self.maksivoitava = "O"
            self.vuoro = -1
        else:
            self.maksivoitava = "X"
            self.vuoro = 1

    def lisaa_varattu_paikka(self, x: int, y: int):
        """Lisää paikan varattujen paikojen listaan.

        Args:
            x (int): X-koordinaatti
            y (int): Y-koordinaatti
        """
        self.varatut_paikat.append((x, y))
        self.tutkittavat_paikat = self.lisaa_tutkittavat_paikat(
            self.tutkittavat_paikat, self.varatut_paikat, True)
        self.siirtojen_maara += 1

    def lisaa_tutkittavat_paikat(self, tutkittavat_paikat: list, varatut_paikat: list, ensimmainen: bool):
        """Lisää tutkittavat paikat annetusta tutkittavat paikat listasta.

        Args:
            tutkittavat_paikat (list): Kopio tutkittavat paikat listasta
            varatut_paikat (list): Lista, jossa on kaikki varatut paikat
            ensimmainen (bool): Onko ensimmäinen iteraatio, vai jokin syvempi kerros.

        Returns:
            list: Lista, johon on lisätty kaikki uudet tutkittavat paikat
        """
        paikka = varatut_paikat[-1]

        if ensimmainen:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if paikka[0] + i >= 0 and paikka[1] + j >= 0 and paikka[0] + i < self.n - 1 and paikka[1] + j < self.n - 1:
                        if (paikka[0] + i, paikka[1] + j) in tutkittavat_paikat:
                            tutkittavat_paikat.remove(
                                (paikka[0] + i, paikka[1] + j))
                        if self.lauta[paikka[0] + i][paikka[1] + j] == "_" and (paikka[0] + i, paikka[1] + j) not in varatut_paikat:
                            tutkittavat_paikat.appendleft(
                                (paikka[0] + i, paikka[1] + j))

            for i in range(-2, 3, 2):
                for j in range(-2, 3, 2):

                    if paikka[0] + i >= 0 and paikka[1] + j >= 0 and paikka[0] + i < self.n - 1 and paikka[1] + j < self.n - 1:
                        if (paikka[0] + i, paikka[1] + j) in tutkittavat_paikat:
                            tutkittavat_paikat.remove(
                                (paikka[0] + i, paikka[1] + j))
                        if self.lauta[paikka[0] + i][paikka[1] + j] == "_" and (paikka[0] + i, paikka[1] + j) not in varatut_paikat:
                            tutkittavat_paikat.appendleft(
                                (paikka[0] + i, paikka[1] + j))

        else:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if paikka[0] + i >= 0 and paikka[1] + j >= 0 and paikka[0] + i < self.n - 1 and paikka[1] + j < self.n - 1:
                        if (paikka[0] + i, paikka[1] + j) in tutkittavat_paikat:
                            tutkittavat_paikat.remove(
                                (paikka[0] + i, paikka[1] + j))
                        if self.lauta[paikka[0] + i][paikka[1] + j] == "_" and (paikka[0] + i, paikka[1] + j) not in varatut_paikat:
                            tutkittavat_paikat.appendleft(
                                (paikka[0] + i, paikka[1] + j))

        return tutkittavat_paikat

    def valitse_paras_siirto(self):
        """Funktio, joka kutsuu minimaxia ensimmäistä kertaa.

        Returns:
            tuple: Palauttaa parhaan siirron koordinaatit.
        """
        paras_arvo = -inf
        paras_siirto = (-1, -1)
        syvyys = 3
        self.loydetty = inf
        self.asd = 0

        for paikka in self.tutkittavat_paikat:
            if self.lauta[paikka[0]][paikka[1]] == "_":
                self.voitto_loytynyt = False
                print("Ladataan...")
                self.lauta[paikka[0]][paikka[1]] = self.maksivoitava

                varatut_paikat_kopio = self.varatut_paikat[:]
                varatut_paikat_kopio.append((paikka))
                tutkittavat_paikat_kopio = self.lisaa_tutkittavat_paikat(self.tutkittavat_paikat.copy(),
                                                                         varatut_paikat_kopio, False)

                siirron_arvo = self.minimax(self.lauta, syvyys, -inf, inf, self.vuoro, paikka,
                                            tutkittavat_paikat_kopio, varatut_paikat_kopio)

                self.lauta[paikka[0]][paikka[1]] = "_"

                if siirron_arvo > paras_arvo:
                    paras_arvo = siirron_arvo
                    paras_siirto = paikka

        return paras_siirto

    def siirtoja_jaljella(self, syvyys: int):
        """Tarkistaa, että onko enää mahdollista tehdä siirtoja.

        Args:
            syvyys (int): Minimaxin syvyys.

        Returns:
            bool: True, jos on siirtoja, False jos ei.
        """
        if self.pelatut_siirrot + (3 + syvyys) >= self.siirtojen_maara:
            return False
        return True

    def voiton_tarkistin(self, x, y):
        """Tarkastaa onko pelilaudalle tullut voittoa viimeisimpänä tehdystä siirrosta.

        Returns:
            bool, str: False, jos ei voittoa. Voittajan nappula, jos voitto
        """

        # vaaka
        for i in range(1, 6):
            if y - 5 + i >= 0 and y + i <= self.n:
                jono = self.lauta[x][y - 5 + i: y + i]
                if len(set(jono)) == 1 and len(jono) == 5 and "_" not in jono:
                    return self.lauta[x][y]

        # pysty
        if True:
            for i in range(1, 6):
                jono = []
                if x - 5 + i >= 0:
                    for j in range(5):
                        if x + i <= self.n:
                            jono.append(self.lauta[x - 5 + i + j][y])
                        else:
                            break

                if len(set(jono)) == 1 and len(jono) == 5 and "_" not in jono:
                    return self.lauta[x][y]

            # diagonaali vasemmalta alaspäin
            for i in range(1, 6):
                jono = []
                if x - 5 + i >= 0:
                    for j in range(5):
                        if x - 5 + i + j <= self.n and x - 5 + i + j < self.n and y - 5 + i + j >= 0 and y - 5 + i + j < self.n:
                            jono.append(
                                self.lauta[x - 5 + i + j][y - 5 + i + j])
                        else:
                            break

                if len(set(jono)) == 1 and len(jono) == 5 and "_" not in jono:
                    return self.lauta[x][y]

            # diagonaali vasemmalta ylös
            for i in range(1, 6):
                jono = []
                if x - i >= -1 and y + i <= self.n:
                    for j in range(5):
                        if x + 5 - i < self.n and y - 5 + i >= 0:
                            jono.append(
                                self.lauta[x + 5 - i - j][y - 5 + i + j])
                        else:
                            break

                    if len(set(jono)) == 1 and len(jono) == 5 and "_" not in jono:
                        return self.lauta[x][y]

        return False

    def minimax(self, lauta: list, syvyys: int, alpha: int, beta: int, vuoro: int, paikka: tuple,
                tutkittavat_paikat: list, varatut_paikat: list):
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
            if voitto == self.maksivoitava:
                return 10**5
            return -10**5

        if syvyys == 0:
            if vuoro == 1:
                return arvioi(self.lauta, self.maksivoitava)
            else:
                return - arvioi(self.lauta, self.minivoitava)

        if not self.siirtoja_jaljella(syvyys):
            return 0

        if vuoro == 1:
            paras = -inf

            for paikka in tutkittavat_paikat:

                if lauta[paikka[0]][paikka[1]] != "_":
                    pass
                else:
                    lauta[paikka[0]][paikka[1]] = self.maksivoitava
                    self.asd += 1
                    varatut_paikat_kopio = varatut_paikat[:]
                    varatut_paikat_kopio.append((paikka))
                    tutkittavat_paikat_kopio = self.lisaa_tutkittavat_paikat(tutkittavat_paikat.copy(),
                                                                             varatut_paikat_kopio, False)

                    arvo = self.minimax(lauta, syvyys-1, alpha, beta, vuoro*-1, paikka,
                                        tutkittavat_paikat_kopio, varatut_paikat_kopio)

                    paras = max(arvo, paras)
                    alpha = max(alpha, arvo)

                    lauta[paikka[0]][paikka[1]] = "_"
                    if beta <= alpha or abs(paras) == 10**5:
                        break

            return paras

        else:
            paras = inf

            for paikka in tutkittavat_paikat:

                if lauta[paikka[0]][paikka[1]] != "_":
                    pass
                else:
                    lauta[paikka[0]][paikka[1]] = self.minivoitava
                    self.asd += 1
                    varatut_paikat_kopio = varatut_paikat[:]
                    varatut_paikat_kopio.append((paikka))
                    tutkittavat_paikat_kopio = self.lisaa_tutkittavat_paikat(tutkittavat_paikat.copy(),
                                                                             varatut_paikat_kopio, False)

                    arvo = self.minimax(lauta, syvyys-1, alpha, beta, vuoro*-1, paikka,
                                        tutkittavat_paikat_kopio, varatut_paikat_kopio)

                    paras = min(arvo, paras)
                    beta = min(beta, arvo)

                    lauta[paikka[0]][paikka[1]] = "_"
                    if beta <= alpha or abs(paras) == 10**5:
                        break
            return paras
