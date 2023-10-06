from time import time
from math import inf, dist
from collections import deque
from tekoaly.heurestiikka import arvioi


class MiniMax():
    """Minimax algoritmin luokka
    """

    def __init__(self, lauta, pelaaja):
        self.n = len(lauta[0])
        self.siirtojen_maara = self.n * self.n
        self.pelatut_siirrot = 0
        self.lauta = lauta
        self.varatut_paikat = []

        self.minivoitava = pelaaja
        if self.minivoitava == "X":
            self.maksivoitava = "O"
            self.vuoro = -1
        else:
            self.maksivoitava = "X"
            self.vuoro = 1

    def lisaa_varattu_paikka(self, x, y):
        self.varatut_paikat.append((x, y))
        self.siirtojen_maara += 1
    
    def lisaa_tutkittavat_paikat(self, tutkittavat_paikat, varatut_paikat, ensimmainen):
        if False:
            for i in range(5):
                for j in range(5):
                    #print(varatut_paikat)
                    for paikka in varatut_paikat:
                        if paikka[0] -2 + i >= 0 and paikka[1] - 2 + j >= 0 and paikka[0] -2 + i < self.n - 1 and paikka[1] - 2 + j < self.n - 1:
                            #print(paikka[0] -2 + i, paikka[1] - 2 + j)
                            if self.lauta[paikka[0] -2 + i][paikka[1] - 2 + j] == "_" and (paikka[0] -2 + i, paikka[1] - 2 + j) not in tutkittavat_paikat:
                                tutkittavat_paikat.appendleft((paikka[0] -2 + i, paikka[1] - 2 + j))
        else:
            for i in range(3):
                for j in range(3):
                    #print(varatut_paikat)
                    for paikka in varatut_paikat:
                        if paikka[0] - 1 + i >= 0 and paikka[1] - 1 + j >= 0 and paikka[0] -1 + i < self.n - 1 and paikka[1] - 1 + j < self.n - 1:
                            #print(paikka[0] -2 + i, paikka[1] - 2 + j)
                            if self.lauta[paikka[0] - 1 + i][paikka[1] - 1 + j] == "_" and (paikka[0] -1 + i, paikka[1] - 1 + j) not in tutkittavat_paikat:
                                tutkittavat_paikat.appendleft((paikka[0] - 1 + i, paikka[1] - 1 + j))
        return deque(tutkittavat_paikat)

    def valitse_paras_siirto(self):
        """Funktio, joka kutsuu minimaxia ensimmäistä kertaa.

        Returns:
            tuple: Palauttaa parhaan siirron koordinaatit.
        """
        paras_arvo = -inf
        paras_siirto = (-1, -1)

        tutkittavat_paikat = self.lisaa_tutkittavat_paikat(deque([]), self.varatut_paikat, True)
        print(tutkittavat_paikat)

        for paikka in tutkittavat_paikat:
            if self.lauta[paikka[0]][paikka[1]] == "_":
                self.voitto_loytynyt = False
                print(paikka, paikka in tutkittavat_paikat)
                #print(tutkittavat_paikat)

                self.lauta[paikka[0]][paikka[1]] = self.maksivoitava

                varatut_paikat_kopio = self.varatut_paikat[:]
                varatut_paikat_kopio.append((paikka))
                tutkittavat_paikat_kopio = self.lisaa_tutkittavat_paikat(tutkittavat_paikat.copy(),
                                                                         varatut_paikat_kopio, False)

                siirron_arvo = self.minimax(self.lauta, 1, -inf, inf, self.vuoro, paikka,
                                            tutkittavat_paikat_kopio, varatut_paikat_kopio)

                self.lauta[paikka[0]][paikka[1]] = "_"

                if siirron_arvo > paras_arvo:
                    paras_arvo = siirron_arvo
                    paras_siirto = paikka
                    #if self.voitto_loytynyt:
                        #return self.voitto_siirto

        print(paras_arvo)
        return paras_siirto

    def siirtoja_jaljella(self, syvyys):
        """Tarkistaa, että onko enää mahdollista tehdä siirtoja.

        Args:
            syvyys (int): Minimaxin syvyys.

        Returns:
            bool: True, jos on siirtoja, False jos ei.
        """
        if self.pelatut_siirrot + syvyys >= self.siirtojen_maara:
            return False
        return True
    
    def voiton_tarkistin(self, x, y):
        """Tarkastaa onko pelilaudalle tullut voittoa viimeisimpänä tehdystä siirrosta.

        Returns:
            bool: False, jos ei voittoa. True jos voitto
        """

        # vaaka
        for i in range(1, 6):
            if y - 5 + i >= 0 and y + i <= self.n:
                jono = self.lauta[x][y - 5 + i: y + i]
                if len(set(jono)) == 1 and len(jono) == 5 and "_" not in jono:
                    print("vaaka", x, y, self.lauta[x][y])
                    #[print(i) for i in self.lauta]
                    return self.lauta[x][y]

        # pysty
        if True:
            for i in range(1, 6):
                jono = []
                if x - 5 + i >= 0:
                    for j in range(5):
                        if x + i <= self.n:
                            #print(x - 5 + i + j, y)
                            jono.append(self.lauta[x - 5 + i + j][y])
                        else:
                            break

                if len(set(jono)) == 1 and len(jono) == 5 and "_" not in jono:
                    print("pysty", self.lauta[x][y], x, y)
                    return self.lauta[x][y]

            # diagonaali vasemmalta alaspäin
            for i in range(1, 6):
                jono = []
                if x - 5 + i >= 0:
                    for j in range(5):
                        if x - 5 + i + j <= self.n and x - 5 + i + j < self.n and y - 5 + i + j >= 0 and y - 5 + i + j < self.n:
                            jono.append(self.lauta[x - 5 + i + j][y - 5 + i + j])
                        else:
                            break

                if len(set(jono)) == 1 and len(jono) == 5 and "_" not in jono:
                    print("diagonaali vasemmalta alaspäin", self.lauta[x][y], x, y)
                    return self.lauta[x][y]

            # diagonaali vasemmalta ylös
            for i in range(1, 6):
                jono = []
                if x - i >= -1 and y + i <= self.n:
                    for j in range(5):
                        if x + 5 - i < self.n and y - 5 + i >= 0:
                            jono.append(self.lauta[x + 5 - i - j][y - 5 + i + j])
                        else:
                            break

                    if len(set(jono)) == 1 and len(jono) == 5 and "_" not in jono:
                        print("diagonaali vasemmalta ylös", self.lauta[x][y], x, y)
                        return self.lauta[x][y]

        return False

    def minimax(self, lauta, syvyys, alpha, beta, vuoro, paikka,
                tutkittavat_paikat, varatut_paikat):
        """Minimaxin rekursiivinen funktio itsessään.

        Args:
            lauta (list): Pelilauta
            syvyys (int): Pelipuun tämänhetkinen syvyys.
            vuoro (int): Kumman vuoro. 1 = maksimoitava ja -1 = minivoitava.

        Returns:
            int: Palauttaa siirron arvon.
        """
        voitto = self.voiton_tarkistin(paikka[0], paikka[1])
        if voitto != False:
            self.voitto_loytynyt = True
            self.voitto_siirto = (paikka[0], paikka[1])
            if voitto == self.maksivoitava:
                return syvyys - 10**5
            return 10**5 - syvyys

        if syvyys >= 4:
            if vuoro == 1:
                return arvioi(self.lauta, self.maksivoitava)
            else:
                return - arvioi(self.lauta, self.minivoitava)

        if not self.siirtoja_jaljella(syvyys):
            return 0

        if vuoro == 1:
            paras = -inf

            for paikka in tutkittavat_paikat:

                liian_kaukana = True
                for varattu in self.varatut_paikat:
                    if dist(paikka, varattu) <= 2.9:
                        liian_kaukana = False
                        break
                if liian_kaukana:
                    continue

                if lauta[paikka[0]][paikka[1]] == "_":

                    lauta[paikka[0]][paikka[1]] = self.maksivoitava

                    varatut_paikat_kopio = varatut_paikat[:]
                    varatut_paikat_kopio.append((paikka))
                    tutkittavat_paikat_kopio = self.lisaa_tutkittavat_paikat(tutkittavat_paikat.copy(),
                                                                             varatut_paikat_kopio, False)

                    arvo = self.minimax(lauta, syvyys+1, alpha, beta, vuoro*-1, paikka,
                                        tutkittavat_paikat_kopio, varatut_paikat_kopio)

                    paras = max(arvo, paras)
                    alpha = max(alpha, arvo)

                    lauta[paikka[0]][paikka[1]] = "_"
                    if beta <= alpha:
                        break

            return paras

        else:
            paras = inf

            for paikka in tutkittavat_paikat:

                liian_kaukana = True
                for varattu in self.varatut_paikat:
                    if dist(paikka, varattu) <= 2.9:
                        liian_kaukana = False
                        break
                if liian_kaukana:
                    continue

                if lauta[paikka[0]][paikka[1]] == "_":
                    lauta[paikka[0]][paikka[1]] = self.minivoitava

                    varatut_paikat_kopio = varatut_paikat[:]
                    varatut_paikat_kopio.append((paikka))
                    tutkittavat_paikat_kopio = self.lisaa_tutkittavat_paikat(tutkittavat_paikat.copy(),
                                                                             varatut_paikat_kopio, False)

                    arvo = self.minimax(lauta, syvyys+1, alpha, beta, vuoro*-1, paikka,
                                        tutkittavat_paikat_kopio, varatut_paikat_kopio)

                    paras = min(arvo, paras)
                    beta = min(beta, arvo)

                    lauta[paikka[0]][paikka[1]] = "_"
                    if beta <= alpha:
                        break
            return paras

if False:

    # Laudan kokoa voi vaihdella kunhan se on vähintään 5x5 kokoinen.

    lauta = [["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#0
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#1
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#2
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#3
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#4
             ["X", "X", "X", "X", "_", "_", "_", "_", "_", "_"],#5
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#6
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#7
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#8
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]]#9
            #  0    1    2    3    4    5    6    7    8    9
    alku = time()
    asd = MiniMax(lauta, "X")
        # MiniMax(lauta, "pelaajan nappula. X tai O")
    asd.lisaa_varattu_paikka(5, 0)
    asd.lisaa_varattu_paikka(5, 1)
    asd.lisaa_varattu_paikka(5, 2)
    asd.lisaa_varattu_paikka(5, 3)
    siirto = asd.valitse_paras_siirto()
    loppu = time()

    print("Aikaa meni:", loppu - alku)
    print(f"asd.lisaa_varattu_paikka{siirto}")