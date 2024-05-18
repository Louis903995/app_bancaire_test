class Account:
    def __init__(self, id, solde_initial=0):
        self.id = id
        self.solde_initial = solde_initial
    
    def afficher_infos(self):
        print(f"Numéro du compte: {self.id}, Solde: {self.solde_initial}")
    
    def solde_du_compte(self, montant):
        self.solde_initial += montant


class Transaction:
    def __init__(self, transaction_id, account_id, amount, type, timestamp, solde_compte):
        self.transaction_id = transaction_id
        self.account_id = account_id
        self.amount = amount
        self.type = type
        self.timestamp = timestamp
        self.solde_compte = solde_compte

    def afficher_infos(self):
        print(f"Le compte {self.account_id} a fait un {self.type} de {self.amount}$, transaction: {self.transaction_id}, solde compte: {self.solde_compte}$, heure: {self.timestamp}")

    def deposit(self, somme):
        self.solde_compte += somme
    
    def withdraw(self, somme):
        self.solde_compte -= somme


transaction = Transaction(281654, 454564, 100, 'retait', '8h25', 785)
transaction.afficher_infos()
print('-----')
transaction.deposit(15)
transaction.afficher_infos()
print('-----')
transaction.withdraw(100)
transaction.afficher_infos()





