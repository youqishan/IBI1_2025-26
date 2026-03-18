'''
1st, create a dictionary for the 5 genes, and record their expression
2nd, add gene 'MYC' to the dictionary
3rd, build the graph, and add the dotted lne for y-axis
4th, create a variable gene_find, and judge whether it is in the dictionary
'''

# import the libraby
import matplotlib.pyplot as plt
import numpy as np

# build a dictionary for the gene 
gene_dic = {
    'TP53': 12.4, 
    'EGFR': 15.1, 
    'BRCA1': 8.2, 
    'PTEN': 5.3,
    'ESR1': 10.7
}

# add gene MYC
gene_dic['MYC'] = 11.6
print("The dictionary of genes is: ", gene_dic)

# name the x-axis and y-axis of the graph
gene_name = list(gene_dic.keys())
gene_value = list(gene_dic.values())

# make the graph
plt.bar(gene_name, gene_value, color = 'lightblue', width = 0.4)
plt.title('the analysis of gene expression', fontsize=14)
plt.xlabel('gene name', fontsize=12)
plt.ylabel('gene expression', fontsize=12)
# plt.xticks(rotation=0)  # horizontal display the y-axis
plt.grid(axis='y', linestyle='--', alpha=0.7)  # add the dotted line for the y-axis, set transparency
plt.tight_layout()  # adjust the layout, preventing the overlapping of the labels
plt.show()

# set a variable for one gene
gene_find = 'VIP'
# judge whether the gene is in the dictionary
if gene_find in gene_dic:
    print(f"The expression of {gene_find} is {gene_dic[gene_find]}.")
else:
    print(f"Error! Gene {gene_find} is not in the gene dictionary!")


