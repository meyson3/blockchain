import hashlib
import json
from time import time

class Blockchain(object):
    def__init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash = 1, proof=100)
    def new_block(self, proof, previous_hash=None):
        
        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """
        block = {
            'index' : len(self.chain) + 1,
            'timestamp' : time(),
            'transactions' : slef.current_transactions,
            'proof' : proof,
            'previous_hash' : previous_hash or self.hash(self.chain[-1]),
        }
        # Reset the current list of transactions
        
        self.current_transactions = []

        self.chain.append(block)
        return block
        pass
        
    def new_transaction(self, sender, recipient, amount):
        """
        Creates a new transaction to go into the next mined block
        :paramm sender: <str> Address of the sender
        :param recipient: <str> Address of the recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        
        self.current_transactions.append({
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount,
            })
            
    return self.last_block['index'] + 1
    @staticmethod
    def hash(block):
       """
        Creates a SHA-256 hash of a Block
        :param block: <dict> Block
        :return: <str>
        """
        pass
        
    @property
    def last_block(self):
        return self.chain[-1]
        pass
        
    