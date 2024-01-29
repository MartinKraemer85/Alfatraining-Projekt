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

# Complete example
# with app.app_context():
#     db_helper = DbHelper(db)
#     db_helper.insert({"objectPath": "Model.Vinyl.Record.Record",
#                          "attributes":
#                              {"title": "Band ohne Namen",
#                               "artist": "Band ohne Namen",
#                               "type": "Vinyl",
#                               "year": 2010,
#                               "state": 5,
#                               "price": 5,
#                               "Model.Vinyl.Track.Track": [
#                                   {"track_number": 1, "title": "track1", "length": "5:23"},
#                                   {"track_number": 2, "title": "track2", "length": "5:23"},
#                                   {"track_number": 3, "title": "track3", "length": "5:23"},
#                               ], "Model.Vinyl.Associations.AscGenre": [
#                                  {"genre_id": 5}
#                              ], "Model.Vinyl.Associations.AscSubGenre": [
#                                  {"sub_genre_id": 5}
#                              ]}
#                          })

if True:
    with app.app_context():
        engine = db.create_engine(f"mssql://@{config('SERVER')}/{config('DATABASE')}?driver={config('ODBC')}")
        create_ddl(engine)
        db_ = DbHelper(db)
        # genres = ["Rock", "Pop", "Metal", "Black Metal", "Death Metal"]
        # sub_genres = ["DBM", "Indie", "Folk", "Electro", "Ambient Black Metal"]
        # bands = [{"artist": "Nyktalgia", "title": "Exitus Letalis"},
        #          {"artist": "Nokturnal Mortum", "title": "Lunar Poetry"},
        #          {"artist": "Aaskereia", "title": "Zwischen den Welten"},
        #          {"artist": "Abyssic Hate", "title": "Suicidal Emotions"},
        #          {"artist": "Arckanum", "title": "Kampen"},
        #          {"artist": "Behexen", "title": "Rituale Satanum"},
        #          {"artist": "Black Messiah", "title": "Oath of a warrior"},
        #          {"artist": "Coldworld", "title": "Melancholie"},
        #          {"artist": "Enthroned", "title": "Xes Haereticum"},
        #          {"artist": "Fiddlers Green", "title": "On and On"},
        #          {"artist": "Lyrinx", "title": "Nihilistic Purity"},
        #          {"artist": "Life is Pain", "title": "Bloody Melancholy"},
        #          {"artist": "Lifelover", "title": "Konkurs"},
        #          {"artist": "Lifelover", "title": "Pulver"},
        #          {"artist": "Mgla", "title": "Groza"},
        #          {"artist": "Manegarm", "title": "Dodsfard"},
        #          {"artist": "Minas Morgul", "title": "Todesschwadron Ost"},
        #          {"artist": "Nachtfalke", "title": "Hail Victory Teutonia"},
        #          {"artist": "Nagelfar", "title": "Virus West"},
        #          {"artist": "Magelfar", "title": "Hühnengrab im Herbst"},
        #          {"artist": "Nokturnal Mortum", "title": "Goat Horns"},
        #          {"artist": "Opeth", "title": "Blackwater Park"},
        #          {"artist": "Forgotten Tomb", "title": "Springtime Depression"},
        #          {"artist": "Darkthrone", "title": "Transilvanian Hunger"},
        #          ]
        #
        # for genre in genres:
        #     db_.insert({"objectPath": "Model.Vinyl.Genre.Genre",
        #                 "attributes": {"name": genre},
        #                 })
        #
        # for genre in sub_genres:
        #     db_.insert({"objectPath": "Model.Vinyl.Genre.SubGenre",
        #                 "attributes": {"name": genre},
        #                 })
        #
        # for band in bands:
        #     db_.insert({"objectPath": "Model.Vinyl.Record.Record",
        #                 "attributes":
        #                     {"title": band.get("title"),
        #                      "artist": band.get("artist"),
        #                      "type": "Vinyl",
        #                      "year": random.randint(1990, 2010),
        #                      "state": random.randint(1, 5),
        #                      "price": random.randint(10, 30),
        #                      "Model.Vinyl.Track.Track": [
        #                          {"track_number": 1, "title": "græmelse ok væ", "length": "5:26"},
        #                          {"track_number": 2, "title": "Lunar Poetry", "length": "2:20"},
        #                          {"track_number": 3, "title": "Perun's Celestial Silver", "length": "0:42"},
        #                          {"track_number": 4, "title": "Carpathian Mysteries", "length": "4:59"},
        #                          {"track_number": 5, "title": "Ancient Nation", "length": "3:32"},
        #                      ], "Model.Vinyl.Associations.AscGenre": [
        #                         {"genre_id": random.randint(1, 5)},
        #                     ], "Model.Vinyl.Associations.AscSubGenre": [
        #                         {"sub_genre_id": random.randint(1, 5)},
        #                     ]},
        #                 })

        # test address
        db_.insert({
            "objectPath": "Model.AddressDetails.Country.Country",
            "attributes": {"country_name": "Deutschland",
                           "country_initials": "DE",
                           "Model.AddressDetails.State.State": [
                               {"state_name": "Baden-Württemberg", "state_initials": "BW"},
                               {"state_name": "Bayern", "state_initials": "BY"},
                               {"state_name": "Berlin", "state_initials": "BE"},
                               {"state_name": "Brandenburg", "state_initials": "BB"},
                               {"state_name": "Bremen ", "state_initials": "HB"},
                               {"state_name": "Hamburg", "state_initials": "HH"},
                               {"state_name": "Hessen", "state_initials": "HE"},
                               {
                                   "state_name": "Mecklenburg-Vorpommern", "state_initials": "MV",
                                   "Model.AddressDetails.City.City": [
                                       {"name": "Schwerin"},
                                       {"name": "Greifswald"},
                                       {"name": "Wismar"},
                                       {"name": "Rostock",
                                        "Model.AddressDetails.District.District": [
                                            {"name": "Reutershagen", "zip_code": "18069"},
                                            {"name": "Ktv", "zip_code": "18057",
                                             "Model.AddressDetails.Street.Street": [
                                                 {"name": "Friedrichstraße", "number": 39},
                                                 {"name": "Händelstraße", "number": 7},
                                                 {"name": "Wismarsche Straße", "number": 12},
                                                 {"name": "Götheplatz", "number": 10},
                                             ]},
                                            {"name": "Warnemünde", "zip_code": "18119"},
                                        ]},
                                   ],
                               },

                               # {"state_name": "Niedersachsen", "state_initials": "NI"},
                               # {"state_name": "Nordrhein-Westfalen", "state_initials": "NW"},
                               # {"state_name": "Rheinland-Pfalz", "state_initials": "BE"},
                               # {"state_name": "Berlin", "state_initials": "RP"},
                               # {"state_name": "Saarland", "state_initials": "SL"},
                               # {"state_name": "Sachsen", "state_initials": "SN"},
                               # {"state_name": "Sachsen-Anhalt", "state_initials": "ST"},
                               # {"state_name": "Schleswig-Holstein", "state_initials": "SH"},
                               # {"state_name": "Thüringen", "state_initials": "TH"},

                           ],
                           }
        })
