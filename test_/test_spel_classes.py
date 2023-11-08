import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import spel_classes as cls



class spel_classes_test (unittest.TestCase):
    
    def setUp(self):
        self.speler_per_troef = cls.speler_per_troef_info()


    def test_bepaal_winst__geval__winst_wel_gespeeld(self):
        self.speler_per_troef._gespeeld = True
        result = True
        self.speler_per_troef._winst = self.speler_per_troef.bepaal_winst(9, 11)
        self.assertEqual(result, self.speler_per_troef._winst)

    def test_bepaal_winst__geval__winst_niet_gespeeld(self):
        self.speler_per_troef._gespeeld = False
        result = True
        self.speler_per_troef._winst = self.speler_per_troef.bepaal_winst(9, 6)
        self.assertEqual(result, self.speler_per_troef._winst)

    def test_bepaal_winst__geval__geen_winst_wel_gespeeld(self):
        self.speler_per_troef._gespeeld =True
        result = False
        self.speler_per_troef._winst = self.speler_per_troef.bepaal_winst(9, 8)
        self.assertEqual(result, self.speler_per_troef._winst)

    def test_bepaal_winst__geval__geen_winst_niet_gespeeld(self):
        self.speler_per_troef._gespeeld = False
        result = False
        self.speler_per_troef._winst = self.speler_per_troef.bepaal_winst(9, 11)
        self.assertEqual(result, self.speler_per_troef._winst)
    
    def test_bepaal_winst__geval__winst_wel_gespeeld_met_gelijk_aantal_slagen(self):
        self.speler_per_troef._gespeeld = True
        result = True
        self.speler_per_troef._winst = self.speler_per_troef.bepaal_winst(9, 9)
        self.assertEqual(result, self.speler_per_troef._winst)

    def test_bepaal_winst__geval__geen_winst_niet_gespeeld_met_gelijk_aantal_slagen(self):
        self.speler_per_troef._gespeeld = False
        result = False
        self.speler_per_troef._winst = self.speler_per_troef.bepaal_winst(9, 9)
        self.assertEqual(result, self.speler_per_troef._winst)


    def test_bepaal_punten__geval__winst_wel_gespeeld_2_spelers(self):
        self.speler_per_troef._gespeeld = True
        self.speler_per_troef._winst = True
        result = 3
        self.speler_per_troef._punten = self.speler_per_troef.bepaal_punten(2, 9, 10)
        self.assertEqual(result, self.speler_per_troef._punten)

    def test_bepaal_punten__geval__winst_wel_gespeeld_1_spelers(self):
        self.speler_per_troef._gespeeld = True
        self.speler_per_troef._winst = True
        result = 9
        self.speler_per_troef._punten = self.speler_per_troef.bepaal_punten(1, 9, 10)
        self.assertEqual(result, self.speler_per_troef._punten)

    def test_bepaal_punten__geval__geen_winst_wel_gespeeld_2_spelers(self):
        self.speler_per_troef._gespeeld = True
        self.speler_per_troef._winst = False
        result = -4
        self.speler_per_troef._punten = self.speler_per_troef.bepaal_punten(2, 9, 7)
        self.assertEqual(result, self.speler_per_troef._punten)

    def test_bepaal_punten__geval__geen_winst_wel_gespeeld_1_spelers(self):
        self.speler_per_troef._gespeeld = True
        self.speler_per_troef._winst = False
        result = -12
        self.speler_per_troef._punten = self.speler_per_troef.bepaal_punten(1, 9, 7)
        self.assertEqual(result, self.speler_per_troef._punten)

    def test_bepaal_punten__geval__winst_niet_gespeeld_2_spelers(self):
        self.speler_per_troef._gespeeld = False
        self.speler_per_troef._winst = True
        result = 3
        self.speler_per_troef._punten = self.speler_per_troef.bepaal_punten(2, 9, 8)
        self.assertEqual(result, self.speler_per_troef._punten)

    def test_bepaal_punten__geval__winst_niet_gespeeld_1_spelers(self):
        self.speler_per_troef._gespeeld = False
        self.speler_per_troef._winst = True
        result = 3
        self.speler_per_troef._punten = self.speler_per_troef.bepaal_punten(1, 9, 8)
        self.assertEqual(result, self.speler_per_troef._punten)

    def test_bepaal_punten__geval__geen_winst_niet_gespeeld_2_spelers(self):
        self.speler_per_troef._gespeeld = False
        self.speler_per_troef._winst = False
        result = -3
        self.speler_per_troef._punten = self.speler_per_troef.bepaal_punten(2, 9, 10)
        self.assertEqual(result, self.speler_per_troef._punten)

    def test_bepaal_punten__geval__geen_winst_niet_gespeeld_1_spelers(self):
        self.speler_per_troef._gespeeld = False
        self.speler_per_troef._winst = False
        result = -3
        self.speler_per_troef._punten = self.speler_per_troef.bepaal_punten(1, 9, 10)
        self.assertEqual(result, self.speler_per_troef._punten)



if __name__ == '__main__':
    unittest.main()