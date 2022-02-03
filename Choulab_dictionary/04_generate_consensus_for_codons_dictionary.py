import Bio
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import motifs
from Bio.Alphabet import IUPAC
import sys
import cPickle as pic

dic = pic.load(open(sys.argv[1] , 'rb'))

primer1 = 'ATGCTTACTA' 
# this is just a constant region on my construct, between the barcode and the variable region of Tae1 DNA sequence
wt1 = 'GACAGTCTCGATCAATGCATCGTCAACGCCTGCAAGAACAGCTGGGACAAGAGCTACCTGGCCGGCACCCCGAACAAGGACAACTGTTCCGGCTTCGTCCAGTCGGTGGCCGCCGAGCTGGGCGTACCGATGCCCCGCGGCAACGCCAACGCCATGGTCGACGGCCTGGAGCAGAGCTGGACCAAGCTCGCCTCCGGCGCCGAGGCCGCGCAGAAGGCGGCCCAGGGCTTCCTGGTGATCGCCGGCCTGAAGGGCCGCACCTACGGGCACGTCGCGGTGGTCATCAGCGGTCCGCTGTATCGGCAGAAGTACCCGATGTGCTGGTGCGGCAGCATCGCCGGCGCGGTCGGCCAGAGCCAGGGCCTGAAGTCGGTCGGCCAGGTGTGGAATCGCACCGACCGCGACCGCCTCAACTACTACGTCTACTCCCTGGCCAGTTGCAGCCTGCCCAGGGCCAGT'


allele_dic = {}
non_singles = {}
allele_dic2 = {}
non_singles2 = {}
allele_dump = {}
non_singles_dump = {}

single_count = 1
non_single_count = 1
count = 1
WT_count = 1

for key in dic:
	print key , count
	count +=1
	glob1 = []
	for seq_index in range(len(dic[key])):
		if dic[key][seq_index][487:497] == primer1: # WATCH THE SELECTION HERE - THE NUMBERING IS VERY COUNTERINTUITIVE!!!
			sequence = dic[key][seq_index]
			glob1.append(Seq(sequence[7:466])) # WATCH THE SELECTION HERE - THE NUMBERING IS VERY COUNTERINTUITIVE!!!
		else:
			pass
	try:
		motif1 = motifs.create(glob1)
	
		allele_gen1 = motifs.create([motif1.consensus, wt1])
		codon = 'NNN'
		codon_list = []
		for index in range(len(wt1)):
			letter = wt1[index]
			if allele_gen1.counts[letter][index] == 1:
				aa_position = int(float(index)/3)
				codon = str(motif1.consensus[(aa_position*3):((aa_position*3)+3)])
				to_append = str(aa_position+2)+'_'+codon
				if to_append in codon_list:
					pass
				else:
					codon_list.append(to_append)	
		if len(codon_list) == 1:
			split_codon = codon_list[0].split('_')
			codon_tuple = (int(split_codon[0]), str(split_codon[1]))
			allele_dic[key] = codon_tuple	
			print 'single' + str(single_count)
			single_count += 1
		elif len(codon_list)== 0:
			print 'WT' + str(WT_count)
			WT_count += 1
			allele_dic[key] = (int(0), str('WT'))
		else:
			non_singles[key] = codon_list
			print 'non_single' + str(non_single_count)
			non_single_count += 1
	except TypeError:
		pass		
print '%d singles' %(single_count - 1)
print '%d WT' %(WT_count - 1)
print '%d non_singles' %(non_single_count - 1) 
pic.dump(allele_dic, open('allele_dic_with_WT.pkl', 'wb'))
pic.dump(non_singles, open('non_singles.pkl', 'wb'))