# classes

class speler_per_spel_info():

    def __init__(self):
        self._naam = ''
        self._gespeeld = False
        self._winst = False
        self._punten = 0


class speler_per_dames_info(speler_per_spel_info):

    def __init__(self, *args, **kwargs):
        speler_per_spel_info.__init__(self)
        self._aantal_dames = 0


class speler_per_troef_info(speler_per_spel_info):

    def bepaal_winst(self, aantal_slagen, behaalde_slagen):
        if behaalde_slagen >= aantal_slagen and self._gespeeld == True:
            winst = True
        elif behaalde_slagen < aantal_slagen and self._gespeeld == False:
            winst = True
        else:
            winst = False
        return winst

    def bepaal_punten(self, aantal_spelers, aantal_slagen, behaalde_slagen):
        score = abs(behaalde_slagen-aantal_slagen)
        if aantal_spelers == 2:
            if self._winst == True:
                punten = 2+score
            else:
                punten = -(2+score)
        elif self._gespeeld == True:
            if self._winst == True:
                punten = 3*(2+score)
            else:
                punten = -3*(2+score)
        else:
            if self._winst == True:
                punten = 2+score
            else:
                punten = -(2+score)
        return punten










class spel():
    count = 0
    def __init__(self):
        spel.count += 1
        self._id = spel.count
        self._deler = ''
        self._spelsoort = ''
        self._troef = ''
        self._aantal_slagen = 0
        self._vrager = ''
        self._meegaander = ''



class spel_result():
    """
        spel_info = object spel waar alle info van het spel inzit
        spelers_list = lijst met objecten speler_per_spel_info
        spelers_dict = dict met naam speler (key) en boolean gewonnen of niet (value)
    """
    def __init__(self, spel, *args, **kwargs):
        self._spel_info = spel
        self._spelers_list = []
        self._spelers_dict = {}

class spel_result_dames():
    """
        spel_info = object spel waar alle info van het spel inzit
        spelers_list = lijst met objecten speler_per_spel_info
        dames_dict = dict met naam spelers (key) die gespeeld hebben en integer aantal dames deze speler gekregen heeft (value)
    """
    def __init__(self, spel, *args, **kwargs):
        self._spel_info = spel
        self._spelers_list = []
        self._dames_dict = {}

class spel_result_troef():
    """
        spel_info = object spel waar alle info van het spel inzit
        spelers_list = lijst met objecten speler_per_spel_info
        behaalde_slagen = integer aantal slagen die behaald zijn
    """
    def __init__(self, spel, *args, **kwargs):
        self._spel_info = spel
        self._spelers_list = []
        self._behaalde_slagen = 0


class avond_info():
    """
        spel_list = lijst met objecten spel_result
    """
    def __init__(self, datum, gezelschap_list):
        self._datum = datum
        self._gezelschap_list = gezelschap_list
        self._spel_list = []