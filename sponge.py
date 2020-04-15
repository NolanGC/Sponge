import random

def mnemonic(s):
    with open('Words/nouns.txt', 'r') as fin:
        nouns = fin.read().splitlines()
    with open('Words/verbs.txt', 'r') as fin:
        verbs = fin.read().splitlines()
    with open('Words/adjectives.txt', 'r') as fin:
        adjectives = fin.read().splitlines()
    data = [s[0].lower() for s in s.split(' ')]
    device = list()
    pattern = list()
    style = 1
    # style 1 = noun verb adj(...) noun
    if(style == 1):
        pattern.append('n')
        pattern.append('v')
        for i in range(len(data) - 3):
            pattern.append('a')
        pattern.append('n')

    index = 0
    for i in range(len(data)):
        if(pattern[index] == 'n'):
            pool = [noun + 's' if noun[len(noun)-1] != 's' else noun for noun in nouns if noun.lower().startswith(data[i].lower())] 
        elif(pattern[index] == 'v'):
            pool = [verb for verb in verbs if verb.lower().startswith(data[i].lower())] 
        elif(pattern[index] == 'a'):
            pool = [adj for adj in adjectives if adj.lower().startswith(data[i].lower())] 
        device.append(pool[random.randint(0, len(pool)-1)])
        index += 1 

    out = ''
    for w in device:
        out += w + ' '
    return out