# part 1
"""
Given any AST node as a JSON string, extract the token and return a string. This token is what will get passed through Word2Vec to become a vector.

"""
from typing import List, Set, Dict, Tuple, Union, Callable

def ast2id_or_lit (node:dict) -> Union[str,None]:
    """pulls identifier or literal out of abstract syntax tree

    Args:
        python dictionary (json file)
       
    Returns:
        string of token LIT:name or ID:name or None 
    """
        
    # soft type check on input
    #import json
    #node == json.dumps(json.loads(node))

    # not sure why these are in the data
    ## acorn devs do what they want
    if node == 0 : return None

    # the json data we are actually tokenizing
    if (node["type"] == "VariableDeclarator" or
        node["type"] == "Identifier" or
        node["type"] == "Property" ) :
        return "ID:"+node["value"]
    
    # all javascript primitive literals seem to start with "literal"
    if node["type"][0:len("Literal")] == "Literal" :
        return "LIT:"+node["value"]

    # else
    return None


# oops, thought we were reading default acorn parsed output
## may still be useful 
def _acorn_json (node) :
    
    # common to all we are parsing
    if node["type"] != "ExpressionStatement" :
        return

    #If n is an identifier { "id":4, "type":"Identifier", "value":"console" }, return its name ID:console.
    if node["expression"]["type"] == "Identifier" : 
        return "ID:"+node["expression"]["value"]

    #If n is a literal { "id":6, "type":"Literal", "value":"hello" }, return a string representation of its value LIT:hello.
    if node["expression"]["type"] == "Literal" : 
        return "LIT:"+node["expression"]["raw"]

    #If n is a this expression, return LIT:this.
    if node["expression"]["type"] == "ThisExpression" : 
        return "LIT:"+"this"
    
    #If n is an update expression that increments or decrements x, return name (x).
    if node["expression"]["type"] == "UpdateExpression" :
        if (node["expression"]["operator"] == "++" or 
           node["expression"]["operator"] == "--") :
            return "ID:"+node["expression"]["argument"]["name"]

    # json is the same for member expressions . And []
    if node["expression"]["type"] == "MemberExpression" :

        #If n is a member expression base.prop that accesses a property, return name (prop).
        if node["expression"]["property"]["type"] == "Identifier" : 
            return "ID:"+node["expression"]["property"]["name"]

        #If n is a member expression base[k] that accesses an array element, return name (base).
        if node["expression"]["property"]["type"] == "Literal" : 
            return "ID:"+node["expression"]["property"]["raw"]

    
    #If n is a call expression base.callee (..), return name (callee).
    if node["expression"]["type"] == "CallExpression" :
        return "ID:"+node["expression"]["callee"]["name"]
        

    #For any other AST node n, do not extract its name.
    return 

# interface, sometimes referenced by these names
Token = ast2id_or_lit
token = ast2id_or_lit
