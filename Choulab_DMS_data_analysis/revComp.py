import sys


def reverseComplement(sequence):
	complement = {'A':'T','C':'G','G':'C','T':'A','N':'N'}
	return "".join([complement.get(nt, '') for nt in sequence[::-1]])



f=sys.stdin

for line in f:
    hdr = line.rstrip('\n')
    seq = f.next().rstrip('\n')
    rcseq = reverseComplement(seq)
    f.next()
    qual = f.next().rstrip('\n')[::-1]
    f.next()
    print "\n".join( (hdr, rcseq, "+", qual ) )