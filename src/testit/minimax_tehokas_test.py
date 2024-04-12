import unittest
from tekoaly.minimax import MiniMax
from testit.pelilaudat import Pelilaudat




class PelilautaTesti(unittest.TestCase):
    """Huom! Nämä testit vaatii, että käyt muuttamassa syvyys = 4 minimax.py tiedoston riviltä 99.
    """
    def setUp(self):
        self.maxDiff = None
        self.pelilaudat = Pelilaudat().pelilaudat
        self.n = 20

    def test_pelaa_voiton_X_paranneltu(self):
        lauta = self.pelilaudat["pelaa_voiton_X_paranneltu"]

        minimax = MiniMax(lauta, "O")
        minimax.ensimmainen_siirto = False

        for x in range(self.n):
            for y in range(self.n):
                if lauta[x][y] == "X" or lauta[x][y] == "O":
                    minimax.lisaa_varattu_paikka(x, y)
        
        siirrot = []

        #Tekoälyn siirto
        siirto = minimax.valitse_paras_siirto()
        siirrot.append((siirto[0], siirto[1]))
        minimax.lauta[siirto[0][0]][siirto[0][1]] = "X"
        minimax.lisaa_varattu_paikka(siirto[0][0], siirto[0][1]) #7 7

        #Pelaajan siirto
        minimax.lauta[7][10] = "O"
        minimax.lisaa_varattu_paikka(7, 10)

        siirto = minimax.valitse_paras_siirto()
        siirrot.append((siirto[0], siirto[1]))
        minimax.lauta[siirto[0][0]][siirto[0][1]] = "X"
        minimax.lisaa_varattu_paikka(siirto[0][0], siirto[0][1]) #6 7

        #Pelaajan siirto
        minimax.lauta[10][7] = "O"
        minimax.lisaa_varattu_paikka(10, 7)

        siirto = minimax.valitse_paras_siirto()
        siirrot.append((siirto[0], siirto[1]))
        minimax.lauta[siirto[0][0]][siirto[0][1]] = "X"
        minimax.lisaa_varattu_paikka(siirto[0][0], siirto[0][1])
        
        oikeat_siirrot = [((7, 7), True), ((6, 7), True), ((5, 7), True)]
        self.assertEqual(siirrot, oikeat_siirrot)