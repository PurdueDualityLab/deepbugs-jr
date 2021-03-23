import unittest
import token_freq


test_stock = [
    None,
    None,
    "ID:gTestfile",
    "LIT:regress-472450-04.js",
    None,
    "ID:BUGNUMBER",
    "LIT:472450",
    None,
    "ID:summary",
    "LIT:TM: Do not assert: StackBase(fp) + blockDepth == regs.sp",
    None,
    "ID:actual",
    "LIT:",
    None,
    "ID:expect",
    "LIT:",
    None,
    None,
    "ID:test",
    None,
    "ID:test",
    None,
    None,
    None,
    "ID:enterFunc",
    "LIT:test",
    None,
    None,
    "ID:printBugNumber",
    "ID:BUGNUMBER",
    None,
    None,
    "ID:printStatus",
    "ID:summary",
    None,
    None,
    "ID:jit",
    "LIT:true",
    None,
    None,
    "ID:__proto__",
    None,
    "ID:✖",
    None,
    "LIT:1",
    None,
    "ID:f",
    None,
    None,
    None,
    "ID:eval",
    "LIT:for (var y = 0; y < 1; ++y) { for each (let z in [null, function(){}, null, '', null, '', null]) { let x = 1, c = []; } }",
    None,
    None,
    "ID:f",
    None,
    None,
    "ID:jit",
    "LIT:false",
    None,
    None,
    "ID:reportCompare",
    "ID:expect",
    "ID:actual",
    "ID:summary",
    None,
    None,
    "ID:exitFunc",
    "LIT:test",
    None
]
        
assert_dict = {
    None: 35, 
    'ID:summary': 3, 
    'ID:BUGNUMBER': 2, 
    'ID:actual': 2, 
    'LIT:': 2, 
    'ID:expect': 2, 
    'ID:test': 2, 
    'LIT:test': 2, 
    'ID:jit': 2, 
    'ID:f': 2, 
    'ID:gTestfile': 1, 
    'LIT:regress-472450-04.js': 1, 
    'LIT:472450': 1, 
    'LIT:TM: Do not assert: StackBase(fp) + blockDepth == regs.sp': 1, 
    'ID:enterFunc': 1, 
    'ID:printBugNumber': 1, 
    'ID:printStatus': 1, 
    'LIT:true': 1, 
    'ID:__proto__': 1, 
    'ID:✖': 1, 
    'LIT:1': 1, 
    'ID:eval': 1, 
    "LIT:for (var y = 0; y < 1; ++y) { for each (let z in [null, function(){}, null, '', null, '', null]) { let x = 1, c = []; } }": 1, 
    'LIT:false': 1, 
    'ID:reportCompare': 1, 
    'ID:exitFunc': 1
}


class TestTester(unittest.TestCase):
    def test_function(self):

        tf = token_freq.TokenFrequency(test_stock)
        self.assertEqual(tf.get_frequency(), assert_dict)
        self.assertEqual(tf.get_most_freq_token(), None)
        self.assertEqual(tf.get_most_freq_token_not_none(), 'ID:summary')
        self.run(tf.clear_list())
        self.assertEqual(tf.add_token('a'), {'a':1})
        self.assertEqual(tf.add_token('a'), {'a':2})
        