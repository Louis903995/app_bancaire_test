from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base
import sqlite3

Base = declarative_base()

# Établir une connexion à la base de données 
connexion = sqlite3.connect('bank.db')

# curseur
curseur = connexion.cursor()

# Créer une table
curseur.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                    id INTEGER PRIMARY KEY,
                    account_id INTEGER,
                    balance INTEGER, 
                    transaction_id INTEGER,
                    count_id INTEGER,
                    amount INTEGER,
                    type INTEGER,
                    timestamp INTEGER
                  )''')

curseur.execute("INSERT INTO utilisateurs (account_id, balance, transaction_id, count_id, amount, type, timestamp) VALUES ('234', '3000', '5', '6', '7', '8', '8')")
curseur.execute("INSERT INTO utilisateurs (account_id, balance, transaction_id, count_id, amount, type, timestamp) VALUES ('889', '9678', '5', '6', '7', '8', '9')")
curseur.execute("INSERT INTO utilisateurs (account_id, balance, transaction_id, count_id, amount, type, timestamp) VALUES ('889', '9678', '5', '6', '7', '8', '5')")
curseur.execute("INSERT INTO utilisateurs (account_id, balance, transaction_id, count_id, amount, type, timestamp) VALUES ('889', '9678', '5', '6', '7', '8', '4')")
curseur.execute("INSERT INTO utilisateurs (account_id, balance, transaction_id, count_id, amount, type, timestamp) VALUES ('889', '9678', '5', '6', '7', '8', '4')")

connexion.commit()
connexion.close()

class Account:
    def creer_compte(self, id_account, solde_initial=0):
        self.id_account = id_account
        self.solde_initial = solde_initial
    
class Transaction:
    def __init__(self, id_account, id_transaction):
        self.id_account = id_account
        self.id_transaction = id_transaction

    def montant(self, montant_transaction):
        self.montant_transaction = montant_transaction
    
    def timestamp(self, date, hours):
        self.date = date 
        self.hours = hours 
    
    def type(self, deposit, withdraw):
        self.deposit = deposit
        self.withdraw = withdraw