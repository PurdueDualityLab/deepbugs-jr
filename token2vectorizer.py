"""This module, when run as __main__, uses specified variables to produce two .npz files, one for train, one for eval
"""
from random import random
from typing import List, Set, Dict, Tuple, Optional, Union

from ast_token_extractor import *

import json
from gensim.models import Word2Vec

def train_word2vec(list_of_lists_of_tokens:list, save_filepath:str="word2vec.model"):
    """Trains a Word2Vec model from a list of tokens using CBOW with a window size of 200.
    The final vocabulary size is capped at the top 10,000 most popular tokens.
    Saves to disk.

    Args:
        list_of_lists_of_tokens (list): A list, where each entry is the list of tokens extracted from one source file AST.
        save_filepath (str, optional): Where to save the trained model. Defaults to "word2vec.model".

    Returns:
        The trained Word2Vec model.
    """
    model = Word2Vec(list_of_lists_of_tokens, window=200,workers=32,sg=0,max_final_vocab=10000)
    model.save(save_filepath)
    return model

def save_token2vec_vocabulary(model, save_filepath:str="our_trained_token2vec.json"):
    """Given a trained Word2Vec model, saves the vocabulary as a key-value dictionary, where
    each key is a token and the value is the corresponding vector. Saves to disk.

    Args:
        model: Trained Word2Vec model.
        save_filepath (str, optional): Where to save the vocabulary. Defaults to "our_trained_token2vec.json".
    """
    dicty = {}
    for key in iter(model.wv.key_to_index):
        if key is not None:
            dicty[key] = list(model.wv[key].astype(float))
        
    with open(save_filepath, "w") as jsony:
        json.dump(dicty, jsony)
         

if __name__ == "__main__":    
    # These files contain one AST (each AST is a list of JSON nodes) per line
    TRAIN_AST_PATH = "../Big, Ugly Data/programs_training.json"
    EVAL_AST_PATH = "../Big, Ugly Data/programs_eval.json"

    list_of_lists_of_tokens = get_tokens_from_corpus(EVAL_AST_PATH)
    train_word2vec(list_of_lists_of_tokens)

    model = Word2Vec.load("word2vec.model")
    print(model.wv["LIT:true"])
    print("Should be large difference", model.wv.similarity("LIT:true", "LIT:false"))
    print("Should be small difference", model.wv.similarity("LIT:true", "LIT:1"))

    save_token2vec_vocabulary(model)

