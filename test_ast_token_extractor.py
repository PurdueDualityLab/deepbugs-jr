import unittest
from ast_token_extractor import test

class TestTester(unittest.TestCase):
    def test_function(self):
        self.assertAlmostEqual(test(3.14), 3.14)
        self.assertAlmostEqual(test(0), 0)
        self.assertEqual(test("Hello World"), "Hello World")
        self.assertEqual(test(True), True)
