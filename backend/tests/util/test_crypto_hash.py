import unittest
from backend.util_pkg._crypto_hash import crypto_hash

class TestHash(unittest.TestCase):

    def test_crypto_hash(self):
        # This should create the same hash with arguments data types in any order
        self.assertTrue(crypto_hash(1, [2], 'three') == crypto_hash([2], 'three', 1))
        self.assertEqual(first=crypto_hash('foo') , second='b2213295d564916f89a6a42455567c87c3f480fcd7a1c15e220f17d7169a790b', msg="NOT THE SAME")

        
if __name__ == '__main__':
    unittest.main()
