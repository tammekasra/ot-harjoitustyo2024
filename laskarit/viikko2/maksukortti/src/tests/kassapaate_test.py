import unittest
from maksukortti import Maksukortti
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()  # Creating an instance of Kassapaate class for testing

    def test_kassapaate_alustus(self):
        # Testing the initialization of Kassapaate class
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_edullisesti(self):
        # Testing cash purchase of affordable meal
        self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)  # Check if cash in register increased
        self.assertEqual(self.kassapaate.edulliset, 1)            # Check if affordable meals sold increased

    def test_kateisosto_maukkaasti(self):
        # Testing cash purchase of hearty meal
        self.kassapaate.syo_maukkaasti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)  # Check if cash in register increased
        self.assertEqual(self.kassapaate.maukkaat, 1)             # Check if hearty meals sold increased

    def test_kateisosto_ei_riittava_edullinen(self):
        # Testing cash purchase of affordable meal with insufficient payment
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  # Check if cash in register remains unchanged
        self.assertEqual(self.kassapaate.edulliset, 0)            # Check if no affordable meals sold

    def test_kateisosto_ei_riittava_maukas(self):
        # Testing cash purchase of hearty meal with insufficient payment
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)  # Check if cash in register remains unchanged
        self.assertEqual(self.kassapaate.maukkaat, 0)     