# a mini compiler, all in one file

#till python 3.9+ import typing
from typing import *

def get_file(filename) :
    File = ''
    with open(filename) as f:
        for l in f.readlines() :
            File += l

    return File

# boolean functions and facts
# {{{
# is fragment (non-look-ahead scan element)
is_frag = {}
def fragment(name :str,  expr :str) :
    "name of fragment, expression"
    
    def f(char :str)-> bool :
        return (char in expr)

    is_frag.update({ name : f })

    return f

# verbose, but literal
is_alpha_ = fragment('alpha_',
                    'abcdefhijklmnopqrstuvwxyz'
                    +'ABCDEFHIJKLMNOPQRSTUVWXYZ'
                    +'_')

is_alphanum_ = fragment('alphanum_',
                        'abcdefhijklmnopqrstuvwxyz'
                       +'ABCDEFHIJKLMNOPQRSTUVWXYZ'
                       +'0123456789'
                       +'_')

is_digit = fragment('digit',
                    '0123456789')
is_digitdot = fragment('digitdot',
                       '0123456789.')

def is_int(string:str) -> bool:
    "int literal default found in C-like languages"
    for ch in string :
        if not is_digit(ch) :
            return False
    return True

def is_decimal(string:str) -> bool:
    "float literal default found in C-like languages"
    if not is_digit(string[0]) :
        return False
    for ch in string :
        if not is_digitdot(ch) :
            return False
    return True

def is_c_identifier(string:str) -> bool:
    "is this string a C identifier"
    if not is_alpha_(string[0]) :
        return False
    for ch in string :
        if not is_alphanum_(ch) :
            return False
    return True


# from C17 standard
ckeywords = ['auto','break','case','char','const','continue','default',
        'do','double','else','enum','extern','float','for','goto','if',
        'inline','int','long','register','restrict','return','short',
        'signed','sizeof','static','struct','switch','typedef','union',
        'unsigned','void','volatile','while','_Alignas','_Alignof',
        '_Atomic','_Bool','_Complex','_Generic','_Imaginary','_Noreturn',
        '_Static_assert','_Thread_local']
ckeywords.append('bool') # some common but unlisted stuff
ckeywords.append('main') 
# }}}
   
# clean up code
# {{{
# 
def remove_single_comments(trigger) :
    " many comments are single char triggers"
    def f (string) :
        i = 0
        while i < len(string) :
            if string[i:i+len(trigger)] == trigger : # skipping single line 
                j = i
                while string[j] != '\n' and j < len(string):
                    j += 1
                string = string[0:i] + string[j:]
            i += 1
                
        return string
    return f

def remove_multi_comments(start,end) :
    
    def f (string) :
        i = 0
        while i < len(string) :
            if string[i:i+len(start)] == start : # skipping single line 
                j = i
                while string[j:j+len(end)] != end and j < len(string):
                    j += 1
                string = string[0:i] + string[j+2:]
            i += 1
        return string
    return f

def remove_extra_whitespace(string) :
    string = string.replace('\r','')
    string = string.replace('\n','')
    string = ' '.join(string.split())
    return string

# }}}

# tokenizing
# {{{
def str_to_tokens(string : str) -> list :
    """the design of this is to treat characters like tokens if they are not part of the token list"""

    def identifier(tokens, i) :
        "C lang identifiers"
        temp = ''
        if is_alpha_(string[i]) :
            temp += string[i]
            i += 1
            while is_alphanum_(string[i]) :
                temp += string[i]
                i += 1

            tokens.append(temp)

        return tokens, i 

    # NOTE: need all valid number types from C
    def number(tokens, i) :
        " integer, decimal  "
        temp = ''
        if is_digit(string[i]) :
            temp += string[i]
            i += 1
            while is_digitdot(string[i]) :
                temp += string[i]
                i += 1

            tokens.append(temp)

        return tokens, i 
        
    spaced_tokens : list = []

    # actual scanning part
    i = 0
    while i < len(string) :
        spaced_tokens, i = identifier(spaced_tokens, i)
        spaced_tokens, i = number(spaced_tokens, i)

        spaced_tokens.append(string[i])

        i += 1

    # remove space tokens
    tokens = []
    for e in spaced_tokens :
        if e != ' ' :
            tokens.append(e) 

    return tokens
# }}}

# parsing
# {{{
def id_tree(tokens:list) :
    "Add numbers, for referencing by other nodes"
    marked_tokens = []
    i = 0
    for e in tokens :
        marked_tokens.append({ 'id' : i, 'value': e })
        i += 1

    return marked_tokens

def name_tree(exclude_keywords) :
    "tag identifier, if it is not a keyword"
        
    def f (tokens) :
        
        for i in range(len(tokens)) :
            if ((not tokens[i]['value'] in exclude_keywords) and
               (is_c_identifier(tokens[i]['value']))) :
                tokens[i]['type'] = 'Identifier'
        
        return tokens
        
    return f
                
def c_literal_tree(tokens) : # note: not literally a tree
        
        for i in range(len(tokens)) :
            if (is_int(tokens[i]['value']) or 
                is_digit(tokens[i]['value'])) :
                tokens[i]['type'] = 'Literal'
        
        return tokens
        
# }}}


def clean_c(program) :
    f = remove_single_comments_c(program)
    f = remove_multi_comments_c(f)
    f = remove_extra_whitespace(f)
    return f

def parse_c(tokens) :
    "tokens to trees"

    t = str_to_tokens(tokens)
    t = id_tree(t)
    t = c_name_tree(t)
    t = c_literal_tree(t)
    #t = struct_tree(t)
    #t = union_tree(t)

    return t

def code_generation(trees) :
    string = ''
    for t in trees :
        string += t['value'] + ' '

    return string

def c_compiler(string) :
    "compile names from c to a json AST"
    s = remove_single_comments('//')(string)
    s = remove_multi_comments('/*','*/')(s)
    s = remove_extra_whitespace(s)

    t = str_to_tokens(s)
    t = id_tree(t)
    t = name_tree(ckeywords)(t)
    t = c_literal_tree(t)

    return t


# main
# {{{
#def main() :
import sys
f = get_file(sys.argv[1])

t = c_compiler(f)
print(t)

c = code_generation(t)

#main()
# }}}
