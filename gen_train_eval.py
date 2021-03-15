# part 3

import os
from random import random

from ast_token_extractor import *
from swarg_fnargs2tokens import get_all_2_arg_fn_calls_from_file as get_funs

positiveExample_p = 0.8

data_path = "data/ast_for_protoyping/"
lamdba word2vec = x : Word2Vec(x)

#Question: are these vectors simply additive?
def gen_good_bad_fun_args (data_path) :
    """make good bad function args

    Args:
        ast_foldername (str): filepath to the AST jsons 

    Returns:
        tuple[list[vectors]]: A tuple of (good, bad) list of function vectors
    """
    
    positiveExample = []
    negativeExample = []
    for File in os.listdir(data_path) :
        some_fn_calls = get_funs(File)
        
        for fn_call in some_fn_calls :
            if random() > positiveExample_p :
                positiveExample.append(
                    word2vec(fn_call["fn_name"]) +
                    word2vec(fn_call["arg1"]) +
                    word2vec(fn_call["arg2"]))
            else :
                negativeExample.append(
                    word2vec(fn_call["fn_name"]) +
                    word2vec(fn_call["arg2"]) +
                    word2vec(fn_call["arg1"]))
    
        return (positiveExample, negativeExample)
         
