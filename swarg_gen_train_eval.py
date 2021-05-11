"""This module, when run as __main__, uses specified variables to produce two .npz files, one for train, one for eval
"""
import os
from random import random
from typing import List, Set, Dict, Tuple, Optional, Union

from ast_token_extractor import *
from swarg_fnargs2tokens import get_all_2_arg_fn_calls_from_ast
import json
import numpy as np
from tqdm import tqdm

def gen_good_bad_fn_args (all_asts_filepath:str, token2vec_filepath: str, save_to_filepath:str="") -> Tuple[List,List]:
    """Given a file that has one AST per line, extracts all function calls and makes switch-arg training data.

    Optionally saves to a ".npz" file with keys "data_x" and "labels_y".

    Args:
        all_asts_filepath (str): Path to the file with one AST per line
        token2vec_filepath (str): Path to the JSON file that is a lookup table for all "ID:foo" and "LIT:foo" tokens
        save_to_filepath (str, optional): Path to the .npz file to save data to. Defaults to "".

    Returns:
        Tuple[List,List]: (Data, Labels). Both Data and Labels are numpy arrays of the same length, where Labels[i] is 1 for positive, 0 for negative
    """
    
    positive_examples = []
    negative_examples = []

    with open(token2vec_filepath) as token2vec_fp:
        token2vec = json.load(token2vec_fp)

    with open(all_asts_filepath, errors="ignore") as all_asts_fp:
        for ast_line in tqdm(all_asts_fp): # Iterate over all lines in file

            ast = json.loads(ast_line) # Each line contains a new AST
            fn_calls = get_all_2_arg_fn_calls_from_ast(ast) # A list of {"fn_name": "ID:foo", "arg1": "LIT:true", "arg2": "LIT:false"}
            
            for fn_call in fn_calls:
                try:
                    # Lookup the vector embedding for all three tokens
                    fn_name_vec = np.array(token2vec[fn_call["fn_name"]])
                    arg1_name_vec = np.array(token2vec[fn_call["arg1"]])
                    arg2_name_vec = np.array(token2vec[fn_call["arg2"]])

                    # Make one good example, and one bad one with arg1 and arg2 switched
                    positive_example = np.concatenate([fn_name_vec, arg1_name_vec, arg2_name_vec])
                    negative_example = np.concatenate([fn_name_vec, arg2_name_vec, arg1_name_vec])

                    positive_examples.append(positive_example)
                    negative_examples.append(negative_example)
                except:
                    pass


    # Everything should be numpy arrays
    positive_labels = np.ones(len(positive_examples))
    positive_examples = np.array(positive_examples)
    negative_labels = np.zeros(len(negative_examples))
    negative_examples = np.array(negative_examples)

    # first half is positive, second half is negative
    data_x = np.concatenate([positive_examples, negative_examples])
    labels_y = np.concatenate([positive_labels, negative_labels])

    # Save using keys "data_x" and "labels_y"
    if save_to_filepath != "":
        #print("data_x: "+str(data_x.shape))
        #print("data_y: "+str(labels_y.shape))
        np.savez(save_to_filepath, data_x=data_x, labels_y=labels_y)
    
    return data_x, labels_y
         

if __name__ == "__main__":

    # NOTE: Took about 13 minutes.

    # This json file is in the format {"LIT:something": [...vector], "ID:someotherthing": [...vector], ...}
    TOKEN2VEC_PATH = "our_trained_token2vec.json"
    
    # These files contain one AST (each AST is a list of JSON nodes) per line
    TRAIN_AST_PATH = "../programs_training.json"
    EVAL_AST_PATH = "../programs_eval.json"

    # These .npz files can be opened using np.load(). Keys are data_x and labels_y
    # See https://www.tensorflow.org/tutorials/load_data/numpy for easy walkthrough on using w Keras
    OUTPUT_TRAIN_PATH = "../swarg_training_data.npz"
    OUTPUT_EVAL_PATH = "../swarg_eval_data.npz"

    # Save the two .npz files
    #gen_good_bad_fn_args(TRAIN_AST_PATH, TOKEN2VEC_PATH, OUTPUT_TRAIN_PATH)
    gen_good_bad_fn_args(EVAL_AST_PATH, TOKEN2VEC_PATH, OUTPUT_EVAL_PATH)
