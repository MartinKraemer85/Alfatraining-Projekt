from flask import Blueprint

hello_world = Blueprint('hello_world', __name__)


@hello_world.route('/hello_world', methods=['GET'])
def verify_password() -> str:
    return "Hello World"
