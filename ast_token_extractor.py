# Jordan Winkler
# Mon Mar  8 05:02:28 EST 2021

# always good to check
test = lambda x : x

def ast2id_or_lit (node) :
    """ast2id_or_lit
        pulls identifier or literal out of abstract syntax tree
    """
    # soft type check on input
    import json
    node == json.dumps(json.loads(node))


    # common to all we are parsing
    if node["type"] == "ExpressionStatement" :
        return node

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
    return node

