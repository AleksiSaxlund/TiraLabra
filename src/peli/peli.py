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
            print(vuoro)
            voitto = self.voiton_tarkistin()
            if voitto == "X" or voitto == "Y":
                # palauttaa voittajan merkin?? None jos ei voittajaa
                print("voitto")
                break

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
        x, y = self.pelilauta.viimeisin_siirto
        print(self.pelilauta.viimeisin_siirto)
        lauta = self.pelilauta.lauta
        # vaaka
        for i in range(1,6):
            if y - 5 + i >= 0 and y + i <= 25:
                jono = lauta[x][y - 5 + i : y + i]
                if len(set(jono)) == 1:
                    return lauta[x][y]
                
        # pysty
        for i in range(1, 6):
            jono = []
            if x - 5 + i >= 0:
                for j in range(5):
                    if x + i <= 25:
                        jono.append(lauta[x - 5 + i + j][y])
                    else:
                        break

            if len(set(jono)) == 1 and "_" not in jono and len(jono) == 5:
                return lauta[x][y]

        #diagonaali vasemmalta alaspäin
        #
        # VIELÄ BUGEJA V
        #
        for i in range(1, 6):
            jono = []
            if x - 5 + i >= 0:
                for j in range(5):
                    if x + i <= 24 and y + j <= 24:
                        #print(x - 5 + i + j, y - 5 + i + j, x + i)
                        jono.append(lauta[x - 5 + i + j][y - 5 + i + j])
                    else:
                        break

            if len(set(jono)) == 1 and "_" not in jono and len(jono) == 5:
                return lauta[x][y]

        # diagonaali vasemmalta ylös
        for i in range(1, 6):
            jono = []
            if x - i >= 0 and y + i <= 24:
                for j in range(5):
                    if x + 5 - i <= 24 and y - 5 + i >= 0:
                        jono.append(lauta[x + 5 - i - j][y - 5 + i + j])
                    else:
                        break

                if len(set(jono)) == 1 and "_" not in jono and len(jono) == 5:
                    return lauta[x][y]

        return False


a = [i for i in range(20)]
y = 7
for i in range(1,6):
    jono = a[y-5+i : y+i]
    print(jono)
            
asd = PeliMoottori()