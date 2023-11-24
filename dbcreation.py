import sqlalchemy as db
from config_ import engine
from Helper.GeneralHelper import create_pwd
from Helper.DDLGenerator import create_ddl
from Helper.DbHelper import DbHelper
import random

db_ = DbHelper(engine)

# print(test.select("record", ["*"], "where artist = 'Leichenzug'"))

# ---- testing stuff ------------
# create db if needed


if True:
    create_ddl()
    genres = ["Rock", "Pop", "Metal", "Black Metal", "Death Metal"]
    sub_genres = ["DBM", "Raw", "Folk", "Symphonischer Black Metal", "Ambient Black Metal"]
    bands = [{"title": "Exitus Letalis", "artist": "Nyktalgia"},
             {"title": "Lunar Poetry", "artist": "Nokturnal Mortum"},
             {"title": "Aaskereia", "artist": "Zwischen den Welten"},
             {"title": "Abyssic Hate", "artist": "Suicidal Emotions"},
             {"title": "Arckanum", "artist": "Kampen"},
             {"title": "Behexen", "artist": "Rituale Satanum"},
             {"title": "Black Messiah", "artist": "Oath of a warrior"},
             {"title": "Coldworld", "artist": "Melancholie"},
             {"title": "Enthroned", "artist": "Xes Haereticum"},
             {"title": "Fiddlers Green", "artist": "On and On"},
             {"title": "Lyrinx", "artist": "Nihilistic Purity"},
             {"title": "Life is Pain", "artist": "Bloody Melancholy"},
             {"title": "Lifelover", "artist": "Konkurs"},
             {"title": "Lifelover", "artist": "Pulver"},
             {"title": "Mgla", "artist": "Groza"},
             {"title": "Manegarm", "artist": "Dodsfard"},
             {"title": "Minas Morgul", "artist": "Todesschwadron Ost"},
             {"title": "Nachtfalke", "artist": "Hail Victory Teutonia"},
             {"title": "Nagelfar", "artist": "Virus West"},
             {"title": "Magelfar", "artist": "Hühnengrab im Herbst"},
             {"title": "Nokturnal Mortum", "artist": "Goat Horns"},
             {"title": "Opeth", "artist": "Blackwater Park"},
             {"title": "Forgotten Tomb", "artist": "Springtime Depression"},
             {"title": "Darkthrone", "artist": "Transilvanian Hunger"},
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

