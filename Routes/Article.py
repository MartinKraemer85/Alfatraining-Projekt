from typing import Any
from flask import Blueprint, request, jsonify
from Helper.DbHelper import DbHelper
from config_ import engine
article = Blueprint('article', __name__)


@article.route('/article', methods=['POST'])
def get_article() -> Any:
    """
    | Get an existing article. Post because it would be a hassle to create and parse the url.
    |
    | data example:
    | {
    | "table": "record",
    | "fields": ["artist", "title"],
    | "where": "where artist is not null"
    | }

    :return: Article
    :rtype: json
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


