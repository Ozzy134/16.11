def read_end(lines, file):
    with open(file) as f:
        ls = f.readlines()
    for i in range(len(ls) - lines, len(ls)):
        print(ls[i], end='')

read_end(3, 'artikle.txt')