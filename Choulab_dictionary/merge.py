with open('read2_1to245.txt','r') as read1_file, open('read1_RC_1to267.txt','r') as read2_file, open('merged_DNA_sequences.txt','w') as output_file:
      for line1 in read1_file:
          line2=read2_file.readline()
          merged_line_list=list(line1[:-1]) # Take the lines from the forward read, and put them in a list
          merged_line_list.append(line2) # add the lines of the reverse read
          merged_line="".join(merged_line_list) # turn the list into a string
          output_file.write(merged_line)