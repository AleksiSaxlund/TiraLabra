from time import time
from heurestiikka import arvioi


class MiniMax():
    """Minimax algoritmin luokka
    """

    def __init__(self, lauta, pelaaja):
        self.n = len(lauta)
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
        paras_arvo = -10**6
        paras_siirto = (-1, -1)

        for i in range(self.n):
            for j in range(self.n):

                if self.lauta[i][j] == "_":
                    print(i, j)

                    self.lauta[i][j] = self.maksivoitava

                    siirron_arvo = self.minimax(self.lauta, 0, -10**5, 10**5, self.vuoro)

                    self.lauta[i][j] = "_"

                    if siirron_arvo > paras_arvo:
                        paras_arvo = siirron_arvo
                        paras_siirto = (i, j)
        print(paras_arvo)
        return paras_siirto

    def siirtoja_jaljella(self, lauta):
        """Tarkistaa, että onko enää mahdollista tehdä siirtoja.

        Args:
            lauta (list): Pelilauta

        Returns:
            bool: True, jos on siirtoja, False jos ei.
        """
        for i in range(self.n-1):
            if "_" in lauta[i]:
                return True
        return False

    def minimax(self, lauta, syvyys, alpha, beta, vuoro):
        """Minimaxin rekursiivinen funktio itsessään.

        Args:
            lauta (list): Pelilauta
            syvyys (int): Pelipuun tämänhetkinen syvyys.
            vuoro (int): Kumman vuoro. 1 = maksimoitava ja -1 = minivoitava.

        Returns:
            int: Palauttaa siirron arvon.
        """
        if vuoro == 1:
            arvo = arvioi(lauta, self.maksivoitava)
        else:
            arvo = -arvioi(lauta, self.minivoitava)
        

        if arvo == 10**5:
            return arvo - syvyys
        if arvo == -10**5:
            return arvo + syvyys

        if syvyys >= 3:
            return arvo

        if not self.siirtoja_jaljella(lauta):
            return 0

        if vuoro == 1:
            paras = -10**5

            for i in range(self.n):
                for j in range(self.n):

                    if lauta[i][j] == "_":
                        lauta[i][j] = self.maksivoitava

                        arvo = self.minimax(lauta, syvyys+1, alpha, beta, vuoro*-1)

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

                        arvo = self.minimax(lauta, syvyys, alpha, beta, vuoro*-1)

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
    lauta = [["_", "_", "_", "_", "_", "X"],
             ["X", "O", "O", "O", "X", "X"],
             ["X", "O", "O", "X", "O", "_"],
             ["O", "X", "X", "X", "X", "_"],
             ["_", "O", "O", "X", "O", "O"],
             ["O", "_", "X", "X", "X", "_"]]
             #["_", "_", "_", "_", "_", "_", "_"],
             #["_", "_", "_", "_", "_", "_", "_"]]
             #["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
             #["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
             #["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]]

asd = MiniMax(lauta, "O")
    # MiniMax(lauta, "JOS PELAAJA ON X SYÖTÄ O JA TOISIN PÄIN")
siirto = asd.valitse_paras_siirto()
loppu = time()

print("Aikaa meni:", loppu - alku)
print(siirto)