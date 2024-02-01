from Helper.GeneralHelper import create_pwd
from Helper.DDLGenerator import create_ddl
from decouple import config
from Helper.DbHelper import DbHelper
from settings import db, app
import random

# print(test.select("record", ["*"], "where artist = 'Leichenzug'"))

# ---- testing stuff ------------
# create db if needed
with app.app_context():
    db_helper = DbHelper(db)
    test = db_helper.select_all_where(object_path="Model.Vinyl.Record.Record",
                                      where="genre_1.name = 'Black Metal'")
    # test = db_helper.select_all_where(object_path="Model.AddressDetails.Country.Country")
    # test = db_helper.select_all_where(object_path="Model.AddressDetails.Country.Country"
    #                                   ,where="street_1.id = 1")
    # test = db_helper.select_all_where(object_path="Model.AddressDetails.Address.Address",
    #                                   where="street_4.id  = 1 and ")

    print(test)

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
