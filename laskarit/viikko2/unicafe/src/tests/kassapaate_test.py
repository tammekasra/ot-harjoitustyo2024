import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_self(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_riittavan_rahaa_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(240), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_riittavan_rahaa__maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(400), 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_ei_riittavan_rahaa_edullinen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_cash_ei_riittavan_rahaa_maukas(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_rahaa_tarpeeks_edullinen(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.kortti))
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_riittavan_rahaa_maukas(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_ei_riittavan_rahaa_edullinen(self):
        self.kortti.ota_rahaa(800)  # Take 8 euros away
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.kortti))
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 2.00 euroa")
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_ei_riitavana_rahaa__maukas(self):
        self.kortti.ota_rahaa(600)  # Take 6 euros away
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.kortti))
     

    def test_ei_vaihtoa_rahaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahaan_lisaaminen(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000 + 200)
        self.assertEqual(str(self.kortti), "Kortilla on rahaa 12.00 euroa")
