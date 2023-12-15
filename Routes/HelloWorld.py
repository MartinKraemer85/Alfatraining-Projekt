from settings import app


@app.route('/hello_world', methods=['GET'])
def hello_world() -> str:
    return "Hello World"
