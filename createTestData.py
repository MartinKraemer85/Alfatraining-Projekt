from Helper.GeneralHelper import create_pwd
from Helper.DDLGenerator import create_ddl
from decouple import config
from Helper.DbHelper import DbHelper
from settings import db, app
import random

with app.app_context():
    engine = db.create_engine(f"mssql://@{config('SERVER')}/{config('DATABASE')}?driver={config('ODBC')}")
    create_ddl(engine)
    db_ = DbHelper(db)

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
                                         "Model.AddressDetails.Address.Address": [
                                             {"name": "Friedrichstraße", "number": 39},
                                             {"name": "Händelstraße", "number": 7},
                                             {"name": "Wismarsche Straße", "number": 12},
                                             {"name": "Götheplatz", "number": 10},
                                         ]},
                                        {"name": "Warnemünde", "zip_code": "18119"},
                                    ]},
                               ],
                           },
                           {"state_name": "Niedersachsen", "state_initials": "NI"},
                           {"state_name": "Nordrhein-Westfalen", "state_initials": "NW"},
                           {"state_name": "Rheinland-Pfalz", "state_initials": "BE"},
                           {"state_name": "Berlin", "state_initials": "RP"},
                           {"state_name": "Saarland", "state_initials": "SL"},
                           {"state_name": "Sachsen", "state_initials": "SN"},
                           {"state_name": "Sachsen-Anhalt", "state_initials": "ST"},
                           {"state_name": "Schleswig-Holstein", "state_initials": "SH"},
                           {"state_name": "Thüringen", "state_initials": "TH"},

                       ],
                       }
    })

    # test article
    genres = ["Rock", "Pop", "Metal", "Black Metal", "Death Metal"]
    sub_genres = ["DBM", "Indie", "Folk", "Electro", "Ambient Black Metal"]
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

    sellers = [
        {"username": "Bertram", "pwd": "****", "first_name": "Bert", "last_name": "tram", "mail": "m.kraemer85@web.de", "address": random.randint(1, 4)},
        {"username": "Hans", "pwd": "****", "first_name": "Hans", "last_name": "Wurst", "mail": "m.kraemer85@web.de", "address": random.randint(1, 4)},
        {"username": "Peter", "pwd": "****", "first_name": "Pet", "last_name": "er", "mail": "m.kraemer85@web.de", "address": random.randint(1, 4)},
        {"username": "Klaus", "pwd": "****", "first_name": "Karl", "last_name": "Karlsen", "mail": "m.kraemer85@web.de", "address": random.randint(1, 4)},
        {"username": "User123", "pwd": "****", "first_name": "Homer", "last_name": "Simpson", "mail": "m.kraemer85@web.de", "address": random.randint(1, 4)},
        {"username": "Momo", "pwd": "****", "first_name": "Momo", "last_name": "Das Meerschweinchen", "mail": "m.kraemer85@web.de", "address": random.randint(1, 4)},
        {"username": "Bocchi", "pwd": "****", "first_name": "Bocchi", "last_name": "Das Meerschweinchen", "mail": "m.kraemer85@web.de", "address": random.randint(1, 4)},
    ]

    for seller in sellers:
        db_.insert({"objectPath": "Model.SellerDetails.Seller.Seller",
                    "attributes": seller
                    })

    for genre in genres:
        db_.insert({"objectPath": "Model.Vinyl.Genre.Genre",
                    "attributes": {"name": genre},
                    })

    for genre in sub_genres:
        db_.insert({"objectPath": "Model.Vinyl.Genre.SubGenre",
                    "attributes": {"name": genre},
                    })

    for band in bands:
        db_.insert({"objectPath": "Model.Vinyl.Record.Record",
                    "attributes":
                        {"title": band.get("title"),
                         "artist": band.get("artist"),
                         "type": "Vinyl",
                         "year": random.randint(1990, 2010),
                         "Model.Vinyl.Track.Track": [
                             {"track_number": 1, "title": "græmelse ok væ", "length": "5:26"},
                             {"track_number": 2, "title": "Lunar Poetry", "length": "2:20"},
                             {"track_number": 3, "title": "Perun's Celestial Silver", "length": "0:42"},
                             {"track_number": 4, "title": "Carpathian Mysteries", "length": "4:59"},
                             {"track_number": 5, "title": "Ancient Nation", "length": "3:32"},
                         ],
                         "Model.Vinyl.Associations.AscGenre": [
                            {"genre_id": random.randint(1, 5)},
                         ],
                         "Model.Vinyl.Associations.AscSubGenre": [
                            {"sub_genre_id": random.randint(1, 5)},
                         ],
                         "Model.Vinyl.Associations.AscSellerRecord": [
                            {
                                "state": random.randint(1, 5),
                                "price": random.randint(1, 5),
                                "amount": random.randint(20, 30),
                                "seller_id": random.randint(1, 7),
                            },
                        ]
                         },

                    })
