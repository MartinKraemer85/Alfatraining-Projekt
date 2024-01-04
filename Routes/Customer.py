from flask import request
from Helper.DbHelper import DbHelper
from settings import app, db
from typing import Any


@app.route('/update_customer', methods=['Post'])
def update_customer() -> tuple[str, int] | Any:
    """

    :return:
    """
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        db_helper = DbHelper(db)

        db_helper.update(object_path=json.get("objectPath"),
                         values=json.get("attributes"))
        return "updated", 200
    else:
        return 'Content-Type not supported', 400
