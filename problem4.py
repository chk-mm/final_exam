def count_duplicate(str):
    dict = {}
    tmp = str.lower()
    for x in tmp:
        if x in dict:
            dict[x] += 1
        else:
            dict[x] = 1
    if sum(dict.values()) == len(dict):
        print('No characters repeats more than once')
    else:
        for z in dict:
            # print(dict[z],z)
            if dict[z] > 1:
                print(z,' occurs ',dict[z],' times')
    return 0



count_duplicate('aA11b')
count_duplicate('abcde')
count_duplicate('aabBcde')
