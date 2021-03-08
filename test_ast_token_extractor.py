import unittest
from ast_token_extractor import ast2id_or_lit 

    
# manually checked outs, regression style test
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

class TestTester(unittest.TestCase):
    def test_function(self):
        
        File = open("data/ast_for_prototyping/ast_0.json",'r')
        lines = File.readlines()
        File.close()
        file_str = ''
        for l in lines :
           file_str += l
        file_str.replace('\n','')
        nodes = eval(file_str) # json is legal python
        
        test_outputs = []
        for node in nodes :
            test_outputs.append(ast2id_or_lit(node))

        for i in range(len(test_stock)) :
            self.assertEqual(test_outputs[i], test_stock[i])
