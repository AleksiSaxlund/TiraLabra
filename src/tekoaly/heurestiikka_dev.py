
class Heurestiikka():
    def __init__(self):
        self.arvo = 0
        self.suunnat = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
    
    def paivita_arvo(self, arvo):
        self.arvo = arvo

    def paivita_arvio(self, lauta, x, y, arvioitava):
        arvo = self.arvo
        for delta_rivi, delta_sarake in self.suunnat:
            
            valiarvo, auki_alussa, auki_lopussa = self.laske_rivi(lauta, x, y, delta_rivi, delta_sarake, arvioitava)
        
            if valiarvo == 0:
                arvo += 0
            elif valiarvo == 1:
                arvo += 2 if auki_alussa and auki_lopussa else 1
            elif valiarvo == 2:
                arvo += 40 if auki_alussa and auki_lopussa else 20
            elif valiarvo == 3:
                arvo += 60 if auki_alussa and auki_lopussa else 30
            elif valiarvo == 4:
                arvo += 80 if auki_alussa and auki_lopussa else 40

        return arvo
    
    def laske_rivi(self, lauta, x, y, delta_rivi, delta_sarake, arvioitava):
        valiarvo = 0

        if lauta[x - delta_rivi][y - delta_sarake] == "_" or lauta[x - delta_rivi][y - delta_sarake] == arvioitava:
            auki_alussa = True
        else:
            auki_alussa = False

        for i in range(5):
            uusi_x = x + i * delta_rivi
            uusi_y = y + i * delta_sarake

            if not (0 <= uusi_x < 20 and 0 <= uusi_y < 20):
                break

            if lauta[uusi_x][uusi_y] == "_":
                return valiarvo, auki_alussa, True

            elif lauta[uusi_x][uusi_y] == arvioitava:
                valiarvo += 1

            else:
                return valiarvo, auki_alussa, False
