import sys
arg1 = float(sys.argv[1])

def conversion(arg1=1, rate = 0.77):
    pounds = float(arg1*rate)
    print(f"{arg1} US dollars converts to {pounds} British Pounds.")

conversion(arg1)
