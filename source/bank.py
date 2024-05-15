from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base
import sqlite3

Base = declarative_base()

class Account:

    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)


    def account_id(self, client_id):
        self.client_id = client_id
    
    def balance(self, money, float):
        self.money = money
        self.client_id = []


class Transaction:

    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)

    
    def transaction_id(self, transaction_id):
        self.transaction_id = transaction_id
    
    def account_id(self, client_id):
        self.client_id = client_id

    def amount(self, dollar):
        self.dollar = dollar 
    
    def type(self, deposit, withdraw, transfer):
        self.deposit = deposit 
        self.withdraw = withdraw 
        self.transfer = transfer 
    
    def timestamp(self, day, hours):
        self.day = day
        self.hours = hours 

# initialise la connexion à la BDD 

# Établir une connexion à la base de données 
connexion = sqlite3.connect('BDD.db')

# curseur
curseur = connexion.cursor()

# Créer une table
curseur.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                    id INTEGER PRIMARY KEY,
                    account_id INTEGER,
                    balance INTEGER
                  )''')

curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('234', 3000)")
curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('678', 25)")
curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('87','98')")
curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('889','9678')")
curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('8567','9856')")
curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('8787','908')")


connexion.commit()
connexion.close()