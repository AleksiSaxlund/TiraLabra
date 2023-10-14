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
        self.tutkittavat_paikat = deque([])

        self.minivoitava = pelaaja
        if self.minivoitava == "X":
            self.maksivoitava = "O"
            self.vuoro = -1
        else:
            self.maksivoitava = "X"
            self.vuoro = 1

    def lisaa_varattu_paikka(self, x, y):
        self.varatut_paikat.append((x, y))
        self.tutkittavat_paikat = self.lisaa_tutkittavat_paikat(self.tutkittavat_paikat, self.varatut_paikat, True)
        print("self.lisaa_varattu")
        print(self.tutkittavat_paikat)
        self.siirtojen_maara += 1
    
    def lisaa_tutkittavat_paikat(self, tutkittavat_paikat, varatut_paikat, ensimmainen):
        paikka = varatut_paikat[-1]
        a = False
        if paikka == (-1,-1):
            a = True
        if ensimmainen:
            for i in range(-2, 3, 2):
                for j in range(-2, 3, 2):

                    if paikka[0] + i >= 0 and paikka[1] + j >= 0 and paikka[0] + i < self.n - 1 and paikka[1] + j < self.n - 1:
                        if (paikka[0] + i, paikka[1] + j) in tutkittavat_paikat:
                            tutkittavat_paikat.remove((paikka[0] + i, paikka[1] + j))
                        if self.lauta[paikka[0] + i][paikka[1] + j] == "_" and (paikka[0] + i, paikka[1] + j) not in varatut_paikat:
                            tutkittavat_paikat.appendleft((paikka[0] + i, paikka[1] + j))
                            if a:
                                lauta[paikka[0]+i][paikka[1] + j] = "C"
            
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if paikka[0] + i >= 0 and paikka[1] + j >= 0 and paikka[0] + i < self.n - 1 and paikka[1] + j < self.n - 1:
                        if (paikka[0] + i, paikka[1] + j) in tutkittavat_paikat:
                            tutkittavat_paikat.remove((paikka[0] + i, paikka[1] + j))
                        if self.lauta[paikka[0] + i][paikka[1] + j] == "_" and (paikka[0] + i, paikka[1] + j) not in varatut_paikat:
                            tutkittavat_paikat.appendleft((paikka[0] + i, paikka[1] + j))
                            if a:
                                lauta[paikka[0]+i][paikka[1] + j] = "C"

        else:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if paikka[0] + i >= 0 and paikka[1] + j >= 0 and paikka[0] + i < self.n - 1 and paikka[1] + j < self.n - 1:
                        if (paikka[0] + i, paikka[1] + j) in tutkittavat_paikat:
                            tutkittavat_paikat.remove((paikka[0] + i, paikka[1] + j))
                        if self.lauta[paikka[0] + i][paikka[1] + j] == "_" and (paikka[0] + i, paikka[1] + j) not in varatut_paikat:
                            tutkittavat_paikat.appendleft((paikka[0] + i, paikka[1] + j))
                            if a:
                                lauta[paikka[0]+i][paikka[1] + j] = "C"

        #for asd in tutkittavat_paikat:
         #   for a in varatut_paikat:
          #      if asd == a:
           #         print(asd)
            #        print(tutkittavat_paikat)
             #       l = input("assda")
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

        print(self.tutkittavat_paikat)

        for paikka in self.tutkittavat_paikat:
            if self.lauta[paikka[0]][paikka[1]] == "_":
                self.voitto_loytynyt = False
                print(paikka, paikka in self.tutkittavat_paikat)
                #print(tutkittavat_paikat)

                self.lauta[paikka[0]][paikka[1]] = self.maksivoitava

                varatut_paikat_kopio = self.varatut_paikat[:]
                varatut_paikat_kopio.append((paikka))
                tutkittavat_paikat_kopio = self.lisaa_tutkittavat_paikat(self.tutkittavat_paikat.copy(),
                                                                         varatut_paikat_kopio, False)

                siirron_arvo = self.minimax(self.lauta, syvyys, -inf, inf, self.vuoro, paikka,
                                            tutkittavat_paikat_kopio, varatut_paikat_kopio)

                self.lauta[paikka[0]][paikka[1]] = "_"
                #if self.loydetty < syvyys:
                    #syvyys = self.loydetty + 1

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
                    #print("vaaka", x, y, self.lauta[x][y])
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
                    #print("pysty", self.lauta[x][y], x, y)
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
                    #print("diagonaali vasemmalta alaspäin", self.lauta[x][y], x, y)
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
                        #print("diagonaali vasemmalta ylös", self.lauta[x][y], x, y)
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
                    print(paikka)
                    print(lauta[paikka[0]][paikka[1]])
                    print(tutkittavat_paikat)
                    raise ValueError("Varattu ruutu")
                else:
                    lauta[paikka[0]][paikka[1]] = self.maksivoitava

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
                    print(paikka)
                    print(lauta[paikka[0]][paikka[1]])
                    print(tutkittavat_paikat)
                    raise ValueError("Varattu ruutu")
                else:
                    lauta[paikka[0]][paikka[1]] = self.minivoitava

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

if False:

    # Laudan kokoa voi vaihdella kunhan se on vähintään 5x5 kokoinen.

    lauta = [["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#6
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#7
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#8
             ["_", "_", "_", "O", "O", "O", "_", "_", "_", "_"],#3
             ["_", "X", "X", "_", "X", "X", "O", "_", "_", "_"],#4
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#5
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#6
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#7
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],#8
             ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]]#9
            #  0    1    2    3    4    5    6    7    8    9
    alku = time()
    asd = MiniMax(lauta, "X")
        # MiniMax(lauta, "pelaajan nappula. X tai O")
    # asd.lisaa_varattu_paikka()
    asd.lisaa_varattu_paikka(4,4)
    asd.lisaa_varattu_paikka(3,5)
    asd.lisaa_varattu_paikka(4,5)
    asd.lisaa_varattu_paikka(4,6)
    asd.lisaa_varattu_paikka(4,2)
    asd.lisaa_varattu_paikka(3,3)
    asd.lisaa_varattu_paikka(3,4)
    asd.lisaa_varattu_paikka(4,1)
    

    print(asd.tutkittavat_paikat)
    siirto = asd.valitse_paras_siirto()
    loppu = time()

    print("Aikaa meni:", loppu - alku)
    print(f"asd.lisaa_varattu_paikka{siirto}")