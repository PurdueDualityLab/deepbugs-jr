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
is_frag = {}
def fragment(name :str,  expr :str) :
    "name of fragment, expression"
    
    def f(char :str)-> bool :
        return (char in expr)

    is_frag.update({ name : f })

    return f

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

def is_int(string) -> bool:
    for ch in string :
        if not is_digit(ch) :
            return False
    return True

def is_decimal(string) -> bool:
    if not is_digit(string[0]) :
        return False
    for ch in string :
        if not is_digitdot(ch) :
            return False
    return True

def is_c_identifier(string) -> bool:
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
def remove_single_comments_c(string) :
    """ remove C comments
    """
    i = 0
    while i < len(string) :
        if string[i:i+2] == '//' : # skipping single line 
            j = i
            while string[j] != '\n' and j < len(string):
                j += 1
            string = string[0:i] + string[j:]
        i += 1
            
    return string

def remove_multi_comments_c(string) :
    i = 0
    while i < len(string) :
        if string[i:i+2] == '/*' : # skipping single line 
            j = i
            while string[j:j+2] != '*/' and j < len(string):
                j += 1
            string = string[0:i] + string[j+2:]
        i += 1
    return string

def remove_extra_whitespace(string) :
    string = string.replace('\r','')
    string = string.replace('\n','')
    string = ' '.join(string.split())
    return string
# }}}

# tokenizing
# {{{
def str_to_tokens(string : str) -> list :
    "the design of this is to treat characters like tokens if they are not part of the token list"

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
#
#
def id_tree(tokens:list) :
    "Add numbers "
    marked_tokens = []
    i = 0
    for e in tokens :
        marked_tokens.append({ 'id' : i, 'value': e })
        i += 1

    return marked_tokens

def name_tree(exclude_keywords) :

    def f (tokens) :
        
        for i in range(len(tokens)) :
            if ((not tokens[i]['value'] in exclude_keywords) and
               (is_c_identifier(tokens[i]['value']))) :
                tokens[i]['name'] = tokens[i]['value']
        
        return tokens
        
    return f
                
c_name_tree = name_tree(ckeywords)

def typedef_tree(type_name) :
    
    def f (tokens) :
        # iterate over syntax
        for i in range(len(tokens[:-len('si{};')])) :
            # grammar spec
            if (type_name in tokens[i  ]['value'] and
                '{'       in tokens[i+2]['value']) :

                # need to copy only on complete grammar
                temp = {}
                temp['type'] = type_name
                #tokens[i]['type'] = type_name 

                # body
                tempbody = []
                #tokens[i]['children'] = []
                j = i+3
                while  j < len(tokens) and tokens[j]['value'] != '}' :
                    tokens[i]['children'].append(tokens[j]['id'])
                    j += 1

        return tokens
    return f
       

## make more syntax trees
#tree = {}
## primitives
#for prime in ['char','int','float','double','_Bool','struct','union'] :
#    tree.update({ prime : typeinit_tree(prime) })
## declaring stuff
union_tree = typedef_tree('union')
struct_tree = typedef_tree('struct')
#dot_tree = relation_tree('.')
#comma_tree = relation_tree(',')
#plus_tree = relation_tree('+')
#assign_tree = relation_tree('=')

def parse(tokens) :
    "tokens to trees"

    t = str_to_tokens(tokens)
    t = id_tree(t)
    t = c_name_tree(t)
    #t = struct_tree(t)
    #t = union_tree(t)

    return t
# }}}

# code generation
def code_generation(trees) :
    string = ''
    for t in trees :
        string += t['value'] + ' '

    return string

# main
# {{{
#def main() :
import sys
f = get_file(sys.argv[1])

## scanning stuff
def clean_c(program) :
    f = remove_single_comments_c(program)
    f = remove_multi_comments_c(f)
    f = remove_extra_whitespace(f)
    return f

f = clean_c(f)
print('tokens (f)\n'+ f+'\n')

## parsing stuff
t = parse(f)
print('trees (t)')
print(t)
#for b in t : print(b)

# symbol table
#st = symbol_table(t)
#print('symbol table (st)')
#for s in st : print(s, st[s])

## semantic actions
#print('semantic actions (t)')
#t = struct_copy(t,st)
#print(t)

# code generation
#print('code (c)')
c = code_generation(t)
print(c)

#main()
# }}}
