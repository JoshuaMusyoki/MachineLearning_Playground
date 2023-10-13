
from numpy import block
from steem.post import Post
from steem.amount import Amount
from self import self

def _init_(self, amount, user, memo):
    self.user=user
    self.amount=Amount(amount)
    self.memo=memo
    self.post=0
    
class Queue():
    def __init__(self, steem, account):
        self.list={}
        self.total_sbd=0
        self.steem=steem
        self.account=account
        
#Check each transaction is of transfer type, if so operation is processed
for transaction in block['transactions']: # type: ignore
    # Self.process_transaction[transaction]
    self.process_transaction[transaction]
            
def process_transaction(self, transaction):
    if transaction['operation'][0][0]=='transfer':
        operation=transaction['operation'][0][1]
        self.process_transfer(operation)
        
