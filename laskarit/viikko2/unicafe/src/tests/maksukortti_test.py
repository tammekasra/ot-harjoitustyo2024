import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)  

    def test_saldo_oikein(self):
        self.assertEqual(self.kortti.saldo, 1000)

    def test_rahan_lataaminen_oikein(self):
        self.kortti.lataa_rahaa(500)
        self.assertEqual(self.kortti.saldo, 1500)

    def test_rahan_riittavasti(self):
        self.assertTrue(self.kortti.ota_rahaa(500))
        self.assertEqual(self.kortti.saldo, 500)

    def test_rahan_ei_riittavasti(self):
        self.assertFalse(self.kortti.ota_rahaa(1500)) 
        self.assertEqual(self.kortti.saldo, 1000) 
