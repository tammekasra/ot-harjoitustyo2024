import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)
    def test_jos_on_oikea_summa(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")
    def test_jos_lataa_oikeain(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")
    def test_rahaa_ottaaminen_toimii_oikein(self):
        self.maksukortti.ota_rahaa(500) #ottaa rahaa, ja see vahenee
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
        self.maksukortti.ota_rahaa(600) #jos ottaa liikaa raha, niin summa on sama
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")
        self.maksukortti.ota_rahaa(100)
        self.assertTrue( True, self.maksukortti) #on Riittavan maara rahaa!
