import kayttoliittyma
import pelilauta
from random import randint

class PeliMoottori():
    def __init__(self):
        self.kayttoliittyma = kayttoliittyma.Kayttoliittyma()
        self.pelaaja = self.pelin_alku()
        self.pelilauta = pelilauta.Pelilauta(self.pelaaja, False)
        self.peli_kierros()

    def pelin_alku(self):
        return self.kayttoliittyma.alku()

    def peli_kierros(self):
        vuoro = 1

        while True:

            if self.voiton_tarkistin():
                # palauttaa voittajan merkin?? None jos ei voittajaa
                pass

            self.kayttoliittyma.tulosta_pelilauta(self.pelilauta.lauta)
            
            if vuoro == 1:
                if self.pelaaja == "X":
                    self.pelaajan_vuoro()
                else:
                    self.tekoalyn_vuoro()

            elif vuoro == -1:
                if self.pelaaja == "O":
                    self.pelaajan_vuoro()
                else:
                    self.tekoalyn_vuoro()
            
            vuoro *= -1

    def pelaajan_vuoro(self):
        # Kysyy uutta syötettä pelaajalta kunnes saa laillisen syöteen. 
        onnistunut = True
        while True:
            syote = self.kayttoliittyma.pelaajan_siirto_syote(onnistunut)

            if self.pelilauta.siirto(syote, self.pelaaja):
                break
            onnistunut = False
    
    def tekoalyn_vuoro(self):
        onnistunut = True
        while True:
            
            # huippu temp tekoäly!!
            if self.pelilauta.siirto(f"{randint(0, 25)} {randint(0, 25)}", self.pelilauta.vihu):
                break
            onnistunut = False
    
    def voiton_tarkistin(self):
        pass


            
asd = PeliMoottori()