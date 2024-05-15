from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Account:
    def account_id(self, client_id):
        self.client_id = client_id
    
    def balance(self, money, float):
        self.money = money
        self.client_id = []


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




