from time import time
from math import inf
from heurestiikka import arvioi


class MiniMax():
    """Minimax algoritmin luokka
    """

    def __init__(self, lauta, pelaaja, siirrot):
        self.n = len(lauta)
        self.siirtojen_maara = self.n * self.n
        self.pelatut_siirrot = siirrot
        self.lauta = lauta

        self.minivoitava = pelaaja
        if self.minivoitava == "X":
            self.maksivoitava = "O"
            self.vuoro = 1
        else:
            self.maksivoitava = "X"
            self.vuoro = -1

    def valitse_paras_siirto(self):
        """Funktio, joka kutsuu minimaxia ensimmäistä kertaa.

        Returns:
            tuple: Palauttaa parhaan siirron koordinaatit.
        """
        paras_arvo = -inf
        paras_siirto = (-1, -1)

        for i in range(self.n):
            for j in range(self.n):

                if self.lauta[i][j] == "_":
                    print(i, j)

                    self.lauta[i][j] = self.maksivoitava

                    voitto = self.voiton_tarkistin(i, j)
                    if voitto == self.maksivoitava:
                        paras_arvo = 10**5
                        paras_siirto = (i, j)

                    siirron_arvo = self.minimax(self.lauta, 1, -10**5, 10**5, self.vuoro, i, j)

                    self.lauta[i][j] = "_"

                    if siirron_arvo > paras_arvo:
                        paras_arvo = siirron_arvo
                        paras_siirto = (i, j)
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
                jono = lauta[x][y - 5 + i: y + i]
                if len(set(jono)) == 1 and len(jono) == 5:
                    print("vaaka", jono, lauta[x][y])
                    #[print(i) for i in self.lauta]
                    return lauta[x][y]

        # pysty
        for i in range(1, 6):
            jono = []
            if x - 5 + i >= 0:
                for j in range(5):
                    if x + i <= self.n:
                        #print(x - 5 + i + j, y)
                        jono.append(lauta[x - 5 + i + j][y])
                    else:
                        break

            if len(set(jono)) == 1 and "_" not in jono and len(jono) == 5:
                #print("pysty")
                #[print(i) for i in self.lauta]
                #a = input()
                return lauta[x][y]

        # diagonaali vasemmalta alaspäin
        for i in range(1, 6):
            jono = []
            if x - 5 + i >= 0:
                for j in range(5):
                    if x + i <= self.n and y + j < self.n:
                        try:
                            jono.append(lauta[x - 5 + i + j][y - 5 + i + j])
                        except:
                            print(x - 5 + i + j, y - 5 + i + j)
                            a = input("asd")
                    else:
                        break

            if len(set(jono)) == 1 and "_" not in jono and len(jono) == 5:
                print("diagonaali vasemmalta alaspäin")
                return lauta[x][y]

        # diagonaali vasemmalta ylös
        for i in range(1, 6):
            jono = []
            if x - i >= -1 and y + i <= self.n:
                for j in range(5):
                    if x + 5 - i < self.n and y - 5 + i >= 0:
                        jono.append(lauta[x + 5 - i - j][y - 5 + i + j])
                    else:
                        break

                if len(set(jono)) == 1 and "_" not in jono and len(jono) == 5:
                    print("diagonaali vasemmalta ylös")
                    return lauta[x][y]

        return False

    def minimax(self, lauta, syvyys, alpha, beta, vuoro, x, y):
        """Minimaxin rekursiivinen funktio itsessään.

        Args:
            lauta (list): Pelilauta
            syvyys (int): Pelipuun tämänhetkinen syvyys.
            vuoro (int): Kumman vuoro. 1 = maksimoitava ja -1 = minivoitava.

        Returns:
            int: Palauttaa siirron arvon.
        """
        voitto = self.voiton_tarkistin(x, y)
        if voitto != False:
            if voitto == self.maksivoitava:
                return syvyys - 10**5
            return 10**5 - syvyys

        if syvyys >= 5:
            return arvioi(self.lauta, self.maksivoitava)

        if not self.siirtoja_jaljella(syvyys):
            return 0

        if vuoro == 1:
            paras = -10**5

            for i in range(self.n):
                for j in range(self.n):

                    if lauta[i][j] == "_":
                        lauta[i][j] = self.maksivoitava

                        arvo = self.minimax(lauta, syvyys+1, alpha, beta, vuoro*-1, x, y)

                        paras = max(arvo, paras)
                        alpha = max(alpha, arvo)

                        lauta[i][j] = "_"
                        if beta <= alpha:
                            break

            return paras

        else:
            paras = 10**5

            for i in range(self.n):
                for j in range(self.n):

                    if lauta[i][j] == "_":
                        lauta[i][j] = self.minivoitava

                        arvo = self.minimax(lauta, syvyys+1, alpha, beta, vuoro*-1, x, y)

                        paras = min(arvo, paras)
                        beta = min(beta, arvo)

                        lauta[i][j] = "_"
                        if beta <= alpha:
                            break
            return paras

alku = time()
if False:
    lauta = [["_", "_", "_"],
            ["_", "X", "_"],
            ["_", "_", "_"]]
else:
    # Laudan kokoa voi vaihdella kunhan se on vähintään 5x5 kokoinen.
    lauta = [["_", "_", "_", "_", "_", "_"],
             ["_", "_", "_", "_", "O", "_"],
             ["_", "X", "X", "X", "X", "O"],
             ["_", "X", "O", "O", "_", "_"],
             ["_", "_", "_", "_", "_", "_"],
             ["_", "_", "_", "_", "_", "_"]]
             #["_", "_", "_", "_", "_", "_", "_"],
             #["_", "_", "_", "_", "_", "_", "_"]]
             #["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
             #["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
             #["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]]

asd = MiniMax(lauta, "O", 0)
    # MiniMax(lauta, "JOS PELAAJA ON X SYÖTÄ O JA TOISIN PÄIN")
siirto = asd.valitse_paras_siirto()
loppu = time()

print("Aikaa meni:", loppu - alku)
print(siirto)