import Bio
from Bio import SeqIO
import sys
import cPickle as pic

pair_dict = {}

input_file_1 = open(sys.argv[1], 'rU') # output of script01 (fastq format), these sequences contain the N18 bar-code
input_file_2 = open(sys.argv[2], 'rU') # raw read2 fastq file from the sequencer

input1_records_count = 0 # the number of records in the input_file_1 
for record in SeqIO.parse(input_file_1, 'fastq'):
	input1_records_count += 1
	id_line = record.id.split(':')
	identity_key = '%s-%s-%s-%s' % (id_line[3], id_line[4], id_line[5], id_line[6]) # the key for the pair_dict 
	bar_code = str(record.seq[497:512]) #the value in pair_dict[identity_key][0]
	pair_dict[identity_key] = [bar_code]
	print 'Selected Sequences - record # %d' %(input1_records_count) # to track progress
input_file_1.close()	

input2_records_count = 0 # number of records in input_file_2 (raw reads file)
matched_reads = 0 # the number of records in input_file_2 that match to an ID from input_file_1

for record in SeqIO.parse(input_file_2, 'fastq'):
	input2_records_count +=1
	print 'Checking for match - record # %d' %(input2_records_count) # to track progress
	id_line = record.id.split(':')
	identity_key = '%s-%s-%s-%s' % (id_line[3], id_line[4], id_line[5], id_line[6]) # the key for the pair_dict
	if identity_key in pair_dict: 
		pair_dict[identity_key].append(str(record.seq)) # appends the Read2 sequence to the pair_dict value as pair_dict[identity_key][1]
		matched_reads += 1
		print identity_key, matched_reads, input2_records_count
		print pair_dict[identity_key]
input_file_2.close()	
	
pic.dump(pair_dict, open('pair_dict.pkl', 'wb')) # dumps the dictionary as a pickle object. this will be the input for script03

log_file =  open('Script02_logfile.txt', 'w') # writes a logfile documenting the dictionary composition. Use the pickle_printer script to examine the dictionary contents 

log_file.write('Dict contains = %d \n' % (input1_records_count) )
log_file.write('Total reads queried = %d \n' % (input2_records_count) )
log_file.write('Matched reads =  %d \n' % (matched_reads) )
log_file.close()