from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base
import sqlite3

Base = declarative_base()

class Account:

    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


class Transaction:

    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)

    
# Établir une connexion à la base de données 
connexion = sqlite3.connect('BDD.db')

# curseur
curseur = connexion.cursor()

# Créer une table
curseur.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                    id INTEGER PRIMARY KEY,
                    account INTEGER,
                    balance INTEGER, 
                    transaction_id INTEGER,
                    amount INTEGER,
                    type INTEGER,
                    timestamp INTEGER
                  )''')

curseur.execute("INSERT INTO utilisateurs (account, balance, transaction_id , amount, type, timestamp) VALUES ('234', '3000', '5', '6', '7', '8')")
curseur.execute("INSERT INTO utilisateurs (account, balance, transaction_id, amount, type, timestamp) VALUES ('889','9678', '5', '6', '7', '8')")
curseur.execute("INSERT INTO utilisateurs (account, balance, transaction_id, amount, type, timestamp) VALUES ('889','9678', '5', '6', '7', '8')")
curseur.execute("INSERT INTO utilisateurs (account, balance, transaction_id, amount, type, timestamp) VALUES ('889','9678', '5', '6', '7', '8')")


connexion.commit()
connexion.close()
