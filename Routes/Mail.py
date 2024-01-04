from typing import Any
from flask import request
from Services.Mail import mail
from settings import app


@app.route('/mail', methods=['POST'])
def send_mail() -> Any:
    """
    | Send a mail to the given destination.
    | Route:  http://192.168.0.2:5000/mail
    | Method: POST
    | Header-content:
    | Content-Type: application/json
    | Content-Length: <calculated when request is sent>

    :return: Error / "success"
    """

    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        json = request.json
        if not json.get("mail_address"):
            return "Bad Request", 400
        mail(first_name=json.get("first_name"),
                  last_name=json.get("last_name"),
                  mail_address=json.get("mail_address"),
                  subject=json.get("subject"),
                  issue=json.get("issue"))
        # maybe safe the mails?
        return "success", 200
    else:
        return 'Content-Type not supported', 400
