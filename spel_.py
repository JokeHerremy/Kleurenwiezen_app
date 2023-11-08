# variabelen
dict_punten = {
    "Kleine Miserie": {
        4: {
            0: [0, 0, 0, 0],
            1: [30, -10, -10, -10],
            2: [20, 20, -20, -20],
            3: [10, 10, 10, -30],
            4: [0, 0, 0, 0]
        },
        3: {
            0: [-5, -5, -5, 15],
            1: [25, -15, -15, 5],
            2: [15, 15, -25, -5],
            3: [5, 5, 5, -15]
        },
        2: {
            0: [-10, -10, 10, 10],
            1: [20, -20, 0, 0],
            2: [10, 10, -10, -10]
        },
        1: {
            0: [-15, 5, 5, 5],
            1: [15, -5, -5, -5]
        }
    },
    "Picon": {
        4: {
            0: [0, 0, 0, 0],
            1: [30, -10, -10, -10],
            2: [20, 20, -20, -20],
            3: [10, 10, 10, -30],
            4: [0, 0, 0, 0]
        },
        3: {
            0: [-5, -5, -5, 15],
            1: [25, -15, -15, 5],
            2: [15, 15, -25, -5],
            3: [5, 5, 5, -15]
        },
        2: {
            0: [-10, -10, 10, 10],
            1: [20, -20, 0, 0],
            2: [10, 10, -10, -10]
        },
        1: {
            0: [-15, 5, 5, 5],
            1: [15, -5, -5, -5]
        }
    },
    "Grote Miserie": {
        4: {
            0: [0, 0, 0, 0],
            1: [36, -12, -12, -12],
            2: [24, 24, -24, -24],
            3: [12, 12, 12, -36],
            4: [0, 0, 0, 0]
        },
        3: {
            0: [-6, -6, -6, 18],
            1: [30, -18, -18, 6],
            2: [18, 18, -30, -6],
            3: [6, 6, 6, -18]
        },
        2: {
            0: [-12, -12, 12, 12],
            1: [24, -24, 0, 0],
            2: [12, 12, -12, -12]
        },
        1: {
            0: [-18, 6, 6, 6],
            1: [18, -6, -6, -6]
        }
    },
    "Abondance": {
        4: {
            0: [0, 0, 0, 0],
            1: [36, -12, -12, -12],
            2: [24, 24, -24, -24],
            3: [12, 12, 12, -36],
            4: [0, 0, 0, 0]
        },
        3: {
            0: [-6, -6, -6, 18],
            1: [30, -18, -18, 6],
            2: [18, 18, -30, -6],
            3: [6, 6, 6, -18]
        },
        2: {
            0: [-12, -12, 12, 12],
            1: [24, -24, 0, 0],
            2: [12, 12, -12, -12]
        },
        1: {
            0: [-18, 6, 6, 6],
            1: [18, -6, -6, -6]
        }
    },
    "Blote Miserie": {
        4: {
            0: [0, 0, 0, 0],
            1: [72, -24, -24, -24],
            2: [48, 48, -48, -48],
            3: [24, 24, 24, -72],
            4: [0, 0, 0, 0]
        },
        3: {
            0: [-12, -12, -12, 36],
            1: [60, -36, -36, 12],
            2: [36, 36, -60, -12],
            3: [12, 12, 12, -36]
        },
        2: {
            0: [-24, -24, 24, 24],
            1: [48, -48, 0, 0],
            2: [24, 24, -24, -24]
        },
        1: {
            0: [-36, 12, 12, 12],
            1: [36, -12, -12, -12]
        }
    },
    "Soloslim": {
        4: {
            0: [0, 0, 0, 0],
            1: [144, -48, -48, -48],
            2: [96, 96, -96, -96],
            3: [48, 48, 48, -144],
            4: [0, 0, 0, 0]
        },
        3: {
            0: [-24, -24, -24, 72],
            1: [120, -72, -72, 24],
            2: [72, 72, -120, -24],
            3: [24, 24, 24, -72]
        },
        2: {
            0: [-48, -48, 48, 48],
            1: [96, -96, 0, 0],
            2: [48, 48, -48, -48]
        },
        1: {
            0: [-72, 24, 24, 24],
            1: [72, -24, -24, -24]
        }
    },
    "Dames": {
        4: {
            0: [0, 0, 0, 0],
            1: {
                2: [8, -4, -2, -2]
            },
            2: {
                3: [4, 4, -6, -2],
                2: [4, 4, -4, -4]
            },
            3: [3, 3, 3, -9]
        }
    }
}



import spel_classes as cls














def create_avond_info(datum, gezelschap_list, spellen_obj_list):
    avond_info = cls.avond_info(datum, gezelschap_list)
    avond_info._spel_list = spellen_obj_list
    return avond_info


def create_spel_info(spel_deler, spel_spelsoort, spel_troef='', spel_aantal_slagen=0, spel_vrager='', spel_meegaander=''):
    spel_info = cls.spel()

    spel_info._deler = spel_deler
    spel_info._spelsoort = spel_spelsoort
    if spel_spelsoort == 'Troef' or spel_spelsoort == 'Troel':
        spel_info._troef = spel_troef
        spel_info._aantal_slagen = spel_aantal_slagen    
        spel_info._vrager = spel_vrager
        spel_info._meegaander = spel_meegaander  

    return spel_info


########
def create_spelers_info_list_in_spel_info(spel_info, gezelschap_list, spel_result):
    """
        spel_info = object van klasse spel_info
        gezelschap_list = list met namen van spelers
        spel_result = object van klasse spel result
    """

    if spel_info._spelsoort == 'Troef' or spel_info._spelsoort == 'Troel':

        behaalde_slagen = spel_result._behaalde_slagen
        speler_per_troef_list = []
        if spel_info._meegaander != '':
            spelers = [spel_info._vrager, spel_info._meegaander]
        else:
            spelers = [spel_info._vrager]

        for nummer in range(0, len(spelers)):
            speler = cls.speler_per_troef_info()
            speler._naam = spelers[nummer]
            speler._gespeeld = True
            winst = speler.bepaal_winst(spel_info._aantal_slagen, behaalde_slagen)
            speler._winst = winst
            punten = speler.bepaal_punten(len(spelers), spel_info._aantal_slagen, behaalde_slagen)
            speler._punten = punten
            speler_per_troef_list.append(speler)

        for naam in gezelschap_list:
            if not any(speler._naam == naam for speler in speler_per_troef_list):
                speler = cls.speler_per_troef_info()
                speler._naam = naam
                speler._gespeeld = False
                winst = speler.bepaal_winst(spel_info._aantal_slagen, behaalde_slagen)
                speler._winst = winst
                punten = speler.bepaal_punten(len(spelers), spel_info._aantal_slagen, behaalde_slagen)
                speler._punten = punten
                speler_per_troef_list.append(speler)

        spel_result._spelers_info = speler_per_troef_list
        return spel_result

    elif spel_info._spelsoort == 'Dames':
        
        speler_per_dames_list = []
        aantal_winst = 0
        aantal_spelers = 4
        counter = 0
        dict_dames_key = 2
        dames_dict = spel_result._dames_dict

        for naam in gezelschap_list:
            speler = cls.speler_per_dames_info()
            speler._naam = naam
            speler._gespeeld = True
            speler._aantal_dames = dames_dict[naam]
            speler_per_dames_list.append(speler)
            speler_per_dames_list.sort(key=lambda speler: speler._aantal_dames, reverse=True)

        for speler in speler_per_dames_list:
            if speler._aantal_dames == 0:
                speler._winst = True
                aantal_winst += 1
                speler_per_dames_list.remove(speler)
                speler_per_dames_list.insert(0, speler)
            elif speler._aantal_dames == 3:
                speler._winst= False
                dict_dames_key = 3
            else:
                speler._winst = False

        if aantal_winst != 2 and aantal_winst != 1:
            punten_list = dict_punten[spel_info._spelsoort][aantal_spelers][aantal_winst]
        else:
            punten_list = dict_punten[spel_info._spelsoort][aantal_spelers][aantal_winst][dict_dames_key]
        for speler in speler_per_dames_list:
            speler._punten = punten_list[counter]
            counter += 1

        spel_result._spelers_list = speler_per_dames_list
        return spel_result

    else:

        speler_per_spel_list = []
        aantal_winst = 0
        counter = 0
        spelers_dict = spel_result._spelers_dict
        keys_spelers = list(spelers_dict)

        for nummer in range(0, len(spelers_dict)):
            speler = cls.speler_per_spel_info()
            speler._naam = keys_spelers[nummer]
            speler._gespeeld = True
            speler._winst = spelers_dict[keys_spelers[nummer]]
            if speler._winst == True:
                speler_per_spel_list.insert(0, speler)
                aantal_winst += 1
            else:
                speler_per_spel_list.append(speler)

        for naam in gezelschap_list:
            if not any(speler._naam == naam for speler in speler_per_spel_list):
                speler = cls.speler_per_spel_info()
                speler._naam = naam
                speler._gespeeld = False
                speler_per_spel_list.append(speler)

        punten_list = dict_punten[spel_info._spelsoort][len(spelers_dict)][aantal_winst]
        for speler in speler_per_spel_list:
            speler._punten = punten_list[counter]
            if not getattr(speler, '_winst'):
                if speler._punten > 0:
                    speler._winst = True
                elif speler._punten < 0:
                    speler._winst = False
            counter += 1

        spel_result._spelers_info = speler_per_spel_list
        return spel_result


