from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from bank import Base, Account, Transaction

db_user = 'test_alchemy'
db_password = 'test_alchemy'
db_host = 'localhost'
db_port = '5432' 
db_name = 'test_alchemy'

db_url = 

engine = create_engine(db_url)

try:
    conn = engine.connect
    print("Success!")

    Base.metadata
