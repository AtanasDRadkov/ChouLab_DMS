import Bio
from Bio import SeqIO
import sys

in_file_1 = open(sys.argv[1], 'rU')

constant = 'TAGTAAGCATG'
count_good = 0.0 
count_total = 0.0

for record in SeqIO.parse(in_file_1, 'fastq'):
	count_total += 1
	if constant ==  str(record.seq[15:30]):
		count_good	+= 1
in_file_1.close()

log_file =  open('Script01_logfile.txt', 'w')

log_file.write('Good reads = %d \n' % (count_good) )
log_file.write('Total reads =  %d \n' % (count_total))
log_file.write('Percent good reads =  %f \n' % (count_good/count_total))
log_file.close()