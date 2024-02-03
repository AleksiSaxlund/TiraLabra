
class Kayttoliittyma():
    def alku(self):
        """Vastaanottaa pelin alun syötteet pelaajalta. Hyväksyy vasta kun hyväksytty syöte.

        Returns:
            str: Pelaajan valitsema nappula
        """
        print("Valitse nappulasi: (X tai O)")
        while True:
            nappula = input("")
            self.tulosta_tyhjää()

            if nappula == "X":
                return "X"
            elif nappula == "O":
                return "O"

            print("Vääränlainen syöte.")
            print('Kirjoita joko "X" tai "O" (Iso Oo kirjain)')

    def tulosta_pelilauta(self, pelilauta: list):
        """Tulostaa pelilaudan nykyisen tilanteen.

        Args:
            pelilauta (list): Pelilautaa esittävä matriisi
        """
        yla_rivi_1 = "                     1 1 1 1 1 1 1 1 1 1 2"
        yla_rivi_2 = "   1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0"
        ala_rivi_1 = "   1 2 3 4 5 6 7 8 9 1 1 1 1 1 1 1 1 1 1 2"
        ala_rivi_2 = "                     0 1 2 3 4 5 6 7 8 9 0"

        koordinaatit = [i for i in range(21, 0, -1)]
        k1 = koordinaatit.copy()

        self.tulosta_tyhjää()
        print(yla_rivi_1)
        print(yla_rivi_2)

        for rivi in range(len(pelilauta)):
            print(str(k1.pop()).rjust(2, " "), end=" ")

            for sarake in range(len(pelilauta[rivi])):
                print(pelilauta[rivi][sarake], end=" ")
            print(koordinaatit.pop())
        
        print(ala_rivi_1)
        print(ala_rivi_2)
        print()

    def pelaajan_siirto_syote(self, onnistunut: bool):
        """Vastaanottaa pelaajalta syötteen.

        Args:
            onnistunut (bool): True, jos ensimmäinen yritys. False, jos annettu vääriä syötteitä samalla kierroksella.

        Returns:
            str: pelaajan antama syöte
        """
        if onnistunut:
            print("Kirjoita ruudun koordinaatit johon tahdot tehdä seuraavan siirtosi.")

        else:
            print("Virheellinen syöte.")
            print('Kirjoita syöte tyylillä "X-koordinaatti Y-koordinaatti"')

        siirto = input("")
        print()
        return siirto

    def tulosta_tyhjää(self):
        [print() for i in range(5)]
