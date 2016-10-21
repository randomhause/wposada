def sed(pattern, replace, source, dest):
    """Reads a source file and writes the destination file.

    In each line, replaces pattern with replace.

    pattern: string
    replace: string
    source: string filename
    dest: string filename
    
    open 2 files and for each line in each file if we see hey jude we replace it with something else.
    """
    f_in = open(source, 'r')
    f_out = open(dest, 'w')

    for line in f_in:
        new_line = line.replace(pattern, replace)
        f_out.write(new_line)
    
    f_in.close() #always close file


def main():
    pattern = 'Hey Jude', 'hey Jude', 'hey jude'
    replace = 'Hi Jerry'
    source = 'sed_tester.txt'
    dest = 'new_' + source
    sed(pattern, replace, source, dest)


if __name__ == '__main__':
    main()