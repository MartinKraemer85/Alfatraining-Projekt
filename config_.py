import sqlalchemy as db
from decouple import config

# make the engine available for all modules that need it
# https://docs.sqlalchemy.org/en/20/errors.html#error-3o7r
engine = db.create_engine(f"mssql://@{config('SERVER')}/{config('DATABASE')}?driver={config('ODBC')}",  max_overflow=-1)

