'''
1st, make a dictionary to store the mass of each amino acid
2nd, define a function to calculate the mass of a protein sequence
3rd, ask the user to input a protein sequence and calculate its mass
'''

# 1st, make a dictionary to store the mass of each amino acid
amino_acid_mass = {
    'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05, 'V': 99.07,
    'T': 101.05, 'C': 103.01, 'I': 113.08, 'L': 113.08, 'N': 114.04,
    'D': 115.03, 'Q': 128.06, 'K': 128.09, 'E': 129.04, 'M': 131.04,
    'H': 137.06, 'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
}

# 2nd, define a function to calculate the mass of a protein sequence
def calculate_protein_mass(amino_acid_sequence):
    total_mass = 0.0
    for amino_acid in amino_acid_sequence:
        total_mass += amino_acid_mass.get(amino_acid, 0)
    # if the amino acid is not in the dictionary, report wrong and break the loop
        if amino_acid not in amino_acid_mass:
            print(f"Warning: '{amino_acid}' is not a valid amino acid. \n")
            return False

    return total_mass

# 3rd, ask the user to input a protein sequence and calculate its mass
user_input = input("Please enter a protein sequence (using single-letter amino acid codes): ")
protein_mass = calculate_protein_mass(user_input)
if protein_mass:
    print(f"The mass of the protein sequence '{user_input}' is: {protein_mass:.2f} amu.")
else:
    print("Failed to calculate protein mass due to invalid amino acid(s).")