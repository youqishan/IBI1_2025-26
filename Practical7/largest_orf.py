# create a string variable seq
seq = "AAGAUACAUGCAAGUGGUGUGUCUGUUCUGAGAGGGCCUAAAAG"

# find the first occurrence of the start codon "AUG" 
start_index = seq.find("AUG")
# find the last occurrence of the stop codon "UAA" 
stop_index = seq.rfind("UAA")
# find the last occurrence of the stop codon "UAG"
stop_index2 = seq.rfind("UAG")
# find the last occurrence of the stop codon "UGA"
stop_index3 = seq.rfind("UGA")

# check if the start codon is found and if the stop codon is found after the start codon
if start_index != -1 and (stop_index > start_index or stop_index2 > start_index or stop_index3 > start_index):
    # find the closest stop codon after the start codon
    if stop_index == -1:
        stop_index = float('inf')  # if not found, set to infinity
    if stop_index2 == -1:
        stop_index2 = float('inf')  # if not found, set to infinity
    if stop_index3 == -1:
        stop_index3 = float('inf')  # if not found, set to infinity
    closest_stop_index = min(stop_index, stop_index2, stop_index3)
    if closest_stop_index > start_index:
        # extract the ORF sequence
        orf_sequence = seq[start_index:closest_stop_index + 3]  # include the stop codon

        # find the length of the ORF sequence
        orf_length = len(orf_sequence)
        # print the ORF sequence and its length
        print("The largest ORF sequence is:", orf_sequence)
        print("The length of the largest ORF sequence is:", orf_length)
    else:
        print("No valid stop codon found after the start codon.")

else:
    print("No valid ORF found in the sequence.")
