from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.orm import relationship, declarative_base
import sqlite3

Base = declarative_base()

# Établir une connexion à la base de données 
connexion = sqlite3.connect('bank.db')

# curseur
curseur = connexion.cursor()

class Transaction:
    # Création Transaction_Table
        curseur.execute('''CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY,
                    transaction_id INTEGER,
                    count_id INTEGER,
                    amount INTEGER,
                    type INTEGER,
                    timestamp INTEGER
                  )''')

        # curseur.execute("INSERT INTO transactions (transaction_id, count_id, amount, type, timestamp) VALUES ('5', '6', '7', '8', '8')")

        connexion.commit()

    
    def __init__(self, id, solde_initial=0):
        self.id = id
        self.solde = solde_initial

    def deposit(self, montant):
        self.solde += montant

    def withdraw(self, montant):
        if montant > self.solde:
            print("Fonds insuffisants.")
        else:
            self.solde -= montant

    def get_balance(self):
        print(f"Solde du compte de {self.id} : {self.solde}")

class Account:
    def __init__():
        # Création Account_Table
        curseur.execute('''CREATE TABLE IF NOT EXISTS utilisateurs (
                    id INTEGER PRIMARY KEY,
                    account_id INTEGER,
                    balance INTEGER
                  )''')

        # curseur.execute("INSERT INTO utilisateurs (account_id, balance) VALUES ('234', '3000')")

        connexion.commit()
        connexion.close()


        def __init__(self, nom_base_donnees):
            self.connexion = sqlite3.connect(nom_base_donnees)
            self.curseur = self.connexion.cursor()
            self.curseur.execute('''CREATE TABLE IF NOT EXISTS comptes (nom TEXT PRIMARY KEY, solde NUMERIC)''')
            self.connexion.commit()

    def creer_compte(self, nom, solde_initial=0):
        try:
            self.curseur.execute('''INSERT INTO comptes VALUES (?, ?)''', (nom, solde_initial))
            self.connexion.commit()
            print(f"Compte de {nom} créé avec succès.")
        except sqlite3.IntegrityError:
            print(f"Le compte de {nom} existe déjà.")

    def fermer(self):
        self.connexion.close()
