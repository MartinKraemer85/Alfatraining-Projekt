from typing import Any
from flask import request
from Helper.DbHelper import DbHelper
from settings import app, db


@app.route('/select', methods=['POST'])
def select() -> tuple[str, int] | Any:
    """
    | Get an existing article. Post because it would be a hassle to create and parse the url.
    | Route: http://192.168.0.2:5000/get_article
    | Method: POST
    | Header-content:
    | Content-Type: application/json
    | Content-Length: <calculated when request is sent>
    | raw data example:
    | {
    | "table": "record",
    | "fields": ["artist", "title"],
    | "where": "where artist is not null"
    | }

    :return: Article / Error
    """
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        if not json.get("table") or not json.get("fields"):
            return "Bad request, fool!", 400
        db_helper = DbHelper(db)
        return db_helper.select(json.get("table"), json.get("fields"), json.get("where"))
    else:
        return 'Content-Type not supported', 400


@app.route('/select_all_articles', methods=['POST'])
def select_all_articles() -> tuple[str, int] | Any:
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        db_helper = DbHelper(db)
        print(json)
        return db_helper.select_all_where(object_path="Model.Vinyl.Record.Record",
                                          initial=json.get("initial"),
                                          where=json.get("where"))
    else:
        return 'Content-Type not supported', 400
