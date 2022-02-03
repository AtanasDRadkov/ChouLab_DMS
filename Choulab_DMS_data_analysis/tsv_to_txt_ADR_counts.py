# How to run: 
# tsv_to_txt_ADR_counts.py main_identifiers_counts.tsv > counts.txt
# script also translates codons into amino acids

import sys
import cPickle as pic
import numpy as np
from collections import defaultdict
import string
import operator

table = string.maketrans('T', 'U')
TRANSLATE = {'ACC': 'T', 'GUC': 'V', 'ACA': 'T', 'AAA': 'K', 'GUU': 'V', 'AAC': 'N', 'CCU': 'P', 'UAU': 'Y', 'AGC': 'S', 'CUU': 'L', 'CAU': 'H', 'AAU': 'N', 'ACU': 'T', 'GUG': 'V', 'CAC': 'H', 'ACG': 'T', 'AGU': 'S', 'CCA': 'P', 'CCG': 'P', 'CCC': 'P', 'UGU': 'C', 'GGU': 'G', 'UCU': 'S', 'AUG': 'M', 'UGC': 'C', 'CAG': 'Q', 'UGA': '*', 'UGG': 'W', 'CGG': 'R', 'UCG': 'S', 'AGG': 'R', 'GGG': 'G', 'UCC': 'S', 'UCA': 'S', 'UAA': '*', 'GGA': 'G', 'UAC': 'Y', 'CGU': 'R', 'GAA': 'E', 'AUA': 'I', 'GCA': 'A', 'AUC': 'I', 'GGC': 'G', 'GCG': 'A', 'CGC': 'R', 'CUG': 'L', 'GAG': 'E', 'CUC': 'L', 'AGA': 'R', 'CUA': 'L', 'GCC': 'A', 'AUU': 'I', 'AAG': 'K', 'CAA': 'Q', 'UUU': 'F', 'GAC': 'D', 'GUA': 'V', 'CGA': 'R', 'UAG': '*', 'GCU': 'A', 'UUG': 'L', 'UUA': 'L', 'GAU': 'D', 'UUC': 'F'}
transform = {'A': 9, 'C': 8, 'E': 20, 'D': 19, 'G': 10, 'F': 2, 'I': 5, 'H': 16, 'K': 18, '*': 0, 'M': 6, 'L': 4, 'N': 14, 'Q': 15, 'P': 11, 'S': 12, 'R': 17, 'T': 13, 'W': 1, 'V': 7, 'Y': 3}

tsv =  open(sys.argv[1], 'r')

headers = tsv.readline().strip().split()
for line in tsv:
	l_list = line.strip().split()
	ID = l_list[0]
	T1_0 = l_list[1]
	T1_1 = l_list[2]
	T2_0 = l_list[3]
	T2_1 = l_list[4]
	T3_0 = l_list[5]
	T3_1 = l_list[6]
	try:
		pos = int(ID.split('_')[0])
		mut = ID.split('_')[1]
		codon = string.translate(mut, table)
		aa = str(TRANSLATE[codon])
		aa_num = int(transform[aa])
		print pos+1, '\t', mut, '\t', aa, '\t', T1_0, '\t', T1_1, '\t', T2_0, '\t', T2_1, '\t', T3_0, '\t', T3_1
	except ValueError:
		pass
