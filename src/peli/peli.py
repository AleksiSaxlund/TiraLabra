import kayttoliittyma
import pelilauta

class PeliMoottori():
    def __init__(self):
        self.kayttoliittyma = kayttoliittyma.Kayttoliittyma()
        self.pelaaja = self.pelin_alku()
        self.pelilauta = pelilauta.Pelilauta(self.pelaaja)

    def pelin_alku(self):
        self.kayttoliittyma.alku()

    def peli_kierros(self):
        vuoro = "X"

        while True:
            self.voiton_tarkistin()
            


    
    def voiton_tarkistin(self):
        pass


            
asd = PeliMoottori()