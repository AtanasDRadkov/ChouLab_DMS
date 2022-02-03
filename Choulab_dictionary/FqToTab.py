import sys
#file = sys.stdin
f=sys.stdin
for line in f:
    hdr = line.rstrip('\n')[1:]
    seq = f.next().rstrip('\n')
    f.next()
    qual = f.next().rstrip('\n')
    print "\t".join( (hdr, seq, qual ) )