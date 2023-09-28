import unittest
from peli.pelimoottori import PeliMoottori


class PelilautaTesti(unittest.TestCase):
    def setUp(self):
        self.pelimoottori = PeliMoottori()
        