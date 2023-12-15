from decouple import config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# class Config:
#     SQLALCHEMY_TRACK_MODIFICATIONS = True
# class DevelopmentConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URL")
# class TestingConfig(Config):
#     TESTING = True
#     SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")
# class StagingConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True
#     SQLALCHEMY_DATABASE_URI = os.getenv("STAGING_DATABASE_URL")
# class ProductionConfig(Config):
#     DEBUG = False
#     SQLALCHEMY_DATABASE_URI = os.getenv("PRODUCTION_DATABASE_URL")
# config = {
#     "development": DevelopmentConfig,
#     "testing": TestingConfig,
#     "staging": StagingConfig,
#     "production": ProductionConfig
# }

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
"""
has been blocked by CORS policy: Response to preflight request doesn't pass access control check: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response 
serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
"""
CORS(app)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = f"mssql://@{config('SERVER')}/{config('DATABASE')}?driver={config('ODBC')}"
db.init_app(app)



# sqllite fuer Projektabgabe
# engine = db.create_engine(f"sqlite:///project.db", echo=True)
# engine = db.create_engine(f"sqlite:///E:\repos\Plattenfreude\project.db", echo=True)
