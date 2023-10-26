import unittest
from tekoaly.heurestiikka import arvioi_vaakasuorat, arvioi_pystysuorat, arvioi_yksi_diagonaali_vasemmalta_alas, arvioi_yksi_diagonaali_vasemmalta_ylos


class PelilautaTesti(unittest.TestCase):
    def setUp(self):
        self.pelilauta_vaaka_ja_pysty = [["X", "_", "_", "O", "X", "X", "X", "X", "O", "X", "X", "_", "_", "_", "X"],
                                         ["_", "_", "_", "_", "O", "O", "_", "_",
                                             "_", "_", "_", "_", "_", "_", "O"],
                                         ["X", "_", "_", "_", "_", "_", "_", "_",
                                             "_", "_", "_", "_", "_", "_", "_"],
                                         ["X", "O", "_", "_", "_", "_", "_", "_",
                                             "_", "_", "_", "_", "_", "_", "_"],
                                         ["X", "O", "_", "_", "_", "_", "_", "_",
                                             "_", "_", "_", "_", "_", "_", "_"],
                                         ["X", "O", "_", "_", "_", "_", "_", "X",
                                             "_", "_", "_", "_", "_", "_", "_"],
                                         ["_", "_", "_", "_", "_", "_", "X", "X",
                                             "X", "_", "_", "_", "_", "_", "O"],
                                         ["O", "_", "_", "_", "_", "_", "_", "X",
                                             "_", "_", "_", "_", "_", "_", "X"],
                                         ["X", "_", "_", "_", "X", "_", "_", "_",
                                             "_", "_", "_", "_", "_", "_", "X"],
                                         ["X", "_", "_", "X", "X", "_", "_", "_",
                                             "_", "_", "_", "_", "_", "_", "X"],
                                         ["O", "_", "_", "_", "_", "_", "_", "_",
                                             "_", "_", "_", "_", "_", "_", "_"],
                                         ["_", "_", "_", "_", "_", "_", "_", "_",
                                             "_", "_", "_", "_", "_", "_", "_"],
                                         ["_", "_", "_", "_", "_", "_", "_", "_",
                                             "_", "_", "_", "_", "_", "_", "_"],
                                         ["_", "_", "_", "_", "_", "_", "_", "_",
                                             "_", "_", "_", "_", "_", "_", "_"],
                                         ["X", "O", "_", "_", "_", "X", "X", "X", "X", "_", "_", "_", "_", "_", "X"]]
        # Vaaka: 1 + 4 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 400 + 1 + 1 + 1 + 300 + 1 + 6 = 722
        # Pysty: 1 + 400 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 9 + 1 + 1 + 1 + 300 + 1 + 6 = 729

        self.pelilauta_diagonaalit = [["X", "_", "O", "_", "_", "_", "_", "O", "_", "_", "_", "_", "_", "_", "X"],
                                      ["_", "X", "_", "O", "_", "_", "O", "_",
                                          "_", "_", "_", "_", "_", "X", "_"],
                                      ["O", "_", "X", "_", "_", "O", "_", "X",
                                          "_", "O", "_", "_", "X", "_", "_"],
                                      ["_", "O", "_", "_", "O", "_", "X", "_",
                                          "O", "_", "_", "O", "_", "_", "_"],
                                      ["_", "_", "_", "_", "O", "X", "_", "O",
                                          "_", "_", "_", "_", "_", "_", "_"],
                                      ["_", "_", "_", "X", "_", "O", "O", "_",
                                          "_", "_", "_", "_", "_", "_", "_"],
                                      ["_", "_", "O", "_", "X", "_", "O", "_",
                                          "_", "_", "_", "_", "_", "_", "_"],
                                      ["_", "_", "_", "O", "_", "X", "_", "_",
                                          "_", "O", "_", "O", "_", "_", "_"],
                                      ["_", "_", "_", "_", "_", "_", "X", "_",
                                          "O", "_", "X", "_", "_", "_", "_"],
                                      ["_", "_", "_", "_", "_", "_", "_", "_",
                                          "_", "X", "_", "O", "_", "_", "_"],
                                      ["_", "_", "_", "_", "_", "_", "_", "_",
                                          "O", "_", "X", "_", "_", "X", "_"],
                                      ["_", "_", "_", "X", "_", "_", "_", "_",
                                          "_", "O", "_", "O", "X", "_", "_"],
                                      ["_", "_", "X", "_", "_", "_", "_", "_",
                                          "_", "_", "_", "X", "_", "_", "_"],
                                      ["_", "X", "_", "O", "_", "_", "_", "_",
                                          "_", "_", "X", "_", "_", "_", "_"],
                                      ["X", "_", "O", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "X"]]
        # Vasemmalta alas: 1 + 1.5 + 400 + 9 + 1.5 + 1 =
        # Vasemmalta ylös: 16 + 300 + 1 + 1.5 = 318.5

    def test_arvioi_vaakasuorat(self):
        pisteet = arvioi_vaakasuorat(
            self.pelilauta_vaaka_ja_pysty, 15, "X", "O")

        self.assertEqual(pisteet, 722)

    def test_arvioi_pystysuorat(self):
        pisteet = arvioi_pystysuorat(
            self.pelilauta_vaaka_ja_pysty, 15, "X", "O")

        self.assertEqual(pisteet, 729)

    def test_arvioi_diagonaalit_vasemmalta_alas(self):
        pisteet1 = arvioi_yksi_diagonaali_vasemmalta_alas(
            self.pelilauta_diagonaalit, 15, 0, 0, "X", "O")
        pisteet2 = arvioi_yksi_diagonaali_vasemmalta_alas(
            self.pelilauta_diagonaalit, 15, 8, 0, "X", "O")
        pisteet3 = arvioi_yksi_diagonaali_vasemmalta_alas(
            self.pelilauta_diagonaalit, 15, 9, 0, "X", "O")
        pisteet4 = arvioi_yksi_diagonaali_vasemmalta_alas(
            self.pelilauta_diagonaalit, 15, 2, 0, "X", "O")

        self.assertEqual((pisteet1, pisteet2, pisteet3,
                         pisteet4), (10, 1, 0, 400))

    def test_arvioi_diagonaalit_vasemmalta_ylos(self):
        pisteet1 = arvioi_yksi_diagonaali_vasemmalta_ylos(
            self.pelilauta_diagonaalit, 15, 0, 0, "X", "O")
        pisteet2 = arvioi_yksi_diagonaali_vasemmalta_ylos(
            self.pelilauta_diagonaalit, 15, 5, 0, "X", "O")
        pisteet3 = arvioi_yksi_diagonaali_vasemmalta_ylos(
            self.pelilauta_diagonaalit, 15, 0, 4, "X", "O")
        pisteet4 = arvioi_yksi_diagonaali_vasemmalta_ylos(
            self.pelilauta_diagonaalit, 15, 0, 9, "X", "O")

        self.assertEqual((pisteet1, pisteet2, pisteet3,
                         pisteet4), (17, 9, 0, 400))
