from typing import Any

from flask import Blueprint, request, jsonify
from Helper.DbHelper import DbHelper
from Services.mail import test_mail
from config_ import engine

mail = Blueprint('mail', __name__)


@mail.route('/mail', methods=['POST'])
def send_mail() -> Any:
    """
    Get an existing article

    :return: Article
    :rtype: str
    """
    # TODO: Filter Kram
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        if not json.get("mail_adress"):
            return "Bad Request", 400
        test_mail(to= json.get("mail_adress"))
        return "passt"
    else:
        return 'Content-Type not supported', 400

