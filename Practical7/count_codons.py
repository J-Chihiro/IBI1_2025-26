# ask the user to input one of the possible stop codon
stop_codon=input("Enter a stop codon(TAA,TAG,TGA):")
if stop_codon not in ["TAA","TAG","TGA"]:
    print("Error:input is invalid.Please enter TAA,TAG,or TGA.")
    exit()# if not exit, the wrong input will contine to print seqeunces

# import the neeeded module
import re
import matplotlib.pyplot as plt

#open the file
file_handle=open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa","r")
records=[]# use a list to store all the sequences
seq_lines=''# use a string to store the sequence temporarily
gene_name=None
# read the file
for line in file_handle:
    line=line.rstrip()

#collect each sequence into a separate list
    if line[0]=='>':
        if gene_name is not None:
            records.append((gene_name, seq_lines)) # store the seqeunce into the list
        gene_name=line[1:] #delete the >
        seq_lines='' # prepare a new list for new gene to store  
    else:
        seq_lines+=line # add sequences into the list
 # the last gene can't be automatically saved
if gene_name is not None:
    records.append((gene_name,seq_lines))
# close the file
file_handle.close()

codon_counts={}#set a dictionary to count the codon
# calculate the number of codon
for gene_name, full_sequence in records:
    #codon = re.findall('ATG(?:...)*?(?:"user_input")', full_sequence)is wrong, as "user_input"can be misunderstood as string
    codon=re.findall('ATG(?:...)*?'+ stop_codon,full_sequence)# extract the sequences that meet demands
    if codon:
     longest_ORF=max(codon,key=len) #leave the longest codon
     coding_region=longest_ORF[:-3] #delete the stop codons
     for i in range(0,len(coding_region),3): # report all in_frame codons upstream individually
         individual_codon=coding_region[i:i+3]
         if individual_codon in codon_counts:#calculate the number of codons
             codon_counts[individual_codon]+=1
         else:
             codon_counts[individual_codon]=1
#print the outcome
#if codon is not true!
if codon_counts:
    print("codon counts upstream of",stop_codon)
    for codon in codon_counts:#print out all the codon using for loop
        print(codon,codon_counts[codon])

#make a pie chart
if codon_counts:
    labels=list(codon_counts.keys())
    sizes=list(codon_counts.values())
    plt.figure(figsize=(10, 10))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")
    plt.title("Distribution of in-frame codons upstream of " + stop_codon)
 #open a file   
#out_file=open('count_codons.png')is wrong. this is used in text
    plt.savefig("count_codons.png", dpi=300, bbox_inches="tight")
    plt.close()# usins plot rather than write
    print("Pie charts saved as:count_codons.png")
else:
    print("No matching oRFs dounded for", stop_codon)

