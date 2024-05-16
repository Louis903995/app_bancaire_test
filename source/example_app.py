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


class Transaction:

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



class Account():
    def account_id(self, client_id):
        self.client_id = client_id
    
    def balance(self, money, float):
        self.money = money
        self.client_id = []
