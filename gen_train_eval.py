from ast_token_extractor import *

# stub/interface set
Word2Vec = lambda x : 1
Token = lambda x : ast2id_or_lit(x)

fnName = 0
arg1 = 1
arg2 = 2


# would be simpler to pull from the function block
positiveExample = #lambda fnName : 
    Word2Vec(Token(fnName)) + Word2Vec(Token(arg1)) + Word2Vec(Token(arg2))
negativeExample = #lambda fnName : 
    Word2Vec(Token(fnName)) + Word2Vec(Token(arg2)) + Word2Vec(Token(arg1))


