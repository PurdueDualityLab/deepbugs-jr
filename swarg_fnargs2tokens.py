import json
from ast_token_extractor import ast2id_or_lit

def get_all_2_arg_fn_calls_from_file(ast_filename:str)->list[dict]:
    """Given a filename, parses the AST JSON, returns a list of 2-argument function calls with their tokens

    Args:
        ast_filename (str): filepath to the AST json

    Returns:
        list[dict]: A list of {"fn_name": "ID:foo", "arg1": "LIT:true", "arg2": "ID:varName"}
    """
    with open(ast_filename) as ast_file:
        ast = json.load(ast_file)
    
    return get_all_2_arg_fn_calls_from_ast(ast)

def get_all_2_arg_fn_calls_from_ast(ast: list[dict])->list[dict]:
    """Given an AST, returns a list of 2-argument function calls in the tree with their tokens

    Args:
        ast (list[dict]): A list of AST nodes for the entire file

    Returns:
        list[dict]: A list of {"fn_name": "ID:foo", "arg1": "LIT:true", "arg2": "ID:varName"}
    """
    all_fn_calls = []

    for node in ast:
        if node["type"] == "CallExpression":
            if len(node["children"]) == 3: # fn_name, arg1, arg2
                fn_name = get_fn_name(node["children"][0], ast)
                arg1 = get_arg(node["childen"][1], ast)
                arg2 = get_arg(node["childen"][2], ast)

                # Ignore this one, fn call should be yeeted
                if fn_name is None or arg1 is None or arg2 is None:
                    continue

                fn_call = {
                    "fn_name": fn_name,
                    "arg1": arg1,
                    "arg2": arg2
                }

                all_fn_calls.append(fn_call)
    
    return all_fn_calls

def get_fn_name(node_id: int, ast: list[dict])->str:
    """Given the first child of a CallExpression node, figures out the function token (e.g. "ID:fnName")

    Args:
        node_id (int): The numerical ID of the AST node
        ast (list[dict]): The list of AST nodes for the entire file

    Returns:
        str: The function name token (e.g. "ID:fnName")
    """

    if ast[node_id]["type"] == "Identifier": # e.g. "foo" from foo(arg1, arg2)
        return ast2id_or_lit(ast[node_id])
    
    if ast[node_id]["type"] == "Property": # e.g. "callee" from base.callee(arg1, arg2)
        return ast2id_or_lit(ast[node_id])
    
    if ast[node_id]["type"] == "MemberExpression": # e.g. "base, callee" from base.callee(arg1, arg2)
        return get_fn_name(ast[node_id]["children"][1])

    return None # If you got here, this node should be yeeted

def get_arg(node_id: int, ast: list[dict])->str:
    """Given the second or third child of a CallExpression node, figures out the argument token (e.g. "ID:varName" or "LIT:true")

    Args:
        node_id (int): The numerical ID of the AST node
        ast (list[dict]): The list of AST nodes for the entire file

    Returns:
        str: The argument token (e.g. "ID:varName" or "LIT:true")
    """
    if ast[node_id]["type"] == "Identifier": # e.g. "arg1" or "arg2" from foo(arg1, arg2)
        return ast2id_or_lit(ast[node_id])
    
    if ast[node_id]["type"].startswith("Literal"): # e.g. LiteralBoolean, LiteralString, etc.
        return ast2id_or_lit(ast[node_id])
    
    return None # If you got here, this node should be yeeted