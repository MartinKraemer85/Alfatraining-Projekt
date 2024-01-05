from settings import app
from Routes import Article
from Routes import Mail
from Routes import Customer
from threading import Thread
import time

"""
Docu Kram:
sphinx-build -b html source build
Requirement Kram:
pip freeze > requirements.txt
pip install -r requirements.txt
npm i --save @fortawesome/fontawesome-svg-core
npm i --save @fortawesome/free-solid-svg-icons
npm i --save @fortawesome/free-regular-svg-icons
npm i --save @fortawesome/free-brands-svg-icons
npm i --save @fortawesome/react-fontawesome@latest
npm i --save react-select

package json -->   "proxy": "http://localhost:5000"
npm install rimraf -g  | rimraf node_modules # delete node modules
"""


@app.route('/time')
def get_current_time():
    return {'time': time.time()}


if __name__ == '__main__':
    # with app.app_context():
    #     t = Thread(target=synch, daemon=True)
    #     t.start()

    app.run(host='0.0.0.0')

import time

# todo: amount, haendler, verpackung? many to many insert? Bulk Insert?
