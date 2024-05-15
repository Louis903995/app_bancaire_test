from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Account:

    __tablename__ = 'account'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

    stocks = relationship("")

    def account_id(self, client_id):
        self.client_id = client_id
    
    def balance(self, money, float):
        self.money = money
        self.client_id = []


class Transaction:

    __tablename__ = 'transaction'

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer)

    

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

