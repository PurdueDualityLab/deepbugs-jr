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
