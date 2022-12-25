import sys
import shrimp

if __name__ == "__main__":
    
    print("SHRIMP - RPN calculator")
    
    calc = shrimp.RPNcalc()
    for arg in sys.argv[1:]:
        calc.load(arg)
    
    print(calc.all())
