import json
import unittest
from parse import *
import os

TEST_PROGRAM = '''
// This program is used to assist building up the basic grammar of C
/* comment */

// simple structures
//int some_int;
//float some_float;

// structures can be called like this
struct struct_name
{
    int int_e;
    float float_e;
};

//union union_name { int u_int; float u_float; };

// scope of structures
//struct bigger_struct { struct struct_name s_obj; };

//struct even_bigger_struct { struct bigger_struct bs_obj; int struct_leaf; };

//typedef struct even_bigger_struct ebs;

int main ()
{
    struct struct_name obj1;

    (obj1 . int_e) = (1 + 2);

    2.2;

    return 0;
} 

'''

TEST_AST = '''[{'id': 0, 'value': 'struct'}, {'id': 1, 'value': 'struct_name', 'name': 'struct_name'}, {'id': 2, 'value': '{'}, {'id': 3, 'value': 'int'}, {'id': 4, 'value': 'int_e', 'name': 'int_e'}, {'id': 5, 'value': ';'}, {'id': 6, 'value': 'float'}, {'id': 7, 'value': 'float_e', 'name': 'float_e'}, {'id': 8, 'value': ';'}, {'id': 9, 'value': '}'}, {'id': 10, 'value': ';'}, {'id': 11, 'value': 'int'}, {'id': 12, 'value': 'main'}, {'id': 13, 'value': '('}, {'id': 14, 'value': ')'}, {'id': 15, 'value': '{'}, {'id': 16, 'value': 'struct'}, {'id': 17, 'value': 'struct_name', 'name': 'struct_name'}, {'id': 18, 'value': 'obj1', 'name': 'obj1'}, {'id': 19, 'value': ';'}, {'id': 20, 'value': '('}, {'id': 21, 'value': 'obj1', 'name': 'obj1'}, {'id': 22, 'value': '.'}, {'id': 23, 'value': 'int_e', 'name': 'int_e'}, {'id': 24, 'value': ')'}, {'id': 25, 'value': '='}, {'id': 26, 'value': '('}, {'id': 27, 'value': '1'}, {'id': 28, 'value': '+'}, {'id': 29, 'value': '2'}, {'id': 30, 'value': ')'}, {'id': 31, 'value': ';'}, {'id': 32, 'value': '2.2'}, {'id': 33, 'value': ';'}, {'id': 34, 'value': 'return'}, {'id': 35, 'value': '0'}, {'id': 36, 'value': ';'}, {'id': 37, 'value': '}'}]'''

TEST_OUTPUT = """struct struct_name { int int_e ; float float_e ; } ; int main ( ) { struct struct_name obj1 ; ( obj1 . int_e ) = ( 1 + 2 ) ; 2.2 ; return 0 ; }""" 

class TestSwargFnArgs2Tokens_GetArg(unittest.TestCase):
    def test_get_arg_identifier(self):
        self.assertEqual(parse(TEST_PROGRAM), TEST_AST)

    def test_put_back_code(self) :
        self.assertEqual(code_generation(TEST_AST), TEST_OUTPUT)
            

