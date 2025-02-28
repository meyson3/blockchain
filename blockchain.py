import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uudi4

from flask import Flask


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
    def proof_of_work(self, last_proof):
         """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof
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
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
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
    
    #Instantiate our Node
    app = Flask(__name__)
    
    #generate a globally unique address for this node
    node_identifier = str(uudi4()).replace('-'.'')
    
    #Instantiate the Blockchain
    blockchain = Blockchain()
    
    @app.route('/mine', methods=['GET'])
    def mine():
        return "We'll mine a new block"
    
    @app.route('/transactions/new', methods=['POST'])
    def new_transaction():
        return "We'll add a new transaction"

    @app.route('/chain', methods=['GET'])
    def full_chain():
        response = {
            'chain': blockchain.chain,
            'length': len(blockchain.chain),
        }
        return jsonify(response), 200

    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
    