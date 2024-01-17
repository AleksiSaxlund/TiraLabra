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
        self.tutkittavat_paikat = deque()

        self.minivoitava = pelaaja
        if self.minivoitava == "X":
            self.maksivoitava = "O"
            self.vuoro = -1
        else:
            self.maksivoitava = "X"
            self.vuoro = -1
        
        if False:
            for x in range(self.n):
                for y in range(self.n):
                    if lauta[x][y] == "X" or lauta[x][y] == "O":
                        self.lisaa_varattu_paikka(x, y)

    def __varatut_paikat_append(self, koordinaatit: tuple):
        """Lisää varatut paikat listaan.

        Args:
            koordinaatit (tuple): Koordinaatit, jotka lisätään.
        """
        self.varatut_paikat.append(koordinaatit)
    
    def __kasvata_siirtojen_maaraa(self):
        """Kasvattaa siirtojen määrää yhdellä.
        """
        self.siirtojen_maara += 1

    def lisaa_varattu_paikka(self, x: int, y: int):
        """Lisää paikan varattujen paikojen listaan.

        Args:
            x (int): X-koordinaatti
            y (int): Y-koordinaatti
        """
        self.__varatut_paikat_append((x, y))
        self.__kasvata_siirtojen_maaraa()

        self.tutkittavat_paikat = self.lisaa_tutkittavat_paikat(
            self.tutkittavat_paikat, self.varatut_paikat, True)


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
        if ensimmainen:
            print(tutkittavat_paikat)
        return tutkittavat_paikat

    def valitse_paras_siirto(self):
        self.voitto_loytynyt = False
        self.voitto_siirto = (-1, -1)
        self.voitto_nappi = "_"

        paras_arvo = -inf
        paras_siirto = (-1, -1)
        syvyys = 3
        self.alkuperainen_syvyys = syvyys
        self.loydetty = inf
        self.asd = 0

        # Tekoälyn ensimmäinen siirto kovakoodattu tulemaan aina keskelle.
        if len(self.varatut_paikat) == 1:
            return ((self.varatut_paikat[0][0] + 1, self.varatut_paikat[0][1] + 1),
                    self.voitto_loytynyt, self.voitto_siirto, self.voitto_nappi)
        elif self.varatut_paikat == []:
            return ((self.n // 2, self.n // 2), self.voitto_loytynyt, self.voitto_siirto, self.voitto_nappi)

        # Siirron valitsija itsessään. Käy läpi kaikki tutkittavat paikat ja valitsee niistä parhaan.
        for paikka in self.tutkittavat_paikat:
            if self.lauta[paikka[0]][paikka[1]] == "_":
                print(f"Ladataan... {self.tutkittavat_paikat.index(paikka)+1}/{len(self.tutkittavat_paikat)}")
                self.lauta[paikka[0]][paikka[1]] = self.maksivoitava

                varatut_paikat_kopio = self.varatut_paikat[:]
                varatut_paikat_kopio.append((paikka))
                tutkittavat_paikat_kopio = self.lisaa_tutkittavat_paikat(self.tutkittavat_paikat.copy(),
                                                                         varatut_paikat_kopio, False)

                siirron_arvo = self.minimax(self.lauta, syvyys, -inf, inf, self.vuoro, paikka,
                                            tutkittavat_paikat_kopio, varatut_paikat_kopio)
                
                if False:
                    self.tulosta_lauta()
                    print(f"Siirron arvo: {siirron_arvo}")
                    input()

                self.lauta[paikka[0]][paikka[1]] = "_"

                if siirron_arvo >= 10**5 - 1:
                    print("voitto maksimoitava")
                    return self.voitto_siirto, self.voitto_loytynyt, self.voitto_siirto, self.voitto_nappi
                elif siirron_arvo <= -10**5 + 2:
                    print("voitto minimoitava")
                    return self.voitto_siirto, self.voitto_loytynyt, self.voitto_siirto, self.voitto_nappi

                if siirron_arvo > paras_arvo:
                    paras_arvo = siirron_arvo
                    paras_siirto = paikka

        return paras_siirto, self.voitto_loytynyt, self.voitto_siirto, self.voitto_nappi

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
                        self.tulosta_lauta()
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
                        self.tulosta_lauta()
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
                        self.tulosta_lauta()
                        return tarkistettava
                else:
                    loydot = 0

        # diagonaali vasemmalta ylös
        loydot = 0
        for i in range(-4, 5):

            if x + i >= 0 and y + i >= 0 and x + i < self.n and y + i < self.n:
                if self.lauta[x - i][y + i] == tarkistettava:
                    loydot += 1

                    if loydot == 5:
                        self.tulosta_lauta()
                        return tarkistettava
                else:
                    loydot = 0

        return False

    def tulosta_lauta(self):
        """Tulostaa pelilaudan.
        """
        pass
        for i in range(self.n):
            for j in range(self.n):
                print(self.lauta[i][j], end=" ")
            print()

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
        if len(self.varatut_paikat) >= 6:
            self.tulosta_lauta()
            input()
        voitto = self.voiton_tarkistin(paikka[0], paikka[1])
        if voitto != False:
            self.loydetty = min(self.loydetty, syvyys)
            self.voitto_siirto = (paikka[0], paikka[1])
            self.voitto_nappi = voitto
            self.voitto_loytynyt = True
            if voitto == self.maksivoitava:
                print(10**5 - (self.alkuperainen_syvyys - syvyys))
                return 10**5 - (self.alkuperainen_syvyys - syvyys)
            print(10**5 - (self.alkuperainen_syvyys - syvyys))
            return -10**5 + (self.alkuperainen_syvyys - syvyys)

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
                    varatut_paikat.append((paikka))
                    tutkittavat_paikat_kopio = self.lisaa_tutkittavat_paikat(tutkittavat_paikat.copy(),
                                                                             varatut_paikat, False)

                    arvo = self.minimax(lauta, syvyys-1, alpha, beta, vuoro*-1, paikka,
                                        tutkittavat_paikat_kopio, varatut_paikat)

                    paras = max(arvo, paras)
                    alpha = max(alpha, arvo)

                    varatut_paikat.pop()
                    lauta[paikka[0]][paikka[1]] = "_"
                    if beta <= alpha or abs(paras) >= 10**5 - self.alkuperainen_syvyys:
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
                    varatut_paikat.append((paikka))
                    tutkittavat_paikat_kopio = self.lisaa_tutkittavat_paikat(tutkittavat_paikat.copy(),
                                                                             varatut_paikat, False)

                    arvo = self.minimax(lauta, syvyys-1, alpha, beta, vuoro*-1, paikka,
                                        tutkittavat_paikat_kopio, varatut_paikat)

                    paras = min(arvo, paras)
                    beta = min(beta, arvo)

                    varatut_paikat.pop()
                    lauta[paikka[0]][paikka[1]] = "_"
                    if beta <= alpha or abs(paras) >= 10**5 - self.alkuperainen_syvyys:
                        break
            return paras

