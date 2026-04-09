# establish a dictionary to store the amino acid and related mass
Amino_acid={"G":57.02,"A":71.04,"S":87.03,"P":97.05,"V":99.07,"T":101.05,"C":103.01,"I":113.08,"L":113.08,"N":114.04,"D":115.03,"Q":128.06,"K":128.09,"E":129.04,"M":131.04,"H":137.06,"F":147.07,"R":156.10,"Y":163.06,"W":186.08}
# create a function
def calculate_mass(sequence):
    """
    input: seqeunce, an amino seqeunce
    Returns the mass of total protein
    """
    total_mass=0
    for aa in sequence:
        if aa not in Amino_acid:# report an error if the given amino acid is wrong
            print("Error:invalid given amino acid")
            exit()
        else:
            total_mass+=Amino_acid[aa]# calculate the mass. of total protein
    return total_mass  #remember to return !
sequence="ACG"
Total=calculate_mass(sequence)#invoke the function
print(f"The total protein mass of {sequence}:{Total:.2f}amu")

#method 2--use true or false
#def calculate_mass(sequence):
#    total_mass = 0
#    for aa in sequence:
#        if aa not in Amino_acid:
#            return None
#        total_mass += Amino_acid[aa]
#    return total_mass
#if Total is None:
#    print("Error: invalid amino acid")
#else:
#    print(f"The total protein mass of {sequence}: {Total:.2f} amu")
