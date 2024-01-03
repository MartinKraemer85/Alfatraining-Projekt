from Helper.DbHelper import DbHelper
from settings import engine, set_current_data


def synch():
    db_ = DbHelper(engine)
    set_current_data(db_.select_all_where("Model.Vinyl.Record.Record", True))
