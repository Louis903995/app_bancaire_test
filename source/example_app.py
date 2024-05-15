# opérations 

def withdraw(number_one, number_two):
    return number_one + number_two

def deposit(number_one, number_two):
    if number_one >= number_two:
        return number_one - number_two
    
def transfer(account_1, account_2, montant):
    if montant <= account_1:
        account_2 += montant
    return account_2
