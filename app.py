from sponge import mnemonic_sentence, anacronym
from os.path import dirname, join
working = dirname(__file__)

data = 'big brain time lets go'
for i in range(5):
    print(mnemonic_sentence(data))
    print(anacronym(data))


#finfp = join(working, './Words/nouns.txt')
#foutfp = join(working, './Words/new_nouns.txt')
#fin = open(finfp, 'r')
#fout = open(foutfp, "w+")
# for line in fin:
#    if(' ' in line):
#        fout.write(line.replace(' ', '\n'))
# fin.close()
# fout.close()
