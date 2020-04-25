from sponge import mnemonic
from os.path import dirname, join
working = dirname(__file__)

for i in range(1):
    print(mnemonic('Parenthesis Exponent Multiplication Division Addition Subtraction')) 


#finfp = join(working, './Words/nouns.txt')
#foutfp = join(working, './Words/new_nouns.txt')
#fin = open(finfp, 'r')
#fout = open(foutfp, "w+")
#for line in fin:
#    if(' ' in line):
#        fout.write(line.replace(' ', '\n'))
#fin.close()
#fout.close()