# establish a dictionary
my_dict={}
gene_expression = {"TP53": 12.4, "EGFR": 15.1, "BRCA1": 8.2, "PTEN": 5.3, "ESR1": 10.7}
print(gene_expression)

#add the gene "MYC"to the dictionary
gene_expression["MYC"]=11.6
print(gene_expression)

#draw a bar chart showing the expression values of genes
import matplotlib.pyplot as plt
genes=list(gene_expression.keys())
values=list(gene_expression.values())
plt.bar(genes,values)
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.title("Gene Expression Levels")
plt.show()

gene_interest= "TP53" #gene of interest that can be modified
#test whether the gene is present in the dataset
if gene_interest in gene_expression:
    print("Expression value:",gene_expression[gene_interest])
else:
    print("Error: Gene not found in dataset")
#calculate the average gene expresion level
average_expression = sum(gene_expression.values()) / len(gene_expression)
print("average expression of genes is:",average_expression)