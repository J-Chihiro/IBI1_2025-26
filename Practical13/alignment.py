# Function to read FASTA files
def read_fasta(filename):
    sequence = "" #prepare to store the amino seqeunce
    with open(filename, "r") as file:
        for line in file: #read the file line by line
            # Ignore FASTA header
            if not line.startswith(">"):
                sequence += line.strip()
    return sequence

# Function to read BLOSUM62 matrix
def read_blosum(filename):
    blosum = {} # store into a dictionary
    with open(filename, "r") as file:
        lines = file.readlines() # read all the lines
        amino_acids = lines[0].split() #get ['A', 'R', 'N', 'D', 'C', 'Q', 'E']
        for line in lines[1:]: # strat from the second line
            parts = line.split() #get A 4 -1 -2 -2
            row_aa = parts[0] # get the amino name 
            scores = parts[1:] # get the score
            for i in range(len(amino_acids)): # get the eow seqeunce
                col_aa = amino_acids[i]  
                score = int(scores[i])               
                blosum[(row_aa, col_aa)] = score
#the final dictionary:{
# ('A','A'):4,
# ('A','R'):-1,
# ('R','R'):5
#}
    return blosum

# Function for sequence alignment
def align_sequences(seq1, seq2, blosum):
    total_score = 0
    identical = 0
    for i in range(len(seq1)):
        aa1 = seq1[i]
        aa2 = seq2[i]

        # Add BLOSUM score
        total_score += blosum[(aa1, aa2)]

        # Count identical amino acids
        if aa1 == aa2:
            identical += 1
    percentage_identity = (identical / len(seq1)) * 100

    return total_score, percentage_identity

# Read sequences
human = read_fasta("human.fasta")
mouse = read_fasta("mouse.fasta")
random_seq = read_fasta("random.fasta")

# Read BLOSUM62
blosum62 = read_blosum("BLOSUM62.txt")


# Human vs Mouse
score1, identity1 = align_sequences(human, mouse, blosum62)
print("Human vs Mouse")
print("Alignment score:", score1)
print(f"Percentage identity:{identity1:.2f}%")

# Human vs Random
score2, identity2 = align_sequences(human, random_seq, blosum62)
print("\nHuman vs Random")
print("Alignment score:", score2)
print(f"Percentage identity:{identity2:.2f}%")

# Mouse vs Random
score3, identity3 = align_sequences(mouse, random_seq, blosum62)
print("\nMouse vs Random")
print("Alignment score:", score3)
print(f"Percentage identity:{identity3:.2f}%")