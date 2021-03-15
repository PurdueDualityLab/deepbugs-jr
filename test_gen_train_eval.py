# I think the schema of this test should be, at least:
# - to check pos != neg examples
# - check one page manually

import unittest
import gen_train_eval as gte

identity = lambda x : x

#NOTE: this test covers nothing. 
class TestTester(unittest.TestCase):
    def test_function(self):
        self.assertEqual(identity(True), True)
