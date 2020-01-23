def printing():
    print("Octal     Decimal     Hex     Bin     Char")
    print("------------------------------------------")
    for i in range(63,73):
        octal = oct(i)
        hexidecimal = hex(i)
        binary = bin(i)
        character = chr(i)
        my_format = '{0:#5o}{0:>12}{0:8x}{0:>10b}{0:5c}'
        #print("{0:>5s}       {1}        {2}     {3:>5s}     {4}".format(octal, str(i), hexidecimal, str(binary), str(character)))
        print(f'{i:#5o}{i:>12}{i:8x}{i:>10b}{i:8c}')
if __name__ == "__main__":
    printing()
