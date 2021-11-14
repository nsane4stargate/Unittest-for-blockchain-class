import unittest
from backend.blockchain_pkg._block import Block, GENESIS_DATA

class TestBlock(unittest.TestCase):

    def test_mined_block(self):
        last_block = Block.genesis()
        data = 'test-data'
        mine_block = Block.mine_block(last_block, data)

        # Check if block is an instance
        self.assertIsInstance(mine_block, Block, msg="mine_block is not an insance of the Block class" )
        # Check it the data in the mined block is the same
        self.assertTrue(mine_block.data == data)
        # Check if the previous block's hash is the same as mined_block.last_hash 
        self.assertTrue(mine_block.last_hash == last_block.hash)

    def test_genesis(self):
        genesis = Block.genesis()

        # Checks to see the genisis block is of a Block instance 
        self.assertIsInstance(genesis, Block, msg='Genesis is not an instance of Block')

        # Check to see if each fields are the same
        for key, value in GENESIS_DATA.items():
            self.assertTrue(getattr(genesis, key) == value)

if __name__=='__main__':
    unittest.main()
        