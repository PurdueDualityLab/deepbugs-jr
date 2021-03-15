# part 3
"""
Using the function calls from Issue #10 and Word2Vec token-to-vector system from Issue #5, generate a full training/eval dataset for the JavaScript code corpus.

Something like:

positiveExample = Word2Vec(Token(fnName)) + Word2Vec(Token(arg1)) + Word2Vec(Token(arg2))
negativeExample = Word2Vec(Token(fnName)) + Word2Vec(Token(arg2)) + Word2Vec(Token(arg1))

Refer to section 2.2, 2.3, 2.4 of DeepBugs as source of this task.
"""

import os
from random import random

from ast_token_extractor import *
#from swarg_fnargs2tokens import get_all_2_arg_fn_calls_from_file 

positiveExamples_p = 0.8
data_path = "data/ast_for_protoyping/"

# interfaces/stubs
get_fun2s = lambda x : \
    list(x)
    #get_all_2_arg_fn_calls_from_file(x)
word2vec = lambda x :  \
    list(x)
    #Word2Vec(x)

#NOTE:Question: are these vectors simply additive? - checking
##              should output go into a folder?
def gen_good_bad_fun_args (data_path, positiveExamples_p = 0.8) :
    """make good bad function args

    Args:
        ast_foldername (str): filepath to the AST jsons 

    Returns:
        tuple[list[vectors]]: A tuple of (good, bad) list of function vectors
    """
    
    positiveExamples = []
    negativeExamples = []
    for File in os.listdir(data_path) :
        some_fn_calls = get_fun2s(File)
        
        for fn_call in some_fn_calls :
            if random() > positiveExamples_p :
                positiveExamples.append(
                    word2vec(fn_call["fn_name"]) +
                    word2vec(fn_call["arg1"]) +
                    word2vec(fn_call["arg2"]))
            else :
                negativeExamples.append(
                    word2vec(fn_call["fn_name"]) +
                    word2vec(fn_call["arg2"]) +
                    word2vec(fn_call["arg1"]))
    
        return (positiveExamples, negativeExamples)
         
