import random
from os.path import dirname, join
working = dirname(__file__)


def read_corpus(files):
    corpus = list()
    for file in files:
        fp = join(working, './Words/' + file + '.txt')
        with open(fp, 'r') as fin:
            corpus.append(fin.read().splitlines())
    return corpus


def gen_pattern(n):
    structure = [
        '', 'n', 'nv', 'nxv', 'nxvn', 'anxvn', 'acnxvn', 'acnxvan', 'aacnxvan', 'aacnxvacn', 'aacnxvaacn'
    ]
    return structure[n]


def mnemonic_sentence(s):
    files = ['nouns', 'verbs', 'adjectives', 'adverbs', 'colors']
    nouns, verbs, adjectives, adverbs, colors = read_corpus(files)
    data = [s[0].lower() for s in s.split(' ')]
    pattern = gen_pattern(len(data))

    device = list()
    index = 0
    for i in range(len(data)):
        if(pattern[index] == 'n'):
            pool = [noun for noun in nouns if noun.lower(
            ).startswith(data[i].lower())]
        elif(pattern[index] == 'v'):
            pool = [verb for verb in verbs if verb.lower(
            ).startswith(data[i].lower())]
        elif(pattern[index] == 'a'):
            pool = [adj for adj in adjectives if adj.lower(
            ).startswith(data[i].lower())]
        elif(pattern[index] == 'x'):
            pool = [adv for adv in adverbs if adv.lower(
            ).startswith(data[i].lower())]
        elif(pattern[index] == 'c'):
            pool = [color for color in colors if color.lower(
            ).startswith(data[i].lower())]
        device.append(pool[random.randint(0, len(pool)-1)])
        index += 1
    out = ''
    for w in device:
        out += w + ' '
    return out


def anacronym(s):
    return ''.join([s[0].upper() for s in s.split(' ')])
