import unittest
from tekoaly.minimax import MiniMax
from testit.pelilaudat import Pelilaudat


class PelilautaTesti(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None
        self.pelilaudat = Pelilaudat().pelilaudat
        self.n = 25

    def test_voitto_1_paassa_X(self):
        lauta = self.pelilaudat["voitto_1_paassa_X"]
        
        minimax = MiniMax(lauta, "O")

        for x in range(self.n):
            for y in range(self.n):
                if lauta[x][y] == "X" or lauta[x][y] == "O":
                    minimax.lisaa_varattu_paikka(x, y)
        
        self.assertEqual(minimax.valitse_paras_siirto(), ((7, 10), True, (7, 10), 'X'))

    def test_voitto_1_paassa_O(self):
        lauta = self.pelilaudat["voitto_1_paassa_O"]
        
        minimax = MiniMax(lauta, "X")

        for x in range(self.n):
            for y in range(self.n):
                if lauta[x][y] == "X" or lauta[x][y] == "O":
                    minimax.lisaa_varattu_paikka(x, y)
        
        self.assertEqual(minimax.valitse_paras_siirto(), ((7, 13), True, (7, 13), 'O'))
    
    def test_estaa_voiton_1_paassa_X(self):
        lauta = self.pelilaudat["estaa_voiton_1_paassa_X"]
        
        minimax = MiniMax(lauta, "O")

        for x in range(self.n):
            for y in range(self.n):
                if lauta[x][y] == "X" or lauta[x][y] == "O":
                    minimax.lisaa_varattu_paikka(x, y)
        
        self.assertEqual(minimax.valitse_paras_siirto(), ((13, 12), True, (13, 12), 'O'))
    
    def test_estaa_voiton_1_paassa_O(self):
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
        siirto = minimax.valitse_paras_siirto()
        siirrot.append(siirto)

        minimax.lauta[siirto[0][0]][siirto[0][1]] = "X"
        minimax.lisaa_varattu_paikka(siirto[0][0], siirto[0][1])

        siirrot.append(minimax.valitse_paras_siirto())

        self.assertEqual(siirrot, [((9, 8), True, (9, 8), 'X'), ((9, 7), True, (9, 7), 'X')])
    
    def test_voitto_2_paassa_O(self):
        lauta = self.pelilaudat["voitto_2_paassa_O"]

        minimax = MiniMax(lauta, "X")

        for x in range(self.n):
            for y in range(self.n):
                if lauta[x][y] == "X" or lauta[x][y] == "O":
                    minimax.lisaa_varattu_paikka(x, y)
        
        siirrot = []
        siirto = minimax.valitse_paras_siirto()
        siirrot.append(siirto)

        minimax.lauta[siirto[0][0]][siirto[0][1]] = "O"
        minimax.lisaa_varattu_paikka(siirto[0][0], siirto[0][1])

        siirrot.append(minimax.valitse_paras_siirto())

        self.assertEqual(siirrot, [((0, 2), True, (0, 2), 'O'), ((0, 3), True, (0, 3), 'O')])