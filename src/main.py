import sys
import re

# Class definition
class RPNcalc:
    def __init__(self):
        self.stack = []
        
    def load(self, data):
        toks = re.split(r'(-?\d+(?:\.\d+)?[eE]?\d*)', data)
        for tok in toks:
            if tok is not None and tok != '':
                #if str.isnumeric():
                #    tok = (tok)
                self.stack.append(tok)
        
    def get(self):
        return self.stack.pop()
        
    def all(self):
        return self.stack
    
# Main program
print("SHRIMP - RPN calculator")

asd = RPNcalc()
for arg in sys.argv[1:]:
    asd.load(arg)

print(asd.all())
