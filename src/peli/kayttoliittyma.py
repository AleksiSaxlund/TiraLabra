
class Kayttoliittyma():
    def __init__(self):
        pass

    def alku(self):
        print("Valitse nappulasi: (X tai O)")
        while True:
            nappula = input("")

            if nappula == "X":
                self.tulosta_tyhjää()
                return "X"
            elif nappula == "O":
                self.tulosta_tyhjää()
                return "O"

            print()
            print("Vääränlainen syöte.")
            print('Kirjoita joko "X" tai "O" (Iso Oo kirjain)')
    
    def tulosta_pelilauta(self, pelilauta: list):
        self.tulosta_tyhjää()
        for rivi in pelilauta:
            hieno_rivi = "".join(rivi)
            print(hieno_rivi)
    
    def pelaajan_siirto_syote(self, onnistunut: bool):
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
