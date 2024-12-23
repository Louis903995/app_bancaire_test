from bank import Account, Transaction

# Exemple d'utilisation
if __name__ == "__main__":
    
    # Création d'un compte 
    compte1 = Account.create_account(1, 100)
    compte2 = Account.create_account(2, 50)
    """
    # Consultation du solde
    compte = Account.get_account_by_id(2)
    compte.afficher_infos()
    
    # Dépôt 
    compte = Account.get_account_by_id(4)
    depot = Transaction(compte, None, 0, '')
    depot.deposit(100)
    
    # Retrait 
    compte = Account.get_account_by_id(7)
    retrait = Transaction(compte, None, 0, '')
    retrait.withdraw(10)
    """
    # Sélectionner compte
    compte1 = Account.get_account_by_id(1)
    compte2 = Account.get_account_by_id(2)
    
    # Effectuer un virement du compte1 vers le compte2
    if compte1 and compte2:
        transaction = Transaction(compte1, compte2, 50, '')
        transaction.transfer()
    else:
        print("Un des comptes n'a pas été trouvé.")
    
    
""" 
    ### Tests pour les Dépôts:
    # test_deposit_normal
    compte = Account.get_account_by_id(1)
    depot = Transaction(compte, None, 0, '')
    depot.deposit(100)
    # test_deposit_negative_amount
    compte = Account.get_account_by_id(1)
    depot = Transaction(compte, None, 0, '')
    depot.deposit(-10)
    # test_deposit_zero_amount
    compte = Account.get_account_by_id(1)
    depot = Transaction(compte, None, 0, '')
    depot.deposit(0)

    
    ### Tests pour les Retraits: 
    # test_withdraw_normal
    compte = Account.get_account_by_id(2)
    retrait = Transaction(compte, None, 0, '')
    retrait.withdraw(10)
    # test_withdraw_insufficient_funds
    compte = Account.get_account_by_id(2)
    retrait = Transaction(compte, None, 0, '')
    retrait.withdraw(150)
    # test_withdraw_negative_amount
    compte = Account.get_account_by_id(2)
    retrait = Transaction(compte, None, 0, '')
    retrait.withdraw(-50)
    # test_withdraw_negative_amount
    compte = Account.get_account_by_id(2)
    retrait = Transaction(compte, None, 0, '')
    retrait.withdraw(0)

    
    ### Tests pour les Transferts:
    compte1 = Account.get_account_by_id(2)
    compte2 = Account.get_account_by_id(2)
    # test_transfer_normal
    if compte1 and compte2:
        transaction = Transaction(compte1, compte2, 40, '')
        transaction.transfer()
    else:
        print("Un des comptes n'a pas été trouvé.")

    # test_transfer_insufficient_funds:
    if compte1 and compte2:
        transaction = Transaction(compte1, compte2, 500, '')
        transaction.transfer()
    else:
        print("Un des comptes n'a pas été trouvé.")

    # test_transfer_negative_amount:
    if compte1 and compte2:
        transaction = Transaction(compte1, compte2, -10, '')
        transaction.transfer()
    else:
        print("Un des comptes n'a pas été trouvé.")
    
    # test_transfer_zero_amount
    if compte1 and compte2:
        transaction = Transaction(compte1, compte2, 0, '')
        transaction.transfer()
    else:
        print("Un des comptes n'a pas été trouvé.")
    

    ## Tests pour la Consultation de Solde (Get Balance):
    compte = Account.get_account_by_id(2)
    compte.afficher_infos()
"""


