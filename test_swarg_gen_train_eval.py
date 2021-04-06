# I think the schema of this test should be, at least:
# - to check pos != neg examples
# - check one page manually

import unittest
import os
import swarg_gen_train_eval
import json
import numpy as np


SMOKE_TEST_AST = [
    {"id": 0, "type": "Program", "children": [1]},
    {"id": 1, "type": "ExpressionStatement", "children": [2]},
    {"id": 2, "type": "CallExpression", "children": [3, 6, 7]},  # base.callee(x,y)
    {"id": 3, "type": "MemberExpression", "children": [4, 5]},
    {"id": 4, "type": "Identifier", "value": "console"},
    {"id": 5, "type": "Property", "value": "log"},
    {"id": 6, "type": "Identifier", "value": "strVar"},
    {"id": 7, "type": "LiteralBoolean", "value": "true"},
    {"id": 8, "type": "CallExpression", "children": [9, 10, 11]},  # foo(x,y)
    {"id": 9, "type": "Identifier", "value": "fnName"},
    {"id": 10, "type": "LiteralBoolean", "value": "false"},
    {"id": 11, "type": "LiteralString", "value": "hello"},
    {"id": 12, "type": "CallExpression", "children": [13, 14, 15, 16]},  # 3-arg
    {"id": 13, "type": "Identifier", "value": "threeArgFnName"},
    {"id": 14, "type": "LiteralBoolean", "value": "false"},
    {"id": 15, "type": "LiteralString", "value": "hello"},
    {"id": 16, "type": "LiteralString", "value": "helloAgain"},
    {"id": 17, "type": "CallExpression", "children": [18, 19, 20]},  # invalid 2-arg
    {"id": 18, "type": "Identifier", "value": "invalid2ArgFnName"},
    {"id": 19, "type": "LiteralBoolean", "value": "false"},
    {"id": 20, "type": "CompletelyInvalid", "value": "hello"},
]

SMOKE_TEST_TOKEN2VEC = {
    "ID:log": [1, 2, 3],
    "ID:strVar": [4, 5, 6],
    "LIT:true": [7, 8, 9],
    "ID:fnName": [10, 11, 12],
    "LIT:false": [13, 14, 15],
    "LIT:hello": [16, 17, 18]
}

class TestSwargGenTrainEval_GenGoodBadFnArgs(unittest.TestCase):
    def test_smoke_test(self):
        """Just makes sure everything seems to be OK; generates data and labels for a super simple dataset
        """
        test_ast_filename = "__test_ast_file_swarg_gen_train_eval.txt" # Temporarily creates a file
        test_token2vec_filename = "__test_token2vec_file_swarg_gen_train_eval.txt" # Temporarily creates a file
        test_output_filename = "__test_output_file_swarg_gen_train_eval.npz"

        if test_ast_filename in os.listdir("./"):
            raise Exception("Test File '{0}' already exists.  Aborting test".format(test_ast_filename))
        if test_token2vec_filename in os.listdir("./"):
            raise Exception("Test File '{0}' already exists.  Aborting test".format(test_token2vec_filename))
        if test_output_filename in os.listdir("./"):
            raise Exception("Test File '{0}' already exists.  Aborting test".format(test_output_filename))

        with open(test_ast_filename, "w") as temp_json:
            json.dump(SMOKE_TEST_AST, temp_json)

        with open(test_token2vec_filename, "w") as temp_json:
            json.dump(SMOKE_TEST_TOKEN2VEC, temp_json)
        
        data_x, labels_y = swarg_gen_train_eval.gen_good_bad_fn_args(test_ast_filename, test_token2vec_filename, test_output_filename)

        # Make sure vectors are correctly generated
        self.assertListEqual(data_x.tolist(), [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [1, 2, 3, 7, 8, 9, 4, 5, 6], [10, 11, 12, 16, 17, 18, 13, 14, 15]])
        self.assertListEqual(labels_y.tolist(), [1, 1, 0, 0])

        # Make sure file saved OK
        with np.load(test_output_filename) as npz:
            self.assertListEqual(npz["data_x"].tolist(), [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12, 13, 14, 15, 16, 17, 18], [1, 2, 3, 7, 8, 9, 4, 5, 6], [10, 11, 12, 16, 17, 18, 13, 14, 15]])
            self.assertListEqual(npz["labels_y"].tolist(), [1, 1, 0, 0])
        os.remove(test_ast_filename)
        os.remove(test_token2vec_filename)
        os.remove(test_output_filename)

