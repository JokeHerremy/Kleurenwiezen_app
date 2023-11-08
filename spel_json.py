



def speler_json_file_str(spelsoort, speler, gespeeld, winst, punten, aantal_dames=0):
    if spelsoort == 'Dames':
        speler_json = '{"naam": "'+speler+'", "gespeeld": "'+str(gespeeld)+'", "gewonnen": {"winst": "'+str(winst)+'", "punten": '+str(punten)+', "aantal dames": '+str(aantal_dames)+'}}'
    else:
        speler_json = '{"naam": "'+speler+'", "gespeeld": "'+str(gespeeld)+'", "gewonnen": {"winst": "'+str(winst)+'", "punten": '+str(punten)+'}}'
    return speler_json



def spelsoort_json_file_str(spelers, spelsoort, deler, troef='', aantal_slagen=0, behaalde_slagen=0):
    if spelsoort == 'Troef' or spelsoort == 'Troel':
        spelsoort_json = ' "spelsoort": {"soort": {"soort": "'+spelsoort+'", "troef": "'+troef+'", "aantal slagen": "'+str(aantal_slagen)+'", "behaalde slagen": "'+str(behaalde_slagen)+'"}, "spelers": ['+spelers+'], "deler": "'+deler+'"}'
    else: 
        spelsoort_json = ' "spelsoort": {"soort": {"soort": "'+spelsoort+'"}, "spelers": ['+spelers+'], "deler": "'+deler+'"}'
    return spelsoort_json



def gezelschap_json_file_str(gezelschap_list):
    gezelschap_json = ''
    for speler in gezelschap_list:
        speler_json = '{"naam": "'+speler+'"}'
        if gezelschap_list.index(speler) < (len(gezelschap_list)-1):
            gezelschap_json = gezelschap_json+speler_json+', '
        else:
            gezelschap_json = gezelschap_json+speler_json
    gezelschap_json =  ' "gezelschap": {"spelers": ['+gezelschap_json+']} '
    return gezelschap_json



def create_json_file_spel(spelers_per_spel_list, spel_info, spel_result):

    spelers_json_str = ''

    for speler in spelers_per_spel_list:
        if spel_info._spelsoort == 'Dames':
            speler_json_str = speler_json_file_str(spel_info._spelsoort, speler._naam, speler._gespeeld, speler._winst, speler._punten, speler._aantal_dames)
        else:
            speler_json_str = speler_json_file_str(spel_info._spelsoort, speler._naam, speler._gespeeld, speler._winst, speler._punten)
        if spelers_per_spel_list.index(speler) < (len(spelers_per_spel_list)-1):
            spelers_json_str = spelers_json_str+speler_json_str+', '
        else:
            spelers_json_str = spelers_json_str + speler_json_str
    if spel_info._spelsoort == 'Troef' or spel_info._spelsoort == 'Troel':
        spelsoort_json_str = spelsoort_json_file_str(spelers_json_str, spel_info._spelsoort, spel_info._deler, spel_info._troef, spel_info._aantal_slagen, spel_result._behaalde_slagen)
    else:    
        spelsoort_json_str = spelsoort_json_file_str(spelers_json_str, spel_info._spelsoort, spel_info._deler)

    spel_json = '{ "id":"'+str(spel_info._id)+'", '+spelsoort_json_str+'}'
    return spel_json



def create_json_file_avond(datum, gezelschap_list, json_spellen_list):
    
    spellen_json = ''

    for spel in json_spellen_list:
        if json_spellen_list.index(spel) < (len(json_spellen_list)-1):
            spellen_json = spellen_json+spel+', '
        else:
            spellen_json = spellen_json+spel
    gezelschap_json = gezelschap_json_file_str(gezelschap_list)
    avond_json = '{ "datum":"'+datum+'", "spel": "kleurenwiezen", '+gezelschap_json+', "spellen": ['+spellen_json+']}'

    return avond_json