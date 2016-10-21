import random
import string


def process_file(filename, skip_header):
    """Makes a histogram that contains the words from a file.

    filename: string
    skip_header: boolean, whether to skip the Gutenberg header

    returns: map from each word to the number of times it appears.
    key = words
    value = how many times it comes up 
    """
    hist = {} #list
    fp = open(filename)

    # if skip_header:
    #     skip_gutenberg_header(fp)

    for line in fp:
        if line.startswith('*** END OF THIS PROJECT'):
            break
        # INSERT CODE BELOW
        for word in line.split():  #line.split() splits words
            word = word.lower()
            hist[word] = hist.get(word, 0) + 1
        

    return hist

    
print(process_file('test_file.txt', skip_header=False))