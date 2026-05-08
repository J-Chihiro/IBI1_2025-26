import re
import matplotlib.pyplot as plt

# Ask the user to input a valid stop codon
stop_codon = input("Enter a stop codon (TAA, TAG, TGA):")

# Validate user input
if stop_codon not in ["TAA", "TAG", "TGA"]:
    print("Error: input is invalid. Please enter TAA, TAG, or TGA.")
    exit()

# Open the FASTA file
file_handle = open("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa", "r")

records = []   # store (gene_name, sequence)
seq = ""       # temporary sequence storage
gene_name = None

# Read FASTA file line by line
for line in file_handle:
    line = line.rstrip()

    # Detect header line (gene ID)
    if line.startswith(">"):
        # Save previous gene before starting a new one
        if gene_name is not None:
            records.append((gene_name, seq))

        gene_name = line[1:]  # remove ">" from header
        seq = ""              # reset sequence container
    else:
        # Append sequence lines
        seq += line

# Save the last gene in the file
if gene_name is not None:
    records.append((gene_name, seq))

file_handle.close()

# Dictionary to store codon counts
codon_counts = {}

# Process each gene individually
for gene_name, sequence in records:

    matches = []  # store all valid ORFs for this gene

    # Find all possible start codons (ATG)
    for start in re.finditer(r'ATG', sequence):
        i = start.start()

        # Scan forward in-frame (step of 3 nucleotides)
        for j in range(i + 3, len(sequence) - 2, 3):
            codon = sequence[j:j+3]

            # Stop codon found
            if codon in ["TAA", "TAG", "TGA"]:

                # Only keep ORF if stop codon matches user input
                if codon == stop_codon:
                    matches.append(sequence[i:j+3])

                break  # stop scanning this ORF

    # If at least one valid ORF exists
    if matches:

        # Select the longest ORF (required by assignment)
        longest = max(matches, key=len)

        # Remove stop codon for upstream codon analysis
        coding_region = longest[:-3]

        # Split sequence into codons (in-frame, step = 3)
        for i in range(0, len(coding_region), 3):
            codon = coding_region[i:i+3]

            # Count codon occurrences
            if codon in codon_counts:
                codon_counts[codon] += 1
            else:
                codon_counts[codon] = 1


# Output results
if codon_counts:
    print("Codon counts upstream of", stop_codon)

    # Print each codon frequency
    for codon in codon_counts:
        print(codon, codon_counts[codon])

    # Prepare data for pie chart
    labels = list(codon_counts.keys())
    sizes = list(codon_counts.values())

    # Plot pie chart
    plt.figure(figsize=(10, 10))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%")

    plt.title("Distribution of in-frame codons upstream of " + stop_codon)

    # Save figure
    plt.savefig("count_codons.png", dpi=300, bbox_inches="tight")
    plt.close()

    print("Pie chart saved as: count_codons.png")

else:
    print("No matching ORFs found for", stop_codon)


# wrong version：

# codon_counts={}#set a dictionary to count the codon
# # calculate the number of codon
# for gene_name, full_sequence in records:
#     #codon = re.findall('ATG(?:...)*?(?:"user_input")', full_sequence)is wrong, as "user_input"can be misunderstood as string
#     codon = re.findall(r'ATG(?:...)*?' + stop_codon, full_sequence)# extract the sequences that meet demands
#     valid_orfs = [m for m in codon if len(m) % 3 == 0]
#     if valid_orfs:
#      longest_ORF=max(valid_orfs,key=len) #leave the longest codon
#      coding_region=longest_ORF[:-3] #delete the stop codons
#      for i in range(0,len(coding_region),3): # report all in_frame codons upstream individually
#          individual_codon=coding_region[i:i+3]
#          if individual_codon in codon_counts:#calculate the number of codons
#              codon_counts[individual_codon]+=1
#          else:
#              codon_counts[individual_codon]=1
# #print the outcome
# #if codon is not true!
# if codon_counts:
#     print("codon counts upstream of",stop_codon)
#     for codon in codon_counts:#print out all the codon using for loop
#         print(codon,codon_counts[codon])

# #make a pie chart
# if codon_counts:
#     labels=list(codon_counts.keys())
#     sizes=list(codon_counts.values())
#     plt.figure(figsize=(10, 10))
#     plt.pie(sizes, labels=labels, autopct="%1.1f%%")
#     plt.title("Distribution of in-frame codons upstream of " + stop_codon)
#  #open a file   
# #out_file=open('count_codons.png')is wrong. this is used in text
#     plt.savefig("count_codons.png", dpi=300, bbox_inches="tight")
#     plt.close()# usins plot rather than write
#     print("Pie charts saved as:count_codons.png")
# else:
#     print("No matching oRFs dounded for", stop_codon)


