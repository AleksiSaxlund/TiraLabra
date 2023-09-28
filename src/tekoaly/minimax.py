from heurestiikka_temp import heurestiikka


class MiniMax():
    """Minimax algoritmin luokka
    """

    def __init__(self, lauta, pelaaja):
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
        paras_arvo = -1000
        paras_siirto = (-1, -1)

        for i in range(3):
            for j in range(3):

                if self.lauta[i][j] == "_":

                    self.lauta[i][j] = self.maksivoitava

                    siirron_arvo = self.minimax(self.lauta, 0, self.vuoro)

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
        for i in range(3):
            if "_" in lauta[i]:
                return True
        return False

    def minimax(self, lauta, syvyys, vuoro):
        """Minimaxin rekursiivinen funktio itsessään.

        Args:
            lauta (list): Pelilauta
            syvyys (int): Pelipuun tämänhetkinen syvyys.
            vuoro (int): Kumman vuoro. 1 = maksimoitava ja -1 = minivoitava.

        Returns:
            int: Palauttaa siirron arvon.
        """
        arvo = heurestiikka(lauta, self.maksivoitava, self.minivoitava)

        if arvo == 10:
            return arvo - syvyys
        if arvo == -10:
            return arvo + syvyys

        if not self.siirtoja_jaljella(lauta):
            return 0

        if vuoro == 1:
            paras = -1000

            for i in range(3):
                for j in range(3):

                    if lauta[i][j] == "_":
                        lauta[i][j] = self.maksivoitava

                        arvo = self.minimax(lauta, syvyys+1, vuoro*-1)

                        if arvo > paras:
                            paras = arvo

                        lauta[i][j] = "_"
            return paras

        else:
            paras = 1000

            for i in range(3):
                for j in range(3):

                    if lauta[i][j] == "_":
                        lauta[i][j] = self.minivoitava

                        arvo = self.minimax(lauta, syvyys, vuoro*-1)

                        if arvo < paras:
                            paras = arvo

                        lauta[i][j] = "_"
            return paras


lauta = [["_", "_", "_"],
         ["_", "_", "_"],
         ["_", "_", "_"]]

asd = MiniMax(lauta, "X")
print(asd.valitse_paras_siirto())
