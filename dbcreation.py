from Helper.GeneralHelper import create_pwd
from Helper.DDLGenerator import create_ddl
from decouple import config
from Helper.DbHelper import DbHelper
from settings import db, app

import random

# print(test.select("record", ["*"], "where artist = 'Leichenzug'"))

# ---- testing stuff ------------
# create db if needed
# with app.app_context():
#     db_helper = DbHelper(db)
#     test = db_helper.select_all_where(object_path="Model.Vinyl.Record.Record",
#                                       where="genre_1.name = 'Black Metal'",
#                                       initial=True)
#     print(test)

if False:
    engine = db.create_engine(f"mssql://@{config('SERVER')}/{config('DATABASE')}?driver={config('ODBC')}")
    create_ddl(engine)

with app.app_context():
    db_helper = DbHelper(db)
    db_helper.db_insert({"objectPath": "Model.CustomerDetails.Customer.Customer",
                         "attributes": {"username": "test",
                                        "pwd": "miau",
                                        "first_name": "miau",
                                        "last_name": "schnarr",
                                        "mail": "mail@bla.de"},
                         })

if False:

    genres = ["Rock", "Pop", "Metal", "Black Metal", "Death Metal"]
    sub_genres = ["DBM", "Raw", "Folk", "Symphonischer Black Metal", "Ambient Black Metal"]
    bands = [{"artist": "Nyktalgia", "title": "Exitus Letalis"},
             {"artist": "Nokturnal Mortum", "title": "Lunar Poetry"},
             {"artist": "Aaskereia", "title": "Zwischen den Welten"},
             {"artist": "Abyssic Hate", "title": "Suicidal Emotions"},
             {"artist": "Arckanum", "title": "Kampen"},
             {"artist": "Behexen", "title": "Rituale Satanum"},
             {"artist": "Black Messiah", "title": "Oath of a warrior"},
             {"artist": "Coldworld", "title": "Melancholie"},
             {"artist": "Enthroned", "title": "Xes Haereticum"},
             {"artist": "Fiddlers Green", "title": "On and On"},
             {"artist": "Lyrinx", "title": "Nihilistic Purity"},
             {"artist": "Life is Pain", "title": "Bloody Melancholy"},
             {"artist": "Lifelover", "title": "Konkurs"},
             {"artist": "Lifelover", "title": "Pulver"},
             {"artist": "Mgla", "title": "Groza"},
             {"artist": "Manegarm", "title": "Dodsfard"},
             {"artist": "Minas Morgul", "title": "Todesschwadron Ost"},
             {"artist": "Nachtfalke", "title": "Hail Victory Teutonia"},
             {"artist": "Nagelfar", "title": "Virus West"},
             {"artist": "Magelfar", "title": "Hühnengrab im Herbst"},
             {"artist": "Nokturnal Mortum", "title": "Goat Horns"},
             {"artist": "Opeth", "title": "Blackwater Park"},
             {"artist": "Forgotten Tomb", "title": "Springtime Depression"},
             {"artist": "Darkthrone", "title": "Transilvanian Hunger"},
             ]
    for genre in genres:
        db_.db_insert({"objectPath": "Model.Vinyl.Genre.Genre",
                       "attributes": {"name": genre},
                       })

    for genre in sub_genres:
        db_.db_insert({"objectPath": "Model.Vinyl.Genre.SubGenre",
                       "attributes": {"name": genre},
                       })

    for band in bands:
        db_.db_insert({"objectPath": "Model.Vinyl.Record.Record",
                       "attributes":
                           {"title": band.get("title"),
                            "artist": band.get("artist"),
                            "type": "Vinyl",
                            "year": random.randint(1990, 2010),
                            "state": random.randint(1, 5),
                            "price": random.randint(10, 30),
                            "Model.Vinyl.Track.Track": [
                                {"track_number": 1, "title": "track1", "length": "5:23"},
                                {"track_number": 2, "title": "track2", "length": "5:23"},
                                {"track_number": 3, "title": "track3", "length": "5:23"},
                            ], "Model.Vinyl.Associations.AscGenre": [
                               {"genre_id": random.randint(1, 5)},
                           ], "Model.Vinyl.Associations.AscSubGenre": [
                               {"sub_genre_id": random.randint(1, 5)},
                           ]},
                       })
