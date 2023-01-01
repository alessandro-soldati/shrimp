import sys
import rpncalc

TEST_STRING = r'2e3 pi 0xAf7 0o777 0b1101 0B101 4 5+e*/ atan2 2,7 asdf -3.14E6.7'

if __name__ == "__main__":
    
    print("SHRIMP - RPN calculator")
    
    calc = rpncalc.RPNcalc()
    for arg in sys.argv[1:]:
        calc.load(arg)
    
    print(calc.all())
