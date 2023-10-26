from flask import Blueprint
from Helper.DbHelper import DbHelper
from config_ import engine
article = Blueprint('article', __name__)


@article.route('/article', methods=['GET'])
def get_article() -> str:
    """
    Get an existing article

    :return: Article
    :rtype: str[json]
    """
    # TODO: Filter Kram
    db_helper = DbHelper(engine)
    return db_helper.select("record", ["artist", "title"], "where artist is not null")
