import random
from os.path import dirname, join
def mnemonic(s):
    working = dirname(__file__)
    fp = join(working, './Words/nouns.txt')
    with open(fp, 'r') as fin:
        nouns = fin.read().splitlines()
    fp = join(working, './Words/verbs.txt')
    with open(fp, 'r') as fin:
        verbs = fin.read().splitlines()
    fp = join(working, './Words/adjectives.txt')
    with open(fp, 'r') as fin:
        adjectives = fin.read().splitlines()
    fp = join(working, './Words/adverbs.txt')
    with open(fp, 'r') as fin:
        adverbs = fin.read().splitlines()
    data = [s[0].lower() for s in s.split(' ')]
    device = list()
    pattern = list()
    structure = [0,0,0,0,0,'anxvn','aanxvn','aanxvan','aanxvaan','aanxxvaan','aaanxxvaan']
    pattern = structure[len(data)]
    index = 0
    for i in range(len(data)):
        if(pattern[index] == 'n'):
            pool = [noun for noun in nouns if noun.lower().startswith(data[i].lower())] 
        elif(pattern[index] == 'v'):
            pool = [verb for verb in verbs if verb.lower().startswith(data[i].lower())] 
        elif(pattern[index] == 'a'):
            pool = [adj for adj in adjectives if adj.lower().startswith(data[i].lower())] 
        elif(pattern[index] == 'x'):
            pool = [adv for adv in adverbs if adv.lower().startswith(data[i].lower())] 
        device.append(pool[random.randint(0, len(pool)-1)])
        index += 1 

    out = ''
    for w in device:
        out += w + ' '
    return out
