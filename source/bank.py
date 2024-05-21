from datetime import datetime
import random 

class Account:
    def __init__(self, id, solde_compte):
        self.id = id
        self.solde_compte = solde_compte
    
    def afficher_infos(self):
        print(f"Numéro compte: {self.id}; Solde: {self.solde_compte}")
    
    def ajuster_solde(self, montant):
        self.solde_compte += montant

    
class Transaction:
    def __init__(self, account_instance, type, amount):
        self.account = account_instance
        self.transaction_id = random.randint(100000, 999999)
        self.amount = amount
        self.type = type
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def info_av(self):
        print(f"Le compte {self.account.id} a fait un {self.type} de {self.amount}$; Transaction n°{self.transaction_id}; heure: {self.timestamp}; Solde: {self.account.solde_compte}$")

    def info_ap(self):
        print(f"Solde après dépôt: {self.account.solde_compte}$")
        
    def deposit(self, somme):
        self.amount = somme
        self.type = 'dépôt'
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.info_av()
        self.account.ajuster_solde(somme)
        self.info_ap()

    def withdraw(self, somme):
        self.amount = somme
        self.type = 'retrait'
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.info_av()
        if somme <= self.account.solde_compte:
            self.account.ajuster_solde(-somme)
            self.info_ap()
        else:
            print(f'Solde insuffisant pour effectuer le retrait de {somme}$')


# Exemple d'utilisation
compte = Account(12345, 1000)
transaction = Transaction(compte, '', '')


"""
# Tentative de retrait de 1500$ (devrait échouer)
transaction.withdraw(500)
compte.afficher_infos()
"""
# Dépôt de 500$
transaction.deposit(4000)
compte.afficher_infos()
