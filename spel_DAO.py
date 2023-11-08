
import pymongo as pym
import json 



def spel_naar_mongodb(json_spel):
    json_spel = json.loads(json_spel)
    # making a connection to mongo client
    client = pym.MongoClient('mongodb://127.0.0.1:27017/')

    # create a database if not exists:
    db = client["Kleurenwiezen"]
    # create a collection
    table = db["Kleurenwiezen_avonden"]
    db.Kleurenwiezen_spellen.insert_one(json_spel)