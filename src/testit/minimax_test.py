import unittest
from tekoaly.minimax import MiniMax
from testit.pelilaudat import Pelilaudat


class PelilautaTesti(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.pelilaudat = Pelilaudat().pelilaudat
        self.n = 25

    def atest_voitto_1_paassa_X(self):
        lauta = self.pelilaudat["voitto_1_paassa_X"]
        
        minimax = MiniMax(lauta, "O")

        for x in range(self.n):
            for y in range(self.n):
                if lauta[x][y] == "X" or lauta[x][y] == "O":
                    minimax.lisaa_varattu_paikka(x, y)
        
        self.assertEqual(minimax.valitse_paras_siirto(), ((7, 10), True, (7, 10), 'X'))

    def atest_voitto_1_paassa_O(self):
        lauta = self.pelilaudat["voitto_1_paassa_O"]
        
        minimax = MiniMax(lauta, "X")

        for x in range(self.n):
            for y in range(self.n):
                if lauta[x][y] == "X" or lauta[x][y] == "O":
                    minimax.lisaa_varattu_paikka(x, y)
        
        self.assertEqual(minimax.valitse_paras_siirto(), ((7, 13), True, (7, 13), 'O'))
    
    def atest_estaa_voiton_1_paassa_X(self):
        lauta = self.pelilaudat["estaa_voiton_1_paassa_X"]
        
        minimax = MiniMax(lauta, "O")

        for x in range(self.n):
            for y in range(self.n):
                if lauta[x][y] == "X" or lauta[x][y] == "O":
                    minimax.lisaa_varattu_paikka(x, y)
        
        self.assertEqual(minimax.valitse_paras_siirto(), ((13, 12), True, (13, 12), 'O'))
    
    def atest_estaa_voiton_1_paassa_O(self):
        lauta = self.pelilaudat["estaa_voiton_1_paassa_O"]
        
        minimax = MiniMax(lauta, "X")

        for x in range(self.n):
            for y in range(self.n):
                if lauta[x][y] == "X" or lauta[x][y] == "O":
                    minimax.lisaa_varattu_paikka(x, y)
        
        self.assertEqual(minimax.valitse_paras_siirto(), ((16, 7), True, (16, 7), 'X'))
    
    def test_voitto_2_paassa_X(self):
        lauta = self.pelilaudat["voitto_2_paassa_X"]
        
        minimax = MiniMax(lauta, "O")

        for x in range(self.n):
            for y in range(self.n):
                if lauta[x][y] == "X" or lauta[x][y] == "O":
                    minimax.lisaa_varattu_paikka(x, y)
        
        siirrot = []
        siirrot.append(minimax.valitse_paras_siirto())
        minimax.lisaa_varattu_paikka(siirrot[0][0][0], siirrot[0][0][1])
        minimax.lauta[siirrot[0][0][0]][siirrot[0][0][1]] = "X"
        siirrot.append(minimax.valitse_paras_siirto())

        self.assertEqual(siirrot, [((9, 7), True, (9, 7), 'X'), ((9, 8), True, (9, 8), 'X')])