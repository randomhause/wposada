fin = open('words1.txt')
line = repr(fin.readline())

def word_dict_txt():
    word_dict = dict()
    for line in fin:
        word = line.strip()
        word_dict[word] = word
    return word_dict
