import unittest
from peli.pelilauta import Pelilauta


class PelilautaTesti(unittest.TestCase):
    def setUp(self):
        self.pelilauta = Pelilauta("X", False)
        self.alkuperäinen_lauta = self.pelilauta.lauta[:]

    def test_siirto_toimii(self):
        self.pelilauta.siirto("3 5", "X")
        self.pelilauta.siirto("3 24", "O")

        self.assertEqual(self.pelilauta.lauta[2], ['_', '_', '_', '_', 'X', '_', '_', '_', '_',
                         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'O', '_'])

    def test_ei_mene_rajojen_yli(self):
        returnit = []
        returnit.append(self.pelilauta.siirto("3 34", "X"))
        returnit.append(self.pelilauta.siirto("-1 5", "0"))

        self.assertEqual((self.pelilauta.lauta, returnit),
                         (self.alkuperäinen_lauta, [False, False]))

    def test_ei_mene_paallekkain(self):
        returnit = []
        returnit.append(self.pelilauta.siirto("16 5", "X"))
        returnit.append(self.pelilauta.siirto("16 5", "0"))
        returnit.append(self.pelilauta.siirto("16 5", "X"))

        self.assertEqual((self.pelilauta.lauta[15], returnit), (['_', '_', '_', '_', 'X', '_', '_', '_', '_',
                         '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], [True, False, False]))

    def test_virheelliset_syotteet(self):
        returnit = []
        returnit.append(self.pelilauta.siirto("12 ", "X"))
        returnit.append(self.pelilauta.siirto("  ", "X"))
        returnit.append(self.pelilauta.siirto("1232", "O"))
        returnit.append(self.pelilauta.siirto("asd", "O"))
        returnit.append(self.pelilauta.siirto("12 12", "A"))
        returnit.append(self.pelilauta.siirto("16 5 2", "X"))
        returnit.append(self.pelilauta.siirto("2 15", "X"))

        self.assertEqual(returnit, [False, False, False, False, False, False, True])