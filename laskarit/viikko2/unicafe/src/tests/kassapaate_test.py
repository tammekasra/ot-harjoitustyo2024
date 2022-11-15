import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Kassapaate()
        self.maksukortti2 = Maksukortti(1000)
    def test_luotu_kortti_on_olemassa(self):
        self.assertEqual(self.maksukortti.kassassa_rahaa, 100000)
        self.assertEqual(self.maksukortti.maukkaat, 0)
        self.assertEqual(self.maksukortti.edulliset, 0)    
    def test_jos_lataa_oikeain(self):
        self.assertEqual(self.maksukortti.syo_edullisesti_kateisella(250), 10)
        self.assertEqual(self.maksukortti.kassassa_rahaa,100240)
        self.assertEqual(self.maksukortti.edulliset,1)
        self.assertEqual(self.maksukortti.syo_maukkaasti_kateisella(550), 150)
        self.assertEqual(self.maksukortti.kassassa_rahaa,100640)
        self.assertEqual(self.maksukortti.maukkaat,1)
        self.assertEqual(self.maksukortti.syo_maukkaasti_kateisella(399), 399)
        self.assertEqual(self.maksukortti.kassassa_rahaa,100640)
        self.assertEqual(self.maksukortti.maukkaat,1)
        self.assertEqual(self.maksukortti.syo_edullisesti_kateisella(199), 199)
        self.assertEqual(self.maksukortti.kassassa_rahaa,100640)
        self.assertEqual(self.maksukortti.edulliset,1)
    
    def test_maksukortti_kortilla_tarpeeks_raha(self):
        self.assertEqual(self.maksukortti2.ota_rahaa(100),True)
        self.assertEqual(self.maksukortti.syo_edullisesti_kateisella(self.maksukortti2.saldo), 660)
        self.assertEqual(self.maksukortti.edulliset,1)

        self.assertEqual(self.maksukortti2.ota_rahaa(9901),False)
        self.maksukortti2.ota_rahaa(9900)
        self.assertEqual(self.maksukortti.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.maksukortti.edulliset,1)
    
       
 

