import unittest
from tekoaly.heurestiikka import arvioi_vaakasuorat, arvioi_pystysuorat, arvioi_diagonaalit_vasemmalta_alas, arvioi_diagonaalit_vasemmalta_ylos


class HeurestiikkaTesti(unittest.TestCase): # vasen alas: 1 + 2 + 2 + 1 + 2 + 4 + 1 + 1 + 1 + 3 = 18
    def setUp(self):                       # pysty: 1 + 9 + 2 + 2 + 1 + 2 + 2 = 19
        self.pelilauta_vaaka_pysty = [   # vaaka: 2 + 2 + 2 + 9 + 2 + 1 = 18
             ['X','O','_','_','_','_','_','_','O','X','X','_','_','_','_','_','_','_','_','_','_','_','_','O','X',],
             ['X','X','_','O','O','O','_','_','O','X','O','_','_','_','_','_','_','_','_','_','_','_','_','X','X',],
             ['O','O','_','X','X','X','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','O','O',],
             ['_','_','_','O','X','O','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
             ['X','O','_','O','_','_','_','_','_','_','_','_','_','_','O','_','_','_','_','_','_','_','_','_','_',],
             ['_','_','_','_','_','_','_','_','_','_','_','_','_','O','O','X','O','_','_','_','_','_','_','_','_',],
             ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','X','X','O','_','_','_','_','_','_','O','O',],
             ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','O','O','_','_','_','_','_','_','O','X','O',],
             ['_','O','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','O','O','X',],
             ['X','O','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','O','X','O',],
             ['X','O','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','O','O',],
             ['X','O','_','_','_','_','_','_','_','_','_','O','O','O','_','_','_','_','O','O','O','_','_','_','_',],
             ['_','_','_','_','_','_','_','_','X','_','_','O','X','O','O','_','_','O','O','X','O','_','_','_','_',],
             ['_','_','_','_','_','_','_','_','_','_','_','O','O','X','O','_','_','O','X','O','O','_','_','_','_',],
             ['_','_','_','_','_','_','_','_','_','_','_','_','O','O','O','_','_','_','O','O','_','_','_','_','_',],
             ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
             ['_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_','_',],
             ['_','_','_','_','_','_','_','_','_','_','_','O','O','_','_','_','_','_','_','_','_','_','_','_','_',],
             ['_','_','_','_','_','_','O','O','O','_','O','X','O','O','_','_','_','_','_','_','_','_','_','_','_',],
             ['_','_','_','_','_','_','O','X','O','O','O','O','X','O','_','_','_','_','_','_','_','_','_','_','_',],
             ['O','O','_','_','_','_','O','O','X','O','_','O','O','O','_','_','_','_','_','_','_','_','O','O','_',],
             ['O','O','O','_','_','_','_','O','O','_','_','_','_','_','_','_','_','_','_','_','_','_','O','O','O',],
             ['X','O','X','O','_','_','_','_','_','_','_','_','_','_','_','_','O','O','_','_','_','O','X','O','X',],
             ['O','X','O','O','_','O','X','O','_','_','_','_','_','_','_','O','O','X','O','_','_','O','O','X','O',],
             ['X','O','_','_','_','O','X','O','_','_','_','_','_','_','_','O','X','O','O','_','_','_','_','O','X',]]
    
    def test_vaaka(self):
        arvo = arvioi_vaakasuorat(self.pelilauta_vaaka_pysty, 25, 'X', 'O')

        self.assertEqual(arvo, 18)

    def test_pysty(self):
        arvo = arvioi_pystysuorat(self.pelilauta_vaaka_pysty, 25, 'X', 'O')

        self.assertEqual(arvo, 19)

    def test_vasen_alas(self):
        arvo = arvioi_diagonaalit_vasemmalta_alas(self.pelilauta_vaaka_pysty, 25, 'X', 'O')

        self.assertEqual(arvo, 23)

    def test_vasen_ylos(self):
        arvo = arvioi_diagonaalit_vasemmalta_ylos(self.pelilauta_vaaka_pysty, 25, 'X', 'O')

        self.assertEqual(arvo, 23)
