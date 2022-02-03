import Bio
from Bio.Seq import Seq
import sys
import numpy as np

infile = open(sys.argv[1], 'r')
data = {}

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
	
	pos = int(pos) + 1
	seq = Seq(codon)
	aa = str(seq.translate())
	
	try:
		test = data[pos]
	except KeyError:
		data[pos] = {}


	try:
		test = data[pos][aa]
	except KeyError:
		data[pos][aa] = []
	
	data[pos][aa].append(score)
	
	
	
positions = sorted(list(set(data.keys())))
aas = "ACDEFGHIKLMNPQRSTVWY*"

print("Position  ,A,C,D,E,F,G,H,I,K,L,M,N,P,Q,R,S,T,V,W,Y,*,,avg")

for position in range(1,np.amax(positions)+1):
	fitnesses = []
	all = []
	for aa in aas:
		try:
			fitnesses.append(str(np.mean(data[position][aa])))
			all.append(np.mean(data[position][aa]))
		except KeyError:
			fitnesses.append('nan')
	avg = np.mean(all)
	fitnesses.append('0.0')
	fitnesses.append(str(avg))
	
	print(f"{position} ,{','.join(fitnesses)}")