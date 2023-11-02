import sqlalchemy as db
from config_ import engine
from Helper.GeneralHelper import create_pwd

# ---- testing stuff ------------
# only for evaluation so flask is not needed

# create db if needed
# from Helper.DDL_generator import create_ddl
# create_ddl()

from Helper.DbHelper import DbHelper
test = DbHelper(engine)

# print(create_pwd())

test.db_update({"objectPath": "Model.Vinyl.Record.Record",
                "attributes": [
                    {"id": "13", "title": "updat1", "artist": "addd"},
                    {"id": "14", "title": "updat2456", "artist": "schnurr"}
                ]})


test.db_insert({"objectPath": "Model.Vinyl.Record.Record",
                "attributes":
                    {"title": "asfdgfsd", "artist": "asd",
                     "Model.Vinyl.Track.Track": [
                         {"name": "track1", "length": "5:23"},
                         {"name": "track2", "length": "5:23"},
                         {"name": "track3", "length": "5:23"},
                     ]},
                })

# print(test.delete({"objectPath": "Model.Vinyl.Record.Record",
#                    "ids": [i for i in range(0, 100)]}))
