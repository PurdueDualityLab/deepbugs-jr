from ast_token_extractor import ast2id_or_lit
from gensim.models import Word2Vec
import json
import time
import math
import sys

# from HyperParameters import name_embedding_size

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

def main():
    tokens = [] 
    for i in range(10):
        File = open(f"data/ast_for_prototyping/ast_{i}.json",'r')
        lines = File.readlines()
        File.close()
        tokens.append(convert_to_ast(lines))
        print(tokens[:])

    model = Word2Vec(tokens, min_count=3, window=5, size=150, workers=40, iter=15, alpha=0.1, sg=0)

    timestamp = math.floor(time.time() * 1000)
    model.save("embedding_model_" + str(timestamp))

    token_to_vector = dict()
    for token in model.wv.vocab:
        if token.startswith("ID:") or token.startswith("LIT:"):
            vector = model[token].tolist
            token_to_vector[token] = vector
    token_to_vector_file_name = "token_to_vector_" + str(timestamp) + ".json"
    with open(token_to_vector_file_name, "w") as file:
        json.dump(token_to_vector, file, sort_keys=True, indent=4)



if __name__ == "__main__":
    main()
