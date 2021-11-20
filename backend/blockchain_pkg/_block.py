import time
from backend.util_pkg._crypto_hash import crypto_hash

GENESIS_DATA = {
    'timestamp': 1,
    'hash':'genesis_hash',
    'last_hash': 'genesis_last_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
    }

class Block:
    """
    Block: a unit of storage
    Store transactions in a blockchain that supports a cryptocurrency
    """
    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.hash = hash
        self.last_hash = last_hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce
        
    def __repr__(self):
        return (
            'Block ('
            f'timestamp: {self.timestamp}, '
            f'hash: {self.hash}, '
            f'last_hash: {self.last_hash}, '
            f'data: {self.data}), '
            f'data: {self.difficulty}), '
            f'data: {self.nonce}) '
        )
    
    @staticmethod
    def mine_block(last_block, data):
        """
        Mine a block based on the given last_block and data, until a has 
        is found that meet's the leading 0's proof of work requirement
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        difficulty = last_block.difficulty
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        while hash[:difficulty] != '0' * difficulty:
            nonce+=1
            timestamp = timestamp = time.time_ns()
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)
            
        return Block(timestamp, last_hash, hash, data, difficulty, nonce)

    @staticmethod
    def genesis():
        """
        Generates the genesis block
        """
        # return Block(
        #     GENESIS_DATA['timestamp'],
        #     GENESIS_DATA['last_hash'],
        #     GENESIS_DATA['hash'],
        #     GENESIS_DATA['data']            
        # )

        # This essentially does the same thing as the code above
        # The ** unpacks the data as individual arguments
        # and passes them as arguments
        return Block(**GENESIS_DATA)
        
def main():
    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'foo')
    print(f'block.py__name__: {__name__}')
    print(block)

if __name__ == '__main__':
    main()