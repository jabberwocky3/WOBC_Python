import sys

input_file = open(sys.argv[1], 'r').read()

def common_letter(input_file):
    ''' Determines the most common non-whitespace letter in an input file '''
    charset = ''.join(sorted(input_file.lower()))
    nospace = charset.replace(" ", "")
    maxcount = 0
    maxchar = None
    for item in charset.lower():
        charcount = nospace.count(item)
        if charcount > maxcount:
            maxcount = charcount
            maxchar = item
    print(f"{maxchar} is the most common letter. It occurs {maxcount} times.")

def percentage_the(input_file):
    ''' Determines the percetange that the word 'the' appears in an input file'''
    the_count = 0
    words = input_file.lower()
    words = words.split()
    word_count = len(words)

    for i in words:
        if (i == 'the'):
            the_count = the_count + 1

    the_percent = ((the_count / word_count)*100)
    print(int(the_percent)) # rounds down to the closest integer

def first_ten(input_file):
    '''Writes the first ten words of an input file to a new output file'''
    words2 = input_file.split()
    ten = words2[0:10]
    ten = ' '.join(ten)

    newfile = open('challenge8_output.txt', 'w+')
    newfile.write(ten)

if __name__ == "__main__":
    common_letter(input_file)
    percentage_the(input_file)
    first_ten(input_file)
