#this is the prep_BC.py script for preparing codon dictionary:
#use as input the dictionary prepared with "04_generate_consensus.py script (for codons dictionary)"
import sys
import cPickle as pic

BC_dict = pic.load(open(sys.argv[1]))

for BC in BC_dict:
	if BC_dict[BC] == (0, 'WT'):
		print '%s\t_wt'%(BC)
	else:
		print '%s\t%s'%(BC,BC_dict[BC])  
