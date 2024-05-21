# exemple de transaction

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


