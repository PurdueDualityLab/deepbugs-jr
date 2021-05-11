from ast_token_extractor import ast2id_or_lit
from gensim.models import Word2Vec
from gensim.test.utils import common_texts
import json
import time
import math
import sys

def convert_to_ast(lines):
    file_str = ''
        
    for l in lines:
        file_str += l
    file_str.replace('\n', '')
    nodes = eval(file_str)

    tokens = []
    for node in nodes:
        tokens.append(ast2id_or_lit(node))

    return tokens


def filter_token_list(tokens):
    a = tokens[:]
    tokens = []
    for l in a :
        if l :
            tokens.append([l])
    return tokens


def main():
"""
    tokens = [] 
    for i in range(10):
        File = open(f"demo_data/150k_training.json",'r', encoding="latin1")
        lines = File.readlines()
        File.close()
        tokens += convert_to_ast(lines)
    # Clean out None from list
    filter_token_list(tokens)


    # Filter out None, and put each token in a list
    a = tokens[:]
    tokens = []
    for l in a :
        if l :
            tokens.append([l])
        
    #print(type(common_texts))
    #print(tokens[0:50])
    #model = Word2Vec(sentences=tokens, min_count=3, window=5, vector_size=150, workers=40, epochs=15, alpha=0.1, sg=0)
    model = Word2Vec.load("word2vec.model")
    #print(help(model))
    #print(model.wv.key_to_index)
    #print(help(model.wv.key_to_index))

    timestamp = math.floor(time.time() * 1000)
    model.save("embedding_model_" + str(timestamp))

    # Save vectors for to file 
    token_to_vector = dict()
    for token in model.wv.key_to_index : 
        if token != None and (token.startswith("ID:") or token.startswith("LIT:")):
            #print(token)
            vector = model.wv.get_vector(token).tolist() # model is no longer easily subscriptable
            token_to_vector[token] = vector
    token_to_vector_file_name = "token_to_vector_" + str(timestamp) + ".json"
    with open(token_to_vector_file_name, "w") as file:
        json.dump(token_to_vector, file, sort_keys=True, indent=4)
"""


if __name__ == "__main__":
    main()
    #a=1
