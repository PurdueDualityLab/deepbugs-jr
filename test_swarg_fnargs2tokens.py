import json
import unittest
import swarg_fnargs2tokens
import os

TEST_AST = [
    {"id": 0, "type": "Program", "children": [1]},
    {"id": 1, "type": "ExpressionStatement", "children": [2]},
    {"id": 2, "type": "CallExpression", "children": [
        3, 6, 7]},  # Test case for base.callee(x,y)
    {"id": 3, "type": "MemberExpression", "children": [4, 5]},
    {"id": 4, "type": "Identifier", "value": "console"},
    {"id": 5, "type": "Property", "value": "log"},
    {"id": 6, "type": "Identifier", "value": "strVar"},
    {"id": 7, "type": "LiteralBoolean", "value": "true"},
    {"id": 8, "type": "CallExpression", "children": [
        9, 10, 11]},  # Test case for foo(x,y)
    {"id": 9, "type": "Identifier", "value": "fnName"},
    {"id": 10, "type": "LiteralBoolean", "value": "false"},
    {"id": 11, "type": "LiteralString", "value": "hello"},
    {"id": 12, "type": "CallExpression", "children": [
        13, 14, 15, 16]},  # Test case for 3-arg
    {"id": 13, "type": "Identifier", "value": "threeArgFnName"},
    {"id": 14, "type": "LiteralBoolean", "value": "false"},
    {"id": 15, "type": "LiteralString", "value": "hello"},
    {"id": 16, "type": "LiteralString", "value": "helloAgain"},
    {"id": 17, "type": "CallExpression", "children": [
        18, 19, 20]},  # Test case for invalid 2-arg
    {"id": 18, "type": "Identifier", "value": "invalid2ArgFnName"},
    {"id": 19, "type": "LiteralBoolean", "value": "false"},
    {"id": 20, "type": "CompletelyInvalid", "value": "hello"},
]


class TestSwargFnArgs2Tokens_GetArg(unittest.TestCase):
    def test_get_arg_identifier(self):
        self.assertEqual(swarg_fnargs2tokens.get_arg(
            6, TEST_AST), "ID:strVar")

    def test_get_arg_literal(self):
        self.assertEqual(swarg_fnargs2tokens.get_arg(7, TEST_AST), "LIT:true")

    def test_get_arg_none(self):
        self.assertEqual(swarg_fnargs2tokens.get_arg(0, TEST_AST), None)


class TestSwargFnArgs2Tokens_GetFnName(unittest.TestCase):
    def test_get_fn_name_property(self):
        self.assertEqual(swarg_fnargs2tokens.get_fn_name(
            5, TEST_AST), "ID:log")

    def test_get_fn_name_identifier(self):
        self.assertEqual(swarg_fnargs2tokens.get_fn_name(
            9, TEST_AST), "ID:fnName")

    def test_get_fn_name_memberexpression(self):  # checking base.callee()
        self.assertEqual(swarg_fnargs2tokens.get_fn_name(
            3, TEST_AST), "ID:log")

    def test_get_fn_name_none(self):  # checking base.callee()
        self.assertEqual(swarg_fnargs2tokens.get_fn_name(
            0, TEST_AST), None)


class TestSwargFnArgs2Tokens_GetAll2ArgFnCallsFromAst(unittest.TestCase):
    def test_get_all_2_arg_fn_calls_from_ast(self):
        self.assertListEqual(swarg_fnargs2tokens.get_all_2_arg_fn_calls_from_ast(TEST_AST), [
            {
                "fn_name": "ID:log",
                "arg1": "ID:strVar",
                "arg2": "LIT:true"
            },
            {
                "fn_name": "ID:fnName",
                "arg1": "LIT:false",
                "arg2": "LIT:hello"
            }
        ])


class TestSwargFnArgs2Tokens_GetAll2ArgFnCallsFromFile(unittest.TestCase):

    def test_get_all_2_arg_fn_calls_from_file(self):
        test_filename = "__test_swarg2fnargs_get_all_2_arg_fn_calls_from_file.txt" # Temporarily creates a file

        if test_filename in os.listdir("./"):
            raise Exception(
                "Test File '{0}' already exists.  Aborting test".format(test_filename))

        with open(test_filename, "w") as temp_json:
            json.dump(TEST_AST, temp_json)

        self.assertListEqual(swarg_fnargs2tokens.get_all_2_arg_fn_calls_from_file(test_filename), [
            {
                "fn_name": "ID:log",
                "arg1": "ID:strVar",
                "arg2": "LIT:true"
            },
            {
                "fn_name": "ID:fnName",
                "arg1": "LIT:false",
                "arg2": "LIT:hello"
            }
        ])

        os.remove(test_filename)
