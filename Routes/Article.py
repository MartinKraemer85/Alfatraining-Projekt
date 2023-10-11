from flask import Blueprint
from Helper.DbHelper import DbHelper
article = Blueprint('article', __name__)


@article.route('/article', methods=['GET'])
def get_article() -> dict:
    db_helper = DbHelper()
    ret = db_helper.select("record", "where artist is not null", ["artist", "title"])
    print()
    return ret
# def get_article(filer: dict) -> dict:
#     """
#     Get an existing article
#
#     :return: Article
#     :rtype: dict
#     """
#     return {"Schnarr": "Miau"}
