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
                             {"track_number": 1, "name": "track1", "length": "5:23"},
                             {"track_number": 2, "name": "track2", "length": "5:23"},
                             {"track_number": 3, "name": "track3", "length": "5:23"},
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
                             {"track_number": 1, "name": "track1", "length": "5:23"},
                             {"track_number": 2, "name": "track2", "length": "5:23"},
                             {"track_number": 3, "name": "track3", "length": "5:23"},
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
                             {"track_number": 1, "name": "track1", "length": "5:23"},
                             {"track_number": 2, "name": "track2", "length": "5:23"},
                             {"track_number": 3, "name": "track3", "length": "5:23"},
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
                             {"track_number": 1, "name": "track1", "length": "5:23"},
                             {"track_number": 2, "name": "track2", "length": "5:23"},
                             {"track_number": 3, "name": "track3", "length": "5:23"},
                         ]},
                    })

    print(test.select("record", ["*"], ""))
# test.db_update({"objectPath": "Model.Vinyl.Record.Record",
#                 "attributes": [
#                     {"id": "13", "title": "updat1", "artist": "addd"},
#                     {"id": "14", "title": "updat2456", "artist": "schnurr"}
#                 ]})


# print(test.delete({"objectPath": "Model.Vinyl.Record.Record",
#                    "ids": [i for i in range(0, 100)]}))
