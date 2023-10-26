
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
        self.tulosta_tyhjää()
        for rivi in pelilauta:
            hieno_rivi = "".join(rivi)
            print(hieno_rivi)

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
