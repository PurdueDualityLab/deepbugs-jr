# Young Jin Jung
# Sun Mar  14 17:02:28 EST 2021
from collections import Counter


class TokenFrequency:
    """
    Token Frequency Class
    It can be initialized with pre-made list of tokens.
    Or  individual tokens can be fed.

    Attributes
    ----------
    token_list : list
        list of given tokens
    counter : Counter (dict)
        sorted dictionary that consists of {'token_name' : frequency}

    Methods
    -------
    add_token(token):
        append a token into the token_list and returns updated counter
    
    clear_list():
        clear token_list
    
    get_token_list():
        returns token_list
    
    get_frequency():
        returns Counter (dict) with current token_list

    def get_most_freq_token():
        returns the most frequently appeared token name (can be None)
    
    def get_most_freq_token_not_none():
        returns the most frequently appeared token name. 
        if none, returns the next most frequent non-None token name.
    """
    
    # can initialize the class with a list of tokens
    def __init__(self, tokenList=[]):
        self.token_list = tokenList
        self.counter = Counter(self.token_list)
        
    # add single token to the token list
    def add_token(self, token) -> Counter:
        self.token_list.append(token)
        self.counter = Counter(self.token_list)
        return self.counter

    def clear_list(self):
        self.token_list = []

    def get_token_list(self):
        return self.token_list

    def get_frequency(self):
        return self.counter

    def get_most_freq_token(self):
        return self.counter.most_common(1)[0][0]

    def get_most_freq_token_not_none(self):
        if self.counter.most_common(1)[0][0] != None: 
            return self.counter.most_common(1)[0][0]
        else:
            return self.counter.most_common(2)[1][0]

test_stock = [
    None,
    None,
    "ID:gTestfile",
    "LIT:regress-472450-04.js",
    None,
    "ID:BUGNUMBER",
    "LIT:472450",
    None,
    "ID:summary",
    "LIT:TM: Do not assert: StackBase(fp) + blockDepth == regs.sp",
    None,
    "ID:actual",
    "LIT:",
    None,
    "ID:expect",
    "LIT:",
    None,
    None,
    "ID:test",
    None,
    "ID:test",
    None,
    None,
    None,
    "ID:enterFunc",
    "LIT:test",
    None,
    None,
    "ID:printBugNumber",
    "ID:BUGNUMBER",
    None,
    None,
    "ID:printStatus",
    "ID:summary",
    None,
    None,
    "ID:jit",
    "LIT:true",
    None,
    None,
    "ID:__proto__",
    None,
    "ID:✖",
    None,
    "LIT:1",
    None,
    "ID:f",
    None,
    None,
    None,
    "ID:eval",
    "LIT:for (var y = 0; y < 1; ++y) { for each (let z in [null, function(){}, null, '', null, '', null]) { let x = 1, c = []; } }",
    None,
    None,
    "ID:f",
    None,
    None,
    "ID:jit",
    "LIT:false",
    None,
    None,
    "ID:reportCompare",
    "ID:expect",
    "ID:actual",
    "ID:summary",
    None,
    None,
    "ID:exitFunc",
    "LIT:test",
    None
]
tf = TokenFrequency(test_stock)
print(type(tf.get_most_freq_token()))
# print(tf.get_frequency())
# print(tf.get_most_freq_token())
# print(tf.get_most_freq_token_not_none())

tf.clear_list()
print(tf.add_token("a"))

# def token_frequency() -> list:
#     token_list = []
#     def append_char(token):
#         token_list.append(token)
#     def clear_list():
#         token_list = []

#     def get_token_list():
#         return token_list
#     def get_frequency():
#         c = Counter(token_list)
#         return c



# l = []
# # expecting that the token to be string
# def freq(token) -> list :
#     l.append(token)

#     c = Counter(l)
#     print(c.most_common())



# freq("a")
# freq("a")
# freq("b")

