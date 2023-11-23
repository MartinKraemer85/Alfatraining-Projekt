from typing import Any, List, Tuple
from flask import Blueprint, request, jsonify
from Helper.DbHelper import DbHelper
from config_ import engine

article = Blueprint('get_article', __name__)


@article.route('/select', methods=['POST'])
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
        db_helper = DbHelper(engine)
        return jsonify(db_helper.select(json.get("table"), json.get("fields"), json.get("where")))
    else:
        return 'Content-Type not supported', 400


@article.route('/select_all_articles', methods=['POST'])
def select_all_articles() -> tuple[str, int] | Any:
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        db_helper = DbHelper(engine)
        return db_helper.select_all("Model.Vinyl.Record.Record")
    else:
        return 'Content-Type not supported', 400
