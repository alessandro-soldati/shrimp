# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 23:10:13 2022

@author: alex8
"""

import re

TEST_STRING = r'2e3 pi 0xAf7 0777 0b1101 0B101 4 5+e*/ atan2 2,7 asdf -3.14E6.7'

# Class definition
class RPNcalc:
    def __init__(self):
        self.stack = []
        
    def load(self, data):
        re_tok_str = (
            r'0[xX][0-9a-fA-F]+|' # base 16, integer only
            r'0[0-7]+|' # base 8, integer only
            r'0[bB][01]+|' # base 2, integer only
            r'-?\d+(?:\.\d+)?(?:[eE]-?\d)?|' # base 10, possibly exp notation
            r'[\+\-\*/]|' # common operators
            r'\w+' # remaining identifiers
            )
        toks = re.findall(re_tok_str, data)
        for tok in toks:
            self.stack.append(tok)
        
    def get(self):
        return self.stack.pop()
        
    def all(self):
        return self.stack
