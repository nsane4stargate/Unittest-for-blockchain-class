import unittest
from backend.blockchain_pkg._block import Block, GENESIS_DATA
from backend.blockchain_pkg._blockchain import Blockchain

class TestBlockchain(unittest.TestCase):

    def test_blockchain_instance(self):
        blockchain = Blockchain()

        # Check if this is an instance of the Blockchain class 
        # using the 'hash' attribute
        self.assertTrue(blockchain.chain[0].hash == GENESIS_DATA['hash'])

    def test_add_block(self):
        blockchain = Blockchain()
        data = 'test-data'
        blockchain.add_block(data)

        # Checks to see if the data from the last block added 
        # is the same as the data that was passed as a parameter
        self.assertEqual(blockchain.chain[-1].data, data, msg='The last block added to the chain has different data')


if __name__=='__main__':
    unittest.main()
