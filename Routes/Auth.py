from flask_httpauth import HTTPBasicAuth
from settings import engine

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username: str, password: str) -> bool:
    """
    Password verification

    :param username: Name of the user
    :param password: The actual password
    :return: Authentication succeeded or not
    """
    # TODO: passwort verification + session?
    return False
