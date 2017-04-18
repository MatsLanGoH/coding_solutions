# store input
pEmojis = dict()

# read input
try:
    while True:
        line = input().split(',')
        pEmojis[line[0]] = line[1:]
        """ store user and emojis
                                     note: for this task, we could simply store len(set(line[1:]))
                                         instead, since we only want the number of unique emoji
                                    """
except:
    pass

# output array, sorted by length of sets.
finally:
    for k in sorted(pEmojis, key=lambda k: len(set(pEmojis[k])), reverse=True):
        print('{},{}'.format(k,len(set(pEmojis[k]))))
