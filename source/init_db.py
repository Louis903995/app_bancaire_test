from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base
import sqlite3

Base = declarative_base()

# Établir une connexion à la base de données 
connexion = sqlite3.connect('bank.db')

# curseur
curseur = connexion.cursor()

# Création Account_Table
curseur.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                    id INTEGER PRIMARY KEY,
                    account_id INTEGER,
                    balance INTEGER
                  )''')

curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('234', '3000')")
curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('889', '9678')")

connexion.commit()

# Création Transaction_Table
curseur.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY,
                    transaction_id INTEGER,
                    count_id INTEGER,
                    amount INTEGER,
                    type INTEGER,
                    timestamp INTEGER
                  )''')

curseur.execute("INSERT INTO transactions (transaction_id, count_id, amount, type, timestamp) VALUES ('5', '6', '7', '8', '8')")
curseur.execute("INSERT INTO transactions (transaction_id, count_id, amount, type, timestamp) VALUES ('5', '6', '7', '8', '9')")
curseur.execute("INSERT INTO transactions (transaction_id, count_id, amount, type, timestamp) VALUES ('5', '6', '7', '8', '9')")
curseur.execute("INSERT INTO transactions (transaction_id, count_id, amount, type, timestamp) VALUES ('5', '6', '7', '8', '9')")

connexion.commit()

connexion.close()