import re

# Define DNA stop codons
stop_codons = ["TAA", "TAG", "TGA"]
# Define DNA start codon
start_codon = "ATG"

# Input and output file names
input_file = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
output_file = "stop_genes.fa"

def read_fasta(file_path):
    """
    Read a FASTA file and return a dictionary of gene IDs and their sequences
    Handles multi-line sequences, empty lines, and standard FASTA format
    """
    gene_data = {}
    current_id = None
    seq_list = []

    with open(file_path, 'r') as f:
        for line in f:
            # Remove whitespace and newlines
            clean_line = line.strip()
            # Skip empty lines
            if not clean_line:
                continue

            # Process header line starting with >
            if clean_line.startswith('>'):
                # Save previous gene if exists
                if current_id is not None:
                    gene_data[current_id] = ''.join(seq_list)
                # Extract gene ID (first part after >)
                current_id = clean_line.split()[0][1:]
                # Reset sequence list for new gene
                seq_list = []
            else:
                # Add sequence line and convert to uppercase
                seq_list.append(clean_line.upper())

        # Save the last gene in the file
        if current_id is not None:
            gene_data[current_id] = ''.join(seq_list)

    return gene_data

def check_inframe_stop(sequence):
    """
    Check if a sequence contains in-frame stop codons
    Returns a tuple: (has_stop_codon, list_of_stop_codons_found)
    """
    # Find all start codon positions
    start_positions = []
    seq_length = len(sequence)
    for i in range(seq_length - 2):
        if sequence[i:i+3] == start_codon:
            start_positions.append(i)

    # No start codon = no in-frame stop codon
    if not start_positions:
        return False, []

    # Search for stop codons in reading frame (step of 3)
    found_stops = set()
    for pos in start_positions:
        for i in range(pos, seq_length - 2, 3):
            codon = sequence[i:i+3]
            if codon in stop_codons:
                found_stops.add(codon)

    return len(found_stops) > 0, sorted(list(found_stops))

# Main execution
if __name__ == "__main__":
    # Read FASTA file
    genes = read_fasta(input_file)

    # Write results to new FASTA file
    with open(output_file, 'w') as out_f:
        for gene_id, seq in genes.items():
            has_stop, stops = check_inframe_stop(seq)
            if has_stop:
                # Write formatted header
                stop_str = ', '.join(stops)
                out_f.write(f">{gene_id} {stop_str}\n")
                # Write sequence with 80 characters per line
                for i in range(0, len(seq), 80):
                    out_f.write(seq[i:i+80] + '\n')

    print("Processing completed successfully")