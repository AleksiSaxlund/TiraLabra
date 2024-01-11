import unittest
from tekoaly.minimax import MiniMax


class MinimaxUtilsTesti(unittest.TestCase):
    def setUp(self):
        self.pelilauta = [
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
            ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',]]

        self.minimax = MiniMax(self.pelilauta, "X")
        self.maxDiff = None

    def test_lisaa_tutkittavat_paikat_ensimmainen_siirto(self):
        self.minimax.lauta[9][9] = "X"
        self.minimax.lisaa_varattu_paikka(9, 9)

        oikea_lista = [(11, 11), (11, 9), (11, 7), (9, 11), (9, 7), (7, 11), (7, 9), (7, 7), (10, 10), (10, 9), (10, 8), (9, 10), (9, 8), (8, 10), (8, 9), (8, 8)]
        self.assertListEqual(sorted(oikea_lista), sorted(list(self.minimax.tutkittavat_paikat)))

    def test_lisaa_tutkittavat_paikat_toinen_siirto(self):
        self.minimax.lauta[9][9] = "X"
        self.minimax.lisaa_varattu_paikka(9, 9)
        self.minimax.lauta[10][10] = "O"
        self.minimax.lisaa_varattu_paikka(10, 10)

        oikea_lista = [(11, 11), (11, 9), (11, 7), (9, 11), (9, 7), (7, 11), (7, 9), (7, 7), (10, 9), (10, 8), (9, 10), (9, 8), (8, 10), (8, 9), (8, 8), (12, 12), (12, 10), (12, 8), (10, 12), (8, 12), (10, 11), (11, 10)]
        self.assertEqual(sorted(oikea_lista), sorted(list(self.minimax.tutkittavat_paikat)))

    def test_loytyy_voitto_vaaka(self):
        self.minimax.lauta[9][9] = "X"
        self.minimax.lauta[9][10] = "X"
        self.minimax.lauta[9][11] = "X"
        self.minimax.lauta[9][12] = "X"
        self.minimax.lauta[9][13] = "X"

        loydot = []

        for i in range(-2, 7):
            loydot.append(self.minimax.voiton_tarkistin(9, 9 + i))

        self.assertEqual(loydot, [False, False, "X", "X", "X", "X", "X", False, False])
    
    def test_loytyy_voitto_pysty(self):
        self.minimax.lauta[9][9] = "X"
        self.minimax.lauta[10][9] = "X"
        self.minimax.lauta[11][9] = "X"
        self.minimax.lauta[12][9] = "X"
        self.minimax.lauta[13][9] = "X"

        loydot = []

        for i in range(-2, 7):
            loydot.append(self.minimax.voiton_tarkistin(9 + i, 9))

        self.assertEqual(loydot, [False, False, "X", "X", "X", "X", "X", False, False])
    
    def test_loytyy_voitto_vasen_alas(self):
        self.minimax.lauta[9][9] = "X"
        self.minimax.lauta[10][10] = "X"
        self.minimax.lauta[11][11] = "X"
        self.minimax.lauta[12][12] = "X"
        self.minimax.lauta[13][13] = "X"

        loydot = []

        for i in range(-2, 7):
            loydot.append(self.minimax.voiton_tarkistin(9 + i, 9 + i))

        self.assertEqual(loydot, [False, False, "X", "X", "X", "X", "X", False, False])
    
    def test_loytyy_voitto_vasen_ylos(self):
        self.minimax.lauta[9][9] = "X"
        self.minimax.lauta[8][10] = "X"
        self.minimax.lauta[7][11] = "X"
        self.minimax.lauta[6][12] = "X"
        self.minimax.lauta[5][13] = "X"

        loydot = []

        for i in range(-2, 7):
            loydot.append(self.minimax.voiton_tarkistin(9 - i, 9 + i))

        self.assertEqual(loydot, [False, False, "X", "X", "X", "X", "X", False, False])
    
    def test_ei_loydy_voittoa(self):
        self.minimax.lauta[9][9] = "X"
        self.minimax.lauta[9][10] = "X"
        self.minimax.lauta[9][11] = "X"
        self.minimax.lauta[9][12] = "X"
        self.minimax.lauta[9][13] = "X"

        loydot = []

        loydot.append(self.minimax.voiton_tarkistin(9, 9))
        loydot.append(self.minimax.voiton_tarkistin(1, 1))
        loydot.append(self.minimax.voiton_tarkistin(10, 20))
        loydot.append(self.minimax.voiton_tarkistin(20, 10))
        loydot.append(self.minimax.voiton_tarkistin(20, 20))
        loydot.append(self.minimax.voiton_tarkistin(20, 1))
        loydot.append(self.minimax.voiton_tarkistin(6, 24))

        self.assertEqual(loydot, ["X", False, False, False, False, False, False])
    
    def test_voitto_vasen_yla_nurkka_oikein(self):
        self.minimax.lauta[0][0] = "X"

        loydot = self.minimax.voiton_tarkistin(0, 0)

        self.assertEqual(loydot, False)