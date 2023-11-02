import sqlalchemy as db
from decouple import config

# make the engine available for all modules that need it
# engine = db.create_engine(f"mssql://@{config('SERVER')}/{config('DATABASE')}?driver={config('ODBC')}")

# sqllite fuer Projektabgabe
engine = db.create_engine(f"sqlite:///project.db", echo=True)

