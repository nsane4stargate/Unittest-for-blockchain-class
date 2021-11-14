import unittest
from backend.tests.blockchain.test_block import TestBlock
from backend.tests.blockchain.test_blockchain import TestBlockchain
from backend.tests.util.test_crypto_hash import TestHash

class TestSuite(unittest.TestCase):
    # Add the imported unittest classes to a list to test
    # in a suite.
    test_class_list = [TestBlock, TestBlockchain, TestHash]

    for testclass in test_class_list:
        suite = unittest.TestLoader().loadTestsFromTestCase(testclass)
        unittest.TextTestRunner(verbosity=1).run(suite)
    
    