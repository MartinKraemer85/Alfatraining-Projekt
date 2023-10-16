from flask import Blueprint
from Helper.DbHelper import DbHelper
from Services.mail import test_mail

mail = Blueprint('mail', __name__)


@mail.route('/mail', methods=['GET'])
def send_mail() -> str:
    """
    Get an existing article

    :return: Article
    :rtype: str[json]
    """
    # TODO: Filter Kram
    db_helper = DbHelper()
    test_mail()
    return "Klappt"

send_mail()