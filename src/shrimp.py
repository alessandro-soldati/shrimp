import sys
import rpncalc

TEST_REAL = '2 3*5+ 3/'
TEST_TRIG = 'pi 2/ sin'
TEST_STRING = '0x47 2e3 1.3e17 pi \t -1.2e-1 0xAf7 0o777 0b1101 -0B101 4 5+e*/ atan2 2,7 asdf -3.14E+6.7'

if __name__ == "__main__":
    
    print("SHRIMP - RPN calculator")
    
    calc = rpncalc.RPNcalc()
    for arg in sys.argv[1:]:
        calc.load(arg)
    
    print(calc.get_all())
