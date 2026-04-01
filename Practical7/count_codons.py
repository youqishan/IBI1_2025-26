import re
import matplotlib.pyplot as plt
from collections import defaultdict

# Configure font for plot to avoid garbled characters
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Define constant values
START_CODON = "ATG"
STOP_CODONS = ["TAA", "TAG", "TGA"]
INPUT_FILE = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"

# Get valid stop codon input from user
def get_user_input():
    while True:
        user_input = input("Please enter a stop codon (TAA, TAG, or TGA): ").strip().upper()
        if user_input in STOP_CODONS:
            return user_input
        print("Invalid input. Please enter one of the following: TAA, TAG, TGA.")

# Read FASTA file and return gene dictionary {gene_id: sequence}
def read_fasta(file_path):
    gene_dict = {}
    current_gene = None
    seq_buffer = []
    
    with open(file_path, 'r') as f:
        for line in f:
            clean_line = line.strip()
            if not clean_line:
                continue
            # Parse header line
            if clean_line.startswith('>'):
                # Save previous gene
                if current_gene is not None:
                    gene_dict[current_gene] = ''.join(seq_buffer)
                # Extract correct gene ID
                current_gene = clean_line.split()[0][1:]
                seq_buffer = []
            else:
                # Append sequence and convert to uppercase
                seq_buffer.append(clean_line.upper())
        # Save the last gene
        if current_gene is not None:
            gene_dict[current_gene] = ''.join(seq_buffer)
    return gene_dict

# Find the longest ORF ending with target stop codon and count codons
def count_longest_orf_codons(sequence, target_stop):
    codon_list = []
    # Find all positions of target stop codon
    stop_positions = [match.start() for match in re.finditer(target_stop, sequence)]
    if not stop_positions:
        return codon_list

    max_length = 0
    best_start = -1
    best_stop = -1

    # Check each stop codon to find the longest valid ORF
    for stop_pos in stop_positions:
        # Find all in-frame ATG upstream
        for start_pos in range(stop_pos - 2, -1, -3):
            if sequence[start_pos:start_pos+3] == START_CODON:
                orf_len = stop_pos - start_pos + 3
                # Update the longest ORF
                if orf_len > max_length:
                    max_length = orf_len
                    best_start = start_pos
                    best_stop = stop_pos
                break

    # Extract codons (exclude the stop codon itself)
    if best_start != -1:
        for i in range(best_start, best_stop, 3):
            codon = sequence[i:i+3]
            codon_list.append(codon)
    return codon_list

# Generate and save pie chart
def plot_codon_distribution(codon_counts, target_stop):
    total = sum(codon_counts.values())
    # Group small categories (less than 1%) to make chart clean
    filtered = {}
    other = 0
    for codon, cnt in codon_counts.items():
        if cnt / total >= 0.01:
            filtered[codon] = cnt
        else:
            other += cnt
    if other > 0:
        filtered["Others (<1%)"] = other

    # Plot settings
    plt.figure(figsize=(12, 12))
    plt.pie(filtered.values(), labels=filtered.keys(), autopct='%1.1f%%', startangle=90)
    plt.axis('equal')
    plt.title(f'Codon Distribution Upstream of {target_stop} (Longest ORF)', fontsize=16)
    
    # Save chart to file
    filename = f"codon_distribution_{target_stop}.png"
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Pie chart saved successfully: {filename}")

# Main program execution
if __name__ == "__main__":
    # Step 1: Get user input
    target_stop = get_user_input()
    
    # Step 2: Read FASTA file
    print("Reading FASTA file...")
    gene_sequences = read_fasta(INPUT_FILE)
    
    # Step 3: Count codons from longest ORFs
    print("Analyzing codon distribution...")
    codon_counter = defaultdict(int)
    for seq in gene_sequences.values():
        codons = count_longest_orf_codons(seq, target_stop)
        for c in codons:
            codon_counter[c] += 1
    
    # Step 4: Print results
    print(f"\nCodon counts upstream of {target_stop}:")
    for codon, count in sorted(codon_counter.items()):
        print(f"{codon}: {count}")
    
    # Step 5: Generate and save pie chart
    plot_codon_distribution(codon_counter, target_stop)
    print("\nTask 3 completed successfully!")