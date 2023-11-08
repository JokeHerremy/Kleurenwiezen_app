import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import spel_json as jsn

class spel_json_test (unittest.TestCase):
    
    def setUp(self):
        self._json = ''

    def test_speler_json_file_str_met_dames (self):
        spelsoort = 'Dames' 
        speler = 'Joke' 
        gespeeld = True 
        winst = False 
        punten = -2 
        aantal_dames = 1
        self._json = jsn.speler_json_file_str(spelsoort, speler, gespeeld, winst, punten, aantal_dames)
        json_result = '{"naam": "Joke", "gespeeld": "True", "gewonnen": {"winst": "False", "punten": -2, "aantal dames": 1}}'
        self.assertEqual(json_result, self._json)

    def test_speler_json_file_str_met_spel_ (self):
        spelsoort = 'Troef'
        speler = 'Joke' 
        gespeeld = True 
        winst = False 
        punten = -2 
        self._json = jsn.speler_json_file_str(spelsoort, speler, gespeeld, winst, punten)
        json_result = '{"naam": "Joke", "gespeeld": "True", "gewonnen": {"winst": "False", "punten": -2}}'
        self.assertEqual(json_result, self._json)

    def test_spelsoort_json_file_str_met_troef (self):
        spelsoort = 'Troef'
        deler = 'Bram'
        troef = 'Koekes'
        aantal_slagen = 9
        behaalde_slagen = 11
        spelers = '{"naam": "Lucy", "gespeeld": "True", "gewonnen": {"winst": "True", "punten": 4}}, {"naam": "Joke", "gespeeld": "True", "gewonnen": {"winst": "True", "punten": 4}}, {"naam": "Bram", "gespeeld": "False", "gewonnen": {"winst": "False", "punten": -4}}, {"naam": "Frank", "gespeeld": "False", "gewonnen": {"winst": "False", "punten": -4}}'
        json_result = ' "spelsoort": {"soort": {"soort": "Troef", "troef": "Koekes", "aantal slagen": "9", "behaalde slagen": "11"}, "spelers": [{"naam": "Lucy", "gespeeld": "True", "gewonnen": {"winst": "True", "punten": 4}}, {"naam": "Joke", "gespeeld": "True", "gewonnen": {"winst": "True", "punten": 4}}, {"naam": "Bram", "gespeeld": "False", "gewonnen": {"winst": "False", "punten": -4}}, {"naam": "Frank", "gespeeld": "False", "gewonnen": {"winst": "False", "punten": -4}}], "deler": "Bram"}'
        self._json = jsn.spelsoort_json_file_str(spelers, spelsoort, deler, troef, aantal_slagen, behaalde_slagen)
        self.assertEqual(json_result, self._json)

    def test_spelsoort_json_file_str_met_troel (self):
        spelsoort = 'Troel'
        deler = 'Frank'
        troef = 'Klavers'
        aantal_slagen = 9
        behaalde_slagen = 7
        spelers = '{"naam": "Frank", "gespeeld": "True", "gewonnen": {"winst": "False", "punten": -4}}, {"naam": "Bram", "gespeeld": "True", "gewonnen": {"winst": "False", "punten": -4}}, {"naam": "Lucy", "gespeeld": "False", "gewonnen": {"winst": "True", "punten": 4}}, {"naam": "Joke", "gespeeld": "False", "gewonnen": {"winst": "True", "punten": 4}}'
        json_result = ' "spelsoort": {"soort": {"soort": "Troel", "troef": "Klavers", "aantal slagen": "9", "behaalde slagen": "7"}, "spelers": [{"naam": "Frank", "gespeeld": "True", "gewonnen": {"winst": "False", "punten": -4}}, {"naam": "Bram", "gespeeld": "True", "gewonnen": {"winst": "False", "punten": -4}}, {"naam": "Lucy", "gespeeld": "False", "gewonnen": {"winst": "True", "punten": 4}}, {"naam": "Joke", "gespeeld": "False", "gewonnen": {"winst": "True", "punten": 4}}], "deler": "Frank"}'
        self._json = jsn.spelsoort_json_file_str(spelers, spelsoort, deler, troef, aantal_slagen, behaalde_slagen)
        self.assertEqual(json_result, self._json)


    def test_spelsoort_json_file_str_met_spel_ (self):
        spelsoort = 'Kleine Miserie'
        deler = 'Bram'
        spelers = '{"naam": "Joke", "gespeeld": "True", "gewonnen": {"winst": "False", "punten": -20}}, {"naam": "Lucy", "gespeeld": "True", "gewonnen": {"winst": "True", "punten": 20}}, {"naam": "Bram", "gespeeld": "False", "gewonnen": {"winst": "True", "punten": 0}}, {"naam": "Frank", "gespeeld": "False", "gewonnen": {"winst": "True", "punten": 0}}'
        self._json = jsn.spelsoort_json_file_str(spelers, spelsoort, deler)
        json_result = ' "spelsoort": {"soort": {"soort": "Kleine Miserie"}, "spelers": [{"naam": "Joke", "gespeeld": "True", "gewonnen": {"winst": "False", "punten": -20}}, {"naam": "Lucy", "gespeeld": "True", "gewonnen": {"winst": "True", "punten": 20}}, {"naam": "Bram", "gespeeld": "False", "gewonnen": {"winst": "True", "punten": 0}}, {"naam": "Frank", "gespeeld": "False", "gewonnen": {"winst": "True", "punten": 0}}], "deler": "Bram"}'
        self.assertEqual(json_result, self._json)


if __name__ == '__main__':
    unittest.main()