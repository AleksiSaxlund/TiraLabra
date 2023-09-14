
class Kayttoliittyma():
    def __init__(self):
        pass

    def alku(self):
        print("Valitse nappulasi: (X (ÄX) tai O (NOLLA))")
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
        for rivi in pelilauta:
            hieno_rivi = "".join(rivi)
            print(hieno_rivi)

    def tulosta_tyhjää(self):
        [print() for i in range(5)]


