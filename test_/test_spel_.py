import unittest
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import spel_ as spl
import spel_classes as cls

class spel_test_create_avond_info (unittest.TestCase):

    def setUp(self):
        spellen_obj_list = []
        datum = '24//10/2023'
        gezelschap_list = ['Bram', 'Frank', 'Lucy', 'Joke']

        # spel 1 enkele picon met winst
        spel = cls.spel()
        spel._id = 1
        spel._deler = 'Bram'
        spel._spelsoort = 'Picon'

        obj_1 = cls.speler_per_spel_info()
        obj_1._naam = 'Bram'
        obj_1._gespeeld = True
        obj_1._winst = True
        obj_1._punten = 15
        obj_2 = cls.speler_per_spel_info()
        obj_2._naam = 'Frank'
        obj_2._gespeeld = False
        obj_2._winst = False
        obj_2._punten = -5
        obj_3 = cls.speler_per_spel_info()
        obj_3._naam = 'Lucy'
        obj_3._gespeeld = False
        obj_3._winst = False
        obj_3._punten = -5
        obj_4 = cls.speler_per_spel_info()
        obj_4._naam = 'Joke'
        obj_4._gespeeld = False
        obj_4._winst = False
        obj_4._punten = -5
        spelers_obj_list = [obj_1, obj_2, obj_3, obj_4]
        spelers_dict = {'Bram': True, 'Frank': False, 'Lucy': False, 'Joke': False}

        spel_result = cls.spel_result(spel)
        spel_result._spelers_list = spelers_obj_list
        spel_result._spelers_dict = spelers_dict

        spellen_obj_list.append(spel_result)

        # spel 2 troef met 2 spelers 
        spel = cls.spel()
        spel._id = 2
        spel._deler = 'Frank'
        spel._spelsoort = 'Troef'
        spel._troef = 'Hartes'
        spel._aantal_slagen = 9
        spel._vrager = 'Lucy'
        spel._meegaander = 'Joke'

        obj_1 = cls.speler_per_troef_info()
        obj_1._naam = 'Bram'
        obj_1._gespeeld = False
        obj_1._winst = False
        obj_1._punten = -3
        obj_2 = cls.speler_per_troef_info()
        obj_2._naam = 'Frank'
        obj_2._gespeeld = False
        obj_2._winst = False
        obj_2._punten = -3
        obj_3 = cls.speler_per_troef_info()
        obj_3._naam = 'Lucy'
        obj_3._gespeeld = True
        obj_3._winst = True
        obj_3._punten = 3
        obj_4 = cls.speler_per_troef_info()
        obj_4._naam = 'Joke'
        obj_4._gespeeld = True
        obj_4._winst = True
        obj_4._punten = 3
        spelers_obj_list = [obj_1, obj_2, obj_3, obj_4]

        spel_result = cls.spel_result_troef(spel)
        spel_result._spelers_list = spelers_obj_list
        spel_result._behaalde_slagen = 10

        spellen_obj_list.append(spel_result)

        result = cls.avond_info(datum, gezelschap_list)
        result._spel_list = spellen_obj_list
        self.create_avond_info = spl.create_avond_info(datum, gezelschap_list, spellen_obj_list)
        return result

    def test_create_avond_info__geval__datum(self):
        result = self.setUp()
        self.assertEqual(result._datum, self.create_avond_info._datum)

    def test_create_avond_info__geval__gezelschap(self):
        result = self.setUp()
        self.assertEqual(result._gezelschap_list, self.create_avond_info._gezelschap_list)

    # test voor spel 1
    def test_create_avond_info__geval__spel_1_spelers_dict(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_dict, self.create_avond_info._spel_list[0]._spelers_dict)

    def test_create_avond_info__geval__spel_1_spel_info_id(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spel_info._id, self.create_avond_info._spel_list[0]._spel_info._id)
    def test_create_avond_info__geval__spel_1_spel_info_deler(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spel_info._deler, self.create_avond_info._spel_list[0]._spel_info._deler)
    def test_create_avond_info__geval__spel_1_spel_info_spelsoort(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spel_info._spelsoort, self.create_avond_info._spel_list[0]._spel_info._spelsoort)

    def test_create_avond_info__geval__spel_1_speler_list__speler_1_naam(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[0]._naam, self.create_avond_info._spel_list[0]._spelers_list[0]._naam)
    def test_create_avond_info__geval__spel_1_speler_list__speler_1_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[0]._gespeeld, self.create_avond_info._spel_list[0]._spelers_list[0]._gespeeld)
    def test_create_avond_info__geval__spel_1_speler_list__speler_1_winst(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[0]._winst, self.create_avond_info._spel_list[0]._spelers_list[0]._winst)
    def test_create_avond_info__geval__spel_1_speler_list__speler_1_punten(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[0]._punten, self.create_avond_info._spel_list[0]._spelers_list[0]._punten)

    def test_create_avond_info__geval__spel_1_speler_list__speler_2_naam(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[1]._naam, self.create_avond_info._spel_list[0]._spelers_list[1]._naam)
    def test_create_avond_info__geval__spel_1_speler_list__speler_2_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[1]._gespeeld, self.create_avond_info._spel_list[0]._spelers_list[1]._gespeeld)
    def test_create_avond_info__geval__spel_1_speler_list__speler_2_winst(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[1]._winst, self.create_avond_info._spel_list[0]._spelers_list[1]._winst)
    def test_create_avond_info__geval__spel_1_speler_list__speler_2_punten(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[1]._punten, self.create_avond_info._spel_list[0]._spelers_list[1]._punten)

    def test_create_avond_info__geval__spel_1_speler_list__speler_3_naam(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[2]._naam, self.create_avond_info._spel_list[0]._spelers_list[2]._naam)
    def test_create_avond_info__geval__spel_1_speler_list__speler_3_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[2]._gespeeld, self.create_avond_info._spel_list[0]._spelers_list[2]._gespeeld)
    def test_create_avond_info__geval__spel_1_speler_list__speler_3_winst(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[2]._winst, self.create_avond_info._spel_list[0]._spelers_list[2]._winst)
    def test_create_avond_info__geval__spel_1_speler_list__speler_3_punten(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[2]._punten, self.create_avond_info._spel_list[0]._spelers_list[2]._punten)

    def test_create_avond_info__geval__spel_1_speler_list__speler_4_naam(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[3]._naam, self.create_avond_info._spel_list[0]._spelers_list[3]._naam)
    def test_create_avond_info__geval__spel_1_speler_list__speler_4_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[3]._gespeeld, self.create_avond_info._spel_list[0]._spelers_list[3]._gespeeld)
    def test_create_avond_info__geval__spel_1_speler_list__speler_4_winst(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[3]._winst, self.create_avond_info._spel_list[0]._spelers_list[3]._winst)
    def test_create_avond_info__geval__spel_1_speler_list__speler_4_punten(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[0]._spelers_list[3]._punten, self.create_avond_info._spel_list[0]._spelers_list[3]._punten)

    # test voor spel 2
    def test_create_avond_info__geval__spel_2_behaalde_slagen(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._behaalde_slagen, self.create_avond_info._spel_list[1]._behaalde_slagen)

    def test_create_avond_info__geval__spel_2_spel_info_id(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spel_info._id, self.create_avond_info._spel_list[1]._spel_info._id)
    def test_create_avond_info__geval__spel_2_spel_info_deler(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spel_info._deler, self.create_avond_info._spel_list[1]._spel_info._deler)
    def test_create_avond_info__geval__spel_2_spel_info_spelsoort(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spel_info._spelsoort, self.create_avond_info._spel_list[1]._spel_info._spelsoort)
    def test_create_avond_info__geval__spel_2_spel_info_troef(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spel_info._troef, self.create_avond_info._spel_list[1]._spel_info._troef)
    def test_create_avond_info__geval__spel_2_spel_info_aantal_slagen(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spel_info._aantal_slagen, self.create_avond_info._spel_list[1]._spel_info._aantal_slagen)
    def test_create_avond_info__geval__spel_2_spel_info_vrager(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spel_info._vrager, self.create_avond_info._spel_list[1]._spel_info._vrager)
    def test_create_avond_info__geval__spel_2_spel_info_meegaander(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spel_info._meegaander, self.create_avond_info._spel_list[1]._spel_info._meegaander)

    def test_create_avond_info__geval__spel_2_speler_list__speler_1_naam(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[0]._naam, self.create_avond_info._spel_list[1]._spelers_list[0]._naam)
    def test_create_avond_info__geval__spel_2_speler_list__speler_1_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[0]._gespeeld, self.create_avond_info._spel_list[1]._spelers_list[0]._gespeeld)
    def test_create_avond_info__geval__spel_2_speler_list__speler_1_winst(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[0]._winst, self.create_avond_info._spel_list[1]._spelers_list[0]._winst)
    def test_create_avond_info__geval__spel_2_speler_list__speler_1_punten(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[0]._punten, self.create_avond_info._spel_list[1]._spelers_list[0]._punten)

    def test_create_avond_info__geval__spel_2_speler_list__speler_2_naam(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[1]._naam, self.create_avond_info._spel_list[1]._spelers_list[1]._naam)
    def test_create_avond_info__geval__spel_2_speler_list__speler_2_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[1]._gespeeld, self.create_avond_info._spel_list[1]._spelers_list[1]._gespeeld)
    def test_create_avond_info__geval__spel_2_speler_list__speler_2_winst(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[1]._winst, self.create_avond_info._spel_list[1]._spelers_list[1]._winst)
    def test_create_avond_info__geval__spel_2_speler_list__speler_2_punten(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[1]._punten, self.create_avond_info._spel_list[1]._spelers_list[1]._punten)

    def test_create_avond_info__geval__spel_2_speler_list__speler_3_naam(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[2]._naam, self.create_avond_info._spel_list[1]._spelers_list[2]._naam)
    def test_create_avond_info__geval__spel_2_speler_list__speler_3_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[2]._gespeeld, self.create_avond_info._spel_list[1]._spelers_list[2]._gespeeld)
    def test_create_avond_info__geval__spel_2_speler_list__speler_3_winst(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[2]._winst, self.create_avond_info._spel_list[1]._spelers_list[2]._winst)
    def test_create_avond_info__geval__spel_2_speler_list__speler_3_punten(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[2]._punten, self.create_avond_info._spel_list[1]._spelers_list[2]._punten)

    def test_create_avond_info__geval__spel_2_speler_list__speler_4_naam(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[3]._naam, self.create_avond_info._spel_list[1]._spelers_list[3]._naam)
    def test_create_avond_info__geval__spel_2_speler_list__speler_4_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[3]._gespeeld, self.create_avond_info._spel_list[1]._spelers_list[3]._gespeeld)
    def test_create_avond_info__geval__spel_2_speler_list__speler_4_winst(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[3]._winst, self.create_avond_info._spel_list[1]._spelers_list[3]._winst)
    def test_create_avond_info__geval__spel_2_speler_list__speler_4_punten(self):
        result = self.setUp()
        self.assertEqual(result._spel_list[1]._spelers_list[3]._punten, self.create_avond_info._spel_list[1]._spelers_list[3]._punten)


class spel_test_create_spel_info__geval__troef (unittest.TestCase):
    def setUp(self):
        deler = 'Frank'
        spelsoort = 'Troef'
        troef = 'Hartes'
        aantal_slagen = 9
        vrager = 'Lucy'
        meegaander = 'Joke'
        spel = cls.spel()
        spel._deler = 'Frank'
        spel._spelsoort = 'Troef'
        spel._troef = 'Hartes'
        spel._aantal_slagen = 9
        spel._vrager = 'Lucy'
        spel._meegaander = 'Joke'
        self.create_spel_info = spl.create_spel_info(deler, spelsoort, troef, aantal_slagen, vrager, meegaander)
        return spel

    def test_create_spel_info__geval__troef_deler(self):
        result = self.setUp()
        self.assertEqual(result._deler, self.create_spel_info._deler)
    def test_create_spel_info__geval__troef_spelsoort(self):
        result = self.setUp()
        self.assertEqual(result._spelsoort, self.create_spel_info._spelsoort)
    def test_create_spel_info__geval__troef_troef(self):
        result = self.setUp()
        self.assertEqual(result._troef, self.create_spel_info._troef)
    def test_create_spel_info__geval__troef_aantal_slagen(self):
        result = self.setUp()
        self.assertEqual(result._aantal_slagen, self.create_spel_info._aantal_slagen)
    def test_create_spel_info__geval__troef_vrager(self):
        result = self.setUp()
        self.assertEqual(result._vrager, self.create_spel_info._vrager)
    def test_create_spel_info__geval__troef_meegaander(self):
        result = self.setUp()
        self.assertEqual(result._meegaander, self.create_spel_info._meegaander)

class spel_test_create_spel_info__geval__picon (unittest.TestCase):
    def setUp(self):
        deler = 'Frank'
        spelsoort = 'Picon'
        spel = cls.spel()
        spel._deler = 'Frank'
        spel._spelsoort = 'Picon'
        self.create_spel_info = spl.create_spel_info(deler, spelsoort)
        return spel

    def test_create_spel_info__geval__picon_deler(self):
        result = self.setUp()
        self.assertEqual(result._deler, self.create_spel_info._deler)
    def test_create_spel_info__geval__picon_spelsoort(self):
        result = self.setUp()
        self.assertEqual(result._spelsoort, self.create_spel_info._spelsoort)


class spel_test_create_spelers_info_list_in_spel_info__geval__troef_met_2(unittest.TestCase):
    def setUp(self):
        spel_info = cls.spel()
        spel_info._deler = 'Bram'
        spel_info._spelsoort = 'Troef'
        spel_info._troef = 'Hartes'
        spel_info._aantal_slagen = 9
        spel_info._vrager = 'Lucy'
        spel_info._meegaander = 'Joke'
        gezelschap_list = ['Bram', 'Frank', 'Lucy', 'Joke']
        spel_result = cls.spel_result_troef(spel_info)
        spel_result._behaalde_slagen = 10
        self.spelers_info_list = spl.create_spelers_info_list_in_spel_info(spel_info, gezelschap_list, spel_result)

        obj_1 = cls.speler_per_troef_info()
        obj_1._naam = 'Bram'
        obj_1._gespeeld = False
        obj_1._winst = False
        obj_1._punten = -3
        obj_2 = cls.speler_per_troef_info()
        obj_2._naam = 'Frank'
        obj_2._gespeeld = False
        obj_2._winst = False
        obj_2._punten = -3
        obj_3 = cls.speler_per_troef_info()
        obj_3._naam = 'Lucy'
        obj_3._gespeeld = True
        obj_3._winst = True
        obj_3._punten = 3
        obj_4 = cls.speler_per_troef_info()
        obj_4._naam = 'Joke'
        obj_4._gespeeld = True
        obj_4._winst = True
        obj_4._punten = 3
        spelers_obj_list = [obj_3, obj_4, obj_1, obj_2]
        result = spel_result
        result._spelers_list = spelers_obj_list
        return result

    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_1_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._naam, self.spelers_info_list._spelers_list[0]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_1_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._gespeeld, self.spelers_info_list._spelers_list[0]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_1_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._winst, self.spelers_info_list._spelers_list[0]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_1_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._punten, self.spelers_info_list._spelers_list[0]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_2_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._naam, self.spelers_info_list._spelers_list[1]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_2_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._gespeeld, self.spelers_info_list._spelers_list[1]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_2_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._winst, self.spelers_info_list._spelers_list[1]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_2_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._punten, self.spelers_info_list._spelers_list[1]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_3_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._naam, self.spelers_info_list._spelers_list[2]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_3_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._gespeeld, self.spelers_info_list._spelers_list[2]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_3_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._winst, self.spelers_info_list._spelers_list[2]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_3_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._punten, self.spelers_info_list._spelers_list[2]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_4_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._naam, self.spelers_info_list._spelers_list[3]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_4_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._gespeeld, self.spelers_info_list._spelers_list[3]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_4_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._winst, self.spelers_info_list._spelers_list[3]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__speler_4_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._punten, self.spelers_info_list._spelers_list[3]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__troef_met_2__score_som_nul(self):
        som = 0
        for i in range(4):
            som += self.spelers_info_list._spelers_list[i]._punten
        self.assertEqual(0, som)


class spel_test_create_spelers_info_list_in_spel_info__geval__troef_met_1(unittest.TestCase):
    def setUp(self):
        spel_info = cls.spel()
        spel_info._deler = 'Bram'
        spel_info._spelsoort = 'Troef'
        spel_info._troef = 'Koekes'
        spel_info._aantal_slagen = 7
        spel_info._vrager = 'Frank'
        gezelschap_list = ['Bram', 'Frank', 'Lucy', 'Joke']
        spel_result = cls.spel_result_troef(spel_info)
        spel_result._behaalde_slagen = 8
        self.spelers_info_list = spl.create_spelers_info_list_in_spel_info(spel_info, gezelschap_list, spel_result)

        obj_1 = cls.speler_per_troef_info()
        obj_1._naam = 'Bram'
        obj_1._gespeeld = False
        obj_1._winst = False
        obj_1._punten = -3
        obj_2 = cls.speler_per_troef_info()
        obj_2._naam = 'Frank'
        obj_2._gespeeld = True
        obj_2._winst = True
        obj_2._punten = 9
        obj_3 = cls.speler_per_troef_info()
        obj_3._naam = 'Lucy'
        obj_3._gespeeld = False
        obj_3._winst = False
        obj_3._punten = -3
        obj_4 = cls.speler_per_troef_info()
        obj_4._naam = 'Joke'
        obj_4._gespeeld = False
        obj_4._winst = False
        obj_4._punten = -3
        spelers_obj_list = [obj_2, obj_1, obj_3, obj_4]
        result = spel_result
        result._spelers_list = spelers_obj_list
        return result

    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_1_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._naam, self.spelers_info_list._spelers_list[0]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_1_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._gespeeld, self.spelers_info_list._spelers_list[0]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_1_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._winst, self.spelers_info_list._spelers_list[0]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_1_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._punten, self.spelers_info_list._spelers_list[0]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_2_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._naam, self.spelers_info_list._spelers_list[1]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_2_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._gespeeld, self.spelers_info_list._spelers_list[1]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_2_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._winst, self.spelers_info_list._spelers_list[1]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_2_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._punten, self.spelers_info_list._spelers_list[1]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_3_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._naam, self.spelers_info_list._spelers_list[2]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_3_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._gespeeld, self.spelers_info_list._spelers_list[2]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_3_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._winst, self.spelers_info_list._spelers_list[2]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_3_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._punten, self.spelers_info_list._spelers_list[2]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_4_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._naam, self.spelers_info_list._spelers_list[3]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_4_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._gespeeld, self.spelers_info_list._spelers_list[3]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_4_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._winst, self.spelers_info_list._spelers_list[3]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__speler_4_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._punten, self.spelers_info_list._spelers_list[3]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__score_som_nul(self):
        som = 0
        for i in range(4):
            som += self.spelers_info_list._spelers_list[i]._punten
        self.assertEqual(0, som)


class spel_test_create_spelers_info_list_in_spel_info__geval__dames(unittest.TestCase):
    def setUp(self):
        spel_info = cls.spel()
        spel_info._deler = 'Bram'
        spel_info._spelsoort = 'Dames'
        gezelschap_list = ['Bram', 'Frank', 'Lucy', 'Joke']
        spel_result = cls.spel_result_dames(spel_info)
        spel_result._dames_dict = {'Bram': 1, 'Frank': 0, 'Lucy': 3, 'Joke': 0}
        self.spelers_info_list = spl.create_spelers_info_list_in_spel_info(spel_info, gezelschap_list, spel_result)

        obj_1 = cls.speler_per_dames_info
        obj_1._naam = 'Bram'
        obj_1._gespeeld = True
        obj_1._winst = False
        obj_1._punten = -2
        obj_1._aantal_dames = 1
        obj_2 = cls.speler_per_dames_info()
        obj_2._naam = 'Frank'
        obj_2._gespeeld = True
        obj_2._winst = True
        obj_2._punten = 4
        obj_2._aantal_dames = 0
        obj_3 = cls.speler_per_dames_info()
        obj_3._naam = 'Lucy'
        obj_3._gespeeld = True
        obj_3._winst = False
        obj_3._punten = -6
        obj_3._aantal_dames = 3
        obj_4 = cls.speler_per_dames_info()
        obj_4._naam = 'Joke'
        obj_4._gespeeld = True
        obj_4._winst = True
        obj_4._punten = 4
        obj_4._aantal_dames = 0
        spelers_obj_list = [obj_2, obj_4, obj_3, obj_1]
        result = spel_result
        result._spelers_list = spelers_obj_list
        return result

    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_1_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._naam, self.spelers_info_list._spelers_list[0]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_1_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._gespeeld, self.spelers_info_list._spelers_list[0]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_1_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._winst, self.spelers_info_list._spelers_list[0]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_1_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._punten, self.spelers_info_list._spelers_list[0]._punten)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_1_dames(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._aantal_dames, self.spelers_info_list._spelers_list[0]._aantal_dames)

    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_2_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._naam, self.spelers_info_list._spelers_list[1]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_2_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._gespeeld, self.spelers_info_list._spelers_list[1]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_2_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._winst, self.spelers_info_list._spelers_list[1]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_2_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._punten, self.spelers_info_list._spelers_list[1]._punten)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_2_dames(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._aantal_dames, self.spelers_info_list._spelers_list[1]._aantal_dames)

    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_3_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._naam, self.spelers_info_list._spelers_list[2]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_3_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._gespeeld, self.spelers_info_list._spelers_list[2]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_3_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._winst, self.spelers_info_list._spelers_list[2]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_3_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._punten, self.spelers_info_list._spelers_list[2]._punten)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_3_dames(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._aantal_dames, self.spelers_info_list._spelers_list[2]._aantal_dames)

    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_4_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._naam, self.spelers_info_list._spelers_list[3]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_4_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._gespeeld, self.spelers_info_list._spelers_list[3]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_4_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._winst, self.spelers_info_list._spelers_list[3]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_4_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._punten, self.spelers_info_list._spelers_list[3]._punten)
    def test_create_spelers_info_list_in_spel_info__geval__dames__speler_4_dames(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._aantal_dames, self.spelers_info_list._spelers_list[3]._aantal_dames)

    def test_create_spelers_info_list_in_spel_info__geval__troef_met_1__score_som_nul(self):
        som = 0
        for i in range(4):
            som += self.spelers_info_list._spelers_list[i]._punten
        self.assertEqual(0, som)


class spel_test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1(unittest.TestCase):
    def setUp(self):
        spel_info = cls.spel()
        spel_info._deler = 'Bram'
        spel_info._spelsoort = 'Grote Miserie'
        gezelschap_list = ['Bram', 'Frank', 'Lucy', 'Joke']
        spel_result = cls.spel_result(spel_info)
        spel_result._spelers_dict = {'Lucy': False}
        self.spelers_info_list = spl.create_spelers_info_list_in_spel_info(spel_info, gezelschap_list, spel_result)

        obj_1 = cls.speler_per_spel_info()
        obj_1._naam = 'Bram'
        obj_1._gespeeld = False
        obj_1._winst = True
        obj_1._punten = 6
        obj_2 = cls.speler_per_troef_info()
        obj_2._naam = 'Frank'
        obj_2._gespeeld = False
        obj_2._winst = True
        obj_2._punten = 6
        obj_3 = cls.speler_per_troef_info()
        obj_3._naam = 'Lucy'
        obj_3._gespeeld = True
        obj_3._winst = False
        obj_3._punten = -18
        obj_4 = cls.speler_per_troef_info()
        obj_4._naam = 'Joke'
        obj_4._gespeeld = False
        obj_4._winst = True
        obj_4._punten = 6
        spelers_obj_list = [obj_3, obj_1, obj_2, obj_4]
        result = spel_result
        result._spelers_list = spelers_obj_list
        return result

    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_1_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._naam, self.spelers_info_list._spelers_list[0]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_1_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._gespeeld, self.spelers_info_list._spelers_list[0]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_1_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._winst, self.spelers_info_list._spelers_list[0]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_1_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._punten, self.spelers_info_list._spelers_list[0]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_2_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._naam, self.spelers_info_list._spelers_list[1]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_2_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._gespeeld, self.spelers_info_list._spelers_list[1]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_2_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._winst, self.spelers_info_list._spelers_list[1]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__tGrote_Miserie_met_1__speler_2_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._punten, self.spelers_info_list._spelers_list[1]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_3_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._naam, self.spelers_info_list._spelers_list[2]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_3_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._gespeeld, self.spelers_info_list._spelers_list[2]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_3_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._winst, self.spelers_info_list._spelers_list[2]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_3_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._punten, self.spelers_info_list._spelers_list[2]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_4_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._naam, self.spelers_info_list._spelers_list[3]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_4_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._gespeeld, self.spelers_info_list._spelers_list[3]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_4_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._winst, self.spelers_info_list._spelers_list[3]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__speler_4_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._punten, self.spelers_info_list._spelers_list[3]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_1__score_som_nul(self):
        som = 0
        for i in range(4):
            som += self.spelers_info_list._spelers_list[i]._punten
        self.assertEqual(0, som)


class spel_test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2(unittest.TestCase):
    def setUp(self):
        spel_info = cls.spel()
        spel_info._deler = 'Bram'
        spel_info._spelsoort = 'Grote Miserie'
        gezelschap_list = ['Bram', 'Frank', 'Lucy', 'Joke']
        spel_result = cls.spel_result(spel_info)
        spel_result._spelers_dict = {'Lucy': False, 'Joke': True}
        self.spelers_info_list = spl.create_spelers_info_list_in_spel_info(spel_info, gezelschap_list, spel_result)

        obj_1 = cls.speler_per_spel_info()
        obj_1._naam = 'Bram'
        obj_1._gespeeld = False
        obj_1._winst = True
        obj_1._punten = 0
        obj_2 = cls.speler_per_troef_info()
        obj_2._naam = 'Frank'
        obj_2._gespeeld = False
        obj_2._winst = True
        obj_2._punten = 0
        obj_3 = cls.speler_per_troef_info()
        obj_3._naam = 'Lucy'
        obj_3._gespeeld = True
        obj_3._winst = False
        obj_3._punten = -24
        obj_4 = cls.speler_per_troef_info()
        obj_4._naam = 'Joke'
        obj_4._gespeeld = True
        obj_4._winst = True
        obj_4._punten = 24
        spelers_obj_list = [obj_4, obj_3, obj_1, obj_2]
        result = spel_result
        result._spelers_list = spelers_obj_list
        return result

    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_1_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._naam, self.spelers_info_list._spelers_list[0]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_1_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._gespeeld, self.spelers_info_list._spelers_list[0]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_1_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._winst, self.spelers_info_list._spelers_list[0]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_1_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[0]._punten, self.spelers_info_list._spelers_list[0]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_2_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._naam, self.spelers_info_list._spelers_list[1]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_2_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._gespeeld, self.spelers_info_list._spelers_list[1]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_2_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._winst, self.spelers_info_list._spelers_list[1]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__tGrote_Miserie_met_2__speler_2_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[1]._punten, self.spelers_info_list._spelers_list[1]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_3_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._naam, self.spelers_info_list._spelers_list[2]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_3_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._gespeeld, self.spelers_info_list._spelers_list[2]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_3_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._winst, self.spelers_info_list._spelers_list[2]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_3_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[2]._punten, self.spelers_info_list._spelers_list[2]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_4_naam(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._naam, self.spelers_info_list._spelers_list[3]._naam)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_4_gespeeld(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._gespeeld, self.spelers_info_list._spelers_list[3]._gespeeld)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_4_winst(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._winst, self.spelers_info_list._spelers_list[3]._winst)
    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__speler_4_punten(self):
        result = self.setUp()
        self.assertEqual(result._spelers_list[3]._punten, self.spelers_info_list._spelers_list[3]._punten)

    def test_create_spelers_info_list_in_spel_info__geval__Grote_Miserie_met_2__score_som_nul(self):
        som = 0
        for i in range(4):
            som += self.spelers_info_list._spelers_list[i]._punten
        self.assertEqual(0, som)





if __name__ == '__main__':
    unittest.main()
