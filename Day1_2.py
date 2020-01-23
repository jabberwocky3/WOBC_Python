import sys
arg1 = float(sys.argv[1])

def conversion(argv):
    '''Converts USD to British Pounds'''
    pounds = float(arg1*0.77)
    print(f"{arg1} US dollars converts to {pounds} British Pounds.")

conversion(arg1)
