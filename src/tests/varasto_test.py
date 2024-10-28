import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uuden_varaston_luonti_virheellisellä_tilavuudella(self):
        self.assertEqual(Varasto(-10).tilavuus, 0)

    def test_uuden_varaston_luonti_virheellisellä_alkusaldolla(self):
        self.assertEqual(Varasto(-10, -10).saldo, 0)

    def test_uuden_varaston_alkusaldo_korkeintaan_tilavuus(self):
        self.assertEqual(Varasto(10, 20).saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_ei_tee_mitaan_negatiiviselle_maaralle(self):
        self.varasto.lisaa_varastoon(-1)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisays_lisaa_korkeintaan_mita_mahtuu(self):
        self.varasto.lisaa_varastoon(1000)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_ei_tee_mitaan_negatiivisella_maaralla(self):
        self.varasto.lisaa_varastoon(8)

        self.assertEqual(self.varasto.ota_varastosta(-2), 0)

    def test_ottaa_voi_korkeintaan_sen_mita_on(self):
        self.varasto.lisaa_varastoon(8)

        self.assertEqual(self.varasto.ota_varastosta(1000), 8)

    def test_varasto_merkkijonona(self):
        self.assertEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
