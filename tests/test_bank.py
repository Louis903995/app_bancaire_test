from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys
import os
print(sys.path)
sys.path.append('/home/louis/Documents/app_bancaire_test')
from source.bank import Base, Account, Transaction

# Ajouter le chemin du dossier contenant le module ou package désiré
chemin_module = '/home/louis/Documents/app_bancaire_test/source'
if chemin_module not in sys.path:
    sys.path.append(chemin_module)


db_url = "sqlite:///bank.db"

engine = create_engine(db_url)

try:
    conn = engine.connect
    print("succes!")

except Exception as ex:
    print(ex)
    conn = engine.connect
    print("Success!")

    Base.metadata
    