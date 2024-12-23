# Contient différentes fixtures 
import pytest
#from source.bank import Account, Transaction
import sys
sys.path.append('/document/app_bancaire_test/source/bank')



# fixture pour créer une instance de la classe Account
@pytest.fixture 
def account_instance():
    return source.bank.Account(1, 8)





