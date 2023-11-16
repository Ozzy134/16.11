def longest_word(file):
    with open(file) as f:
        ls = f.readlines()
    min_l = -1
    max_l_w = []
    for i in ls:
        if min_l < len(i):
            min_l = len(i)
            max_l_w = []

        if len(i) == min_l:
            max_l_w.append(i)

    return max_l_w

print(longest_word('text.txt'))