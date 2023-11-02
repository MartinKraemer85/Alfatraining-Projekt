from typing import Any

from flask import Blueprint, request, jsonify
from Helper.DbHelper import DbHelper
from Services.mail import test_mail
from config_ import engine

mail = Blueprint('mail', __name__)


@mail.route('/mail', methods=['POST'])
def send_mail() -> Any:
    """
    | Send a mail to the given destination.
    | Route:  http://192.168.0.2:5000/mail
    | Content-Type: application/json
    | Content-Length: <calculated when request is sent>

    :return: Error / "success"
    """
    # TODO: What shall be returned?
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        if not json.get("mail_adress"):
            return "Bad Request", 400
        test_mail(receiver=json.get("mail_adress"))
        return "success"
    else:
        return 'Content-Type not supported', 400
