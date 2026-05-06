# read the file
# find the in-frame stop codon that meet the demand
# put the satisfying codon into the new file
import re #import the module
file_handle=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')#open the file
# open a new file
out_file=open("stop_genes.fa","w")

records=[]# use a list to store all the sequences
seq_lines=[]# use a list to store seqeunce temporarily
gene_name=None
# read the file
for line in file_handle:
    line=line.rstrip()
#collect each sequence into a separate list
    if line.startswith(">"):
        if gene_name is not None:
            full_sequence="".join(seq_lines)# combine sequences in the list together as a long sequence
            records.append((gene_name, full_sequence)) # store the seqeunce into the list
        
        gene_name=line[1:] #delete the >
        seq_lines=[] # prepare a new list for new gene to store
   
    else:
        seq_lines.append(line) # add sequences into the list
 # the last gene can't be automatically saved
if gene_name is not None:
    full_sequence = ''.join(seq_lines)
    records.append((gene_name,full_sequence))

# close the file
file_handle.close()

# find the sequence that meet the demand
for gene_name, full_sequence in records:
    stop_codons=re.findall(r'ATG(?:...)*?(TAA|TAG|TGA)',full_sequence)
    if stop_codons:
        stop_list=sorted(set(stop_codons)) #sort the seqeunces and delete the repeat
        out_file.write(">" + gene_name.split()[0] + ";" + ",".join(stop_list) + "\n")# write the gene name and stop codons in the header, then write the full sequence
        out_file.write(full_sequence +"\n") 
# change the line each 60 code
#for i in range(0, len(sequence), 60):
#                output_file.write(sequence[i:i+60] + '\n')
out_file.close() # close the file

#method 2:
# vertify that stop codon is at the end of each seqeunce
# if full_sequence[-3::] not in ['TAA','TAG',"TGA"]:
#   print("wrong")
#   break
# if no wrong is print, mean every stop codon is at the end
# seq_line=''# use a string to store seqeunce temporarily
# gene_name=None
# for line in file_handle:
#     line=line.rstrip()
#     if line[0]=='>':
#         if gene_name is not None:
#             if seq_line[0]=="ATG" #vertify that the seqeunce has the start codon
#             records.append((gene_name,seq_line))
#             out_file.write(">"+gene_name.split()[0]+ ";" + seq_line[-3:] + "\n")
#             out_file.write(full_sequence +"\n")
#         gene_name=line[1:]
#         seq_line=''
#     else:
#         seq_line+=line
# save the last seqeunce
#if gene_name is not None:
#    records.append((gene_name, seq_line))
#    out_file.write(">" + gene_name.split()[0] + ";" + seq_line[-3:] + "\n")
#    out_file.write(seq_line + "\n")













    

        