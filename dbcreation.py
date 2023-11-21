import sqlalchemy as db
from config_ import engine
from Helper.GeneralHelper import create_pwd
from Helper.DDLGenerator import create_ddl
from Helper.DbHelper import DbHelper

# ---- testing stuff ------------
# create db if needed
create_ddl()
test = DbHelper(engine)
#


if True:

    test.db_insert({"objectPath": "Model.Vinyl.Genre.Genre",
                    "attributes": {"name": "Rock"},
                    })
    test.db_insert({"objectPath": "Model.Vinyl.Genre.Genre",
                    "attributes": {"name": "Rock"},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Genre.Genre",
                    "attributes": {"name": "Metal"},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Genre.Genre",
                    "attributes": {"name": "Black Metal"},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Genre.Genre",
                    "attributes": {"name": "Death Metal"},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Genre.SubGenre",
                    "attributes": {"name": "DBM"},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Genre.SubGenre",
                    "attributes": {"name": "Raw"},
                    })
    test.db_insert({"objectPath": "Model.Vinyl.Genre.SubGenre",
                    "attributes": {"name": "Folk"},
                    })
    test.db_insert({"objectPath": "Model.Vinyl.Genre.SubGenre",
                    "attributes": {"name": "DBM"},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Associations.AscGenre",
                    "attributes": {"record_id": 1,
                                   "genre_id": 1},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Associations.AscGenre",
                    "attributes": {"record_id": 2,
                                   "genre_id": 2},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Associations.AscGenre",
                    "attributes": {"record_id": 3,
                                   "genre_id": 3},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Associations.AscGenre",
                    "attributes": {"record_id": 4,
                                   "genre_id": 4},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Associations.AscSubGenre",
                    "attributes": {"record_id": 1,
                                   "sub_genre_id": 1},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Associations.AscSubGenre",
                    "attributes": {"record_id": 2,
                                   "sub_genre_id": 2},
                    })
    test.db_insert({"objectPath": "Model.Vinyl.Associations.AscSubGenre",
                    "attributes": {"record_id": 3,
                                   "sub_genre_id": 3},
                    })
    test.db_insert({"objectPath": "Model.Vinyl.Associations.AscSubGenre",
                    "attributes": {"record_id": 4,
                                   "sub_genre_id": 4},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Record.Record",
                    "attributes":
                        {"title": "Lunar Poetry",
                         "artist": "Mokturnal Mortum",
                         "type": "Vinyl",
                         "year": 2008,
                         "genre": "Metal",
                         "stile": "Black Metal",
                         "state": 2,
                         "price": 20.99,
                         "Model.Vinyl.Track.Track": [
                             {"track_number": 1, "title": "track1", "length": "5:23"},
                             {"track_number": 2, "title": "track2", "length": "5:23"},
                             {"track_number": 3, "title": "track3", "length": "5:23"},
                         ]},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Record.Record",
                    "attributes":
                        {"title": "Das letzte Gebet",
                         "artist": "Leichenzug",
                         "type": "Vinyl",
                         "year": 2008,
                         "genre": "Metal",
                         "stile": "Black Metal",
                         "state": 2,
                         "price": 16.99,
                         "Model.Vinyl.Track.Track": [
                             {"track_number": 1, "title": "track1", "length": "5:23"},
                             {"track_number": 2, "title": "track2", "length": "5:23"},
                             {"track_number": 3, "title": "track3", "length": "5:23"},
                         ]},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Record.Record",
                    "attributes":
                        {"title": "Kaleidoscope Dreams",
                         "artist": "Black Magic SS",
                         "type": "Vinyl",
                         "year": 2008,
                         "genre": "Rock",
                         "stile": "Black Metal",
                         "state": 2,
                         "price": 18.99,
                         "Model.Vinyl.Track.Track": [
                             {"track_number": 1, "title": "track1", "length": "5:23"},
                             {"track_number": 2, "title": "track2", "length": "5:23"},
                             {"track_number": 3, "title": "track3", "length": "5:23"},
                         ]},
                    })

    test.db_insert({"objectPath": "Model.Vinyl.Record.Record",
                    "attributes":
                        {"title": "Weltanschauung",
                         "artist": "Mokturnal Mortum",
                         "type": "Vinyl",
                         "year": 2008,
                         "genre": "Metal",
                         "stile": "Black Metal",
                         "state": 2,
                         "price": 5.99,
                         "Model.Vinyl.Track.Track": [
                             {"track_number": 1, "title": "track1", "length": "5:23"},
                             {"track_number": 2, "title": "track2", "length": "5:23"},
                             {"track_number": 3, "title": "track3", "length": "5:23"},
                         ]},
                    })

    # print(test.select("record", ["*"], ""))
# test.db_update({"objectPath": "Model.Vinyl.Record.Record",
#                 "attributes": [
#                     {"id": "13", "title": "updat1", "artist": "addd"},
#                     {"id": "14", "title": "updat2456", "artist": "schnurr"}
#                 ]})


# print(test.delete({"objectPath": "Model.Vinyl.Record.Record",
#                    "ids": [i for i in range(0, 100)]}))
