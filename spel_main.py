import pymongo as pym
import spel_classes as cls
import spel_input_console as inp
import spel_ as spl
import spel_json as jsn
import spel_DAO as dao

spelsoorten_list = ['Troef', 'Dames', 'Troel', 'Kleine Miserie', 'Grote Miserie', 'Blote Miserie', 'Picon', 'Abondance', 'Soloslim']





avond_datum = inp.vraag_avond_datum()
gezelschap_list = inp.vraag_avond_gezelschap()
nieuw_spel = True
spellen_json_list = []
spellen_obj_list = []


while nieuw_spel == True:

    spel = cls.spel()
    spel._deler = inp.vraag_spel_deler(gezelschap_list)
    spelsoort = inp.vraag_spel_spelsoort(spelsoorten_list)
    spel._spelsoort = spelsoort

    if spelsoort == 'Troef' or spelsoort == 'Troel':
        spel._troef = inp.vraag_troef()
        aantal_spelers = inp.vraag_aantal_spelers()
        spel._vrager = inp.vraag_spel_vrager(gezelschap_list)
        if aantal_spelers == 2:
            spel._meegaander = inp.vraag_spel_meegaander(gezelschap_list)
        spel._aantal_slagen = inp.vraag_aantal_slagen()
        spel_result = cls.spel_result_troef(spel)
        spel_result._behaalde_slagen = inp.vraag_behaalde_slagen()

    elif spelsoort == 'Dames':
        dames_dict = {}
        for speler in gezelschap_list:
            dames_dict[speler] = inp.vraag_speler_aantal_dames(speler)
        spel_result = cls.spel_result_dames(spel)
        spel_result._dames_dict = dames_dict

    else:
        spelers_dict = {}
        spelers_list = []
        aantal_spelers = inp.vraag_aantal_spelers()
        for nummer in range(0, aantal_spelers):
            speler = inp.vraag_speler_gespeeld(gezelschap_list)
            spelers_list.append(speler)
        for speler in spelers_list:
            spelers_dict[speler] = inp.vraag_speler_gewonnen(speler)
        spel_result = cls.spel_result(spel)
        spel_result._spelers_dict = spelers_dict

    spel_result = spl.create_spelers_info_list_in_spel_info(spel, gezelschap_list, spel_result)
    spel_json_file = jsn.create_json_file_spel(spel_result._spelers_info, spel, spel_result)

    spellen_json_list.append(spel_json_file)
    spellen_obj_list.append(spel_result)
    nieuw_spel = inp.vraag_nieuw_spel()

avond_info = spl.create_avond_info(avond_datum, gezelschap_list, spellen_obj_list)
avond_json = jsn.create_json_file_avond(avond_datum, gezelschap_list, spellen_json_list)
dao.spel_naar_mongodb(avond_json)