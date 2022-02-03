#Usage: python PlotFitnessDistributions_ADR.py main_identifiers_scores.tsv > WT_fitnesses (uncomment print command for WT_fitnesses, comment out the other print command)
#Usage: python PlotFitnessDistributions_ADR.py main_identifiers_scores.tsv > fitnesses (uncomment print command for fitnesses, comment out the other print command)

import Bio
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna, generic_protein
import sys
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns

infile = open(sys.argv[1], 'r')
data = {}

WT_seq = "MDSLDQCIVNACKNSWDKSYLAGTPNKDNCSGFVQSVAAELGVPMPRGNANAMVDGLEQSWTKLASGAEAAQKAAQGFLVIAGLKGRTYGHVAVVISGPLYRQKYPMCWCGSIAGAVGQSQGLKSVGQVWNRTDRDRLNYYVYSLASCSLPRAS"

WT_fitnesses = []
fitnesses = []

counter = 0
for line in infile:
	counter +=1
	
	if counter <=2:
		continue
	
	elif line[:3] == "_wt":
		continue
		
	fields = line.split()
	score = float(fields[-1])
	
	pos, codon = fields[0].split("_")
	
	pos = int(pos)
	seq = Seq(codon, generic_dna)
	aa = str(seq.translate())
	
	fitnesses.append(score)
	if aa == WT_seq[pos]:
		WT_fitnesses.append(score)	
		#print pos+1, '\t', seq, '\t', aa, '\t', score
	elif not aa == WT_seq[pos]:
		fitnesses.append(score)
		#print pos+1, '\t', seq, '\t', aa, '\t', score
	else:
		pass