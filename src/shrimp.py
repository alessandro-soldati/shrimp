# -*- coding: utf-8 -*-
"""
Created on Sun Dec 25 23:10:13 2022

@author: alex8
"""

import re

# Class definition
class RPNcalc:
    def __init__(self):
        self.stack = []
        
    def load(self, data):
        # Whitespace splitting guaranteed only if implemented outside!
        toks = re.split(r'(-?\d+(?:\.\d+)?(?:[eE]-?\d)?)', data)
        print(toks)
        for tok in toks:
            if tok is not None and tok != '':
                self.stack.append(tok)
        
    def get(self):
        return self.stack.pop()
        
    def all(self):
        return self.stack
