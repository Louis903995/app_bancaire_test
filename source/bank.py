import sqlite3
import random
from datetime import datetime

class Account:
    def __init__(self, id, solde_compte):
        self.id = id
        self.solde_compte = solde_compte

    def afficher_infos(self):
        print(f"Numéro compte: {self.id}; Solde: {self.solde_compte}")

    def ajuster_solde(self, montant):
        self.solde_compte += montant
        # Mise à jour du solde dans la base de données
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE Account SET solde_compte = ? WHERE id = ?', (self.solde_compte, self.id))
        conn.commit()
        conn.close()

    @staticmethod
    def create_account(id, solde_compte):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO Account (id, solde_compte) VALUES (?, ?)', (id, solde_compte))
        conn.commit()
        conn.close()
        return Account(id, solde_compte)

    @staticmethod
    def get_account_by_id(account_id):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Account WHERE id = ?', (account_id,))
        account_data = cursor.fetchone()
        conn.close()

        if account_data:
            return Account(*account_data)
        else:
            return None


class Transaction:
    def __init__(self, account, dest_account, amount, type):
        self.account = account
        self.dest_account = dest_account
        self.transaction_id = random.randint(10000000, 99999999)
        self.amount = amount
        self.type = type
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
    def info_av(self):
        print(f"Le compte {self.account.id} va faire un {self.type} de {self.amount}$; Transaction n°{self.transaction_id}; heure: {self.timestamp}; solde avant : {self.account.solde_compte}$")

    def info_ap(self):
        print(f"Solde après {self.type}: {self.account.solde_compte}$")

    def deposit(self, somme):
        self.amount = somme
        self.type = 'dépôt'
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.info_av()
        self.account.ajuster_solde(somme)
        self.info_ap()
        self.save_transaction()

    def withdraw(self, somme):
        self.amount = somme
        self.type = 'retrait'
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.info_av()
        if somme <= self.account.solde_compte:
            self.account.ajuster_solde(-somme)
            self.info_ap()
            self.save_transaction()
        else:
            print(f'Solde insuffisant pour effectuer le retrait de {somme}$')

    def transfer(self):
        if self.amount <= self.account.solde_compte:
            self.type = 'virement'
            self.account.ajuster_solde(-self.amount)
            self.dest_account.ajuster_solde(self.amount)
            print(f"Virement de {self.amount}$ effectué avec succès du compte {self.account.id} au compte {self.dest_account.id}.")
            self.save_transaction()
        else:
            print("Solde insuffisant pour effectuer le virement.")
            
    def save_transaction(self):
        conn = sqlite3.connect('bank.db')
        cursor = conn.cursor()
        if self.dest_account:
            cursor.execute('''
                INSERT INTO "Transaction" (transaction_id, account_id, amount, type, timestamp)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.transaction_id, self.account.id, self.amount, self.type, self.timestamp))
        else:
            cursor.execute('''
                INSERT INTO "Transaction" (transaction_id, account_id, amount, type, timestamp)
                VALUES (?, ?, ?, ?, ?)
            ''', (self.transaction_id, self.account.id, self.amount, self.type, self.timestamp))
        conn.commit()
        conn.close()

    
