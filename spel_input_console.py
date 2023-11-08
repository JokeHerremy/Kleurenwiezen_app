import inquirer as inq




def vraag_spel_deler(gezelschap_list):
    question_deler = [
        inq.List('deler',
            message="Wie is de deler?",
            choices=gezelschap_list,
            ),
    ]
    answer_deler = inq.prompt(question_deler)
    deler_input = str(answer_deler['deler'])
    return deler_input


def vraag_spel_spelsoort(spelsoorten_list):
    question_spelsoort = [
        inq.List('spelsoort',
            message='welk spel wordt er gespeeld?',
            choices=spelsoorten_list
            ),
    ]
    answer_spelsoort = inq.prompt(question_spelsoort)
    spelsoort_input = str(answer_spelsoort['spelsoort'])
    return spelsoort_input


def vraag_speler_gespeeld(gezelschap_list):
    question_gespeeld = [
        inq.List('gespeeld',
            message="Welke speler heeft gespeeld?",
            choices=gezelschap_list,
            ),
    ]
    answer_gespeeld = inq.prompt(question_gespeeld)
    gespeeld = str(answer_gespeeld['gespeeld'])
    return gespeeld

def vraag_speler_gewonnen(speler):
    question_gewonnen = [
        inq.List('gewonnen',
            message="Heeft "+speler+" gewonnen?",
            choices=[True, False],
            ),
    ]
    answer_gewonnen = inq.prompt(question_gewonnen)
    gewonnen = bool(answer_gewonnen['gewonnen'])
    return gewonnen

def vraag_aantal_spelers():
    print('Hoeveel spelers spelen er?')
    aantal = input()
    aantal = int(aantal)
    return aantal


def vraag_speler_aantal_dames(speler):
    print('Hoeveel dames heeft '+speler+' gekregen?')
    dames = input()
    dames = int(dames)
    return dames

def vraag_aantal_slagen():
    print('Voor hoeveel slagen is er gespeeld?')
    slagen = input()
    slagen = int(slagen)
    return slagen

def vraag_behaalde_slagen():
    print('Hoeveel slagen zijn er behaald?')
    behaalde_slagen = input()
    behaalde_slagen = int(behaalde_slagen)
    return behaalde_slagen

def vraag_troef():
    question_troef = [
        inq.List('troef',
            message="Wat was troef?",
            choices=['Hartes', 'Koekes', 'Klavers', 'Pèques'],
            ),
    ]
    answer_troef = inq.prompt(question_troef)
    troef = str(answer_troef['troef'])
    return troef

def vraag_spel_vrager(gezelschap_list):
    question_vrager = [
        inq.List('vrager',
            message="Wie is de vrager?",
            choices=gezelschap_list,
            ),
    ]
    answer_vrager = inq.prompt(question_vrager)
    vrager = str(answer_vrager['vrager'])
    return vrager

def vraag_spel_meegaander(gezelschap_list):
    question_meegaander = [
        inq.List('meegaander',
            message="Wie is de meegaander?",
            choices=gezelschap_list,
            ),
    ]
    answer_meegaander = inq.prompt(question_meegaander)
    meegaander = str(answer_meegaander['meegaander'])
    return meegaander

def vraag_avond_datum():
    print('Wat is de datum?')
    datum = input()
    datum = str(datum)
    return datum

def vraag_avond_gezelschap():
    spelers = []
    for num in range(1,5):
        print('wat is de naam van speler '+str(num)+'?')
        speler = input()
        spelers.append(speler)
    return spelers

def vraag_nieuw_spel():
    question_nieuw_spel = [
        inq.List('spel',
            message="Nog een spel toevoegen?",
            choices=[True, False],
            ),
    ]
    answer_nieuw_spel = inq.prompt(question_nieuw_spel)
    nieuw_spel = bool(answer_nieuw_spel['spel'])
    return nieuw_spel