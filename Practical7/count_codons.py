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
    codon = re.findall(r'ATG(?:...)*?' + stop_codon, full_sequence)# extract the sequences that meet demands
    valid_orfs = [m for m in codon if len(m) % 3 == 0]
    if valid_orfs:
     longest_ORF=max(valid_orfs,key=len) #leave the longest codon
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

import re
import matplotlib.pyplot as plt

# 1. 询问用户输入并验证 [cite: 208, 209]
stop_codon = input("Enter a stop codon (TAA, TAG, TGA): ").upper()
if stop_codon not in ["TAA", "TAG", "TGA"]:
    print("Error: input is invalid. Please enter TAA, TAG, or TGA.")
    exit()

# 2. 读取 FASTA 文件并提取序列 [cite: 215, 216]
file_path = "Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
records = []
try:
    with open(file_path, "r") as file_handle:
        gene_name = None
        seq_lines = []
        for line in file_handle:
            line = line.rstrip()
            if line.startswith(">"):
                if gene_name is not None:
                    full_sequence = "".join(seq_lines)
                    records.append((gene_name, full_sequence))
                gene_name = line[1:]
                seq_lines = []
            else:
                seq_lines.append(line)
        # 保存最后一个基因 [cite: 237, 240]
        if gene_name is not None:
            full_sequence = "".join(seq_lines)
            records.append((gene_name, full_sequence))
except FileNotFoundError:
    print(f"Error: {file_path} not found.")
    exit()

# 3. 计算密码子频率 [cite: 244, 245]
codon_counts = {}
for name, full_sequence in records:
    # 使用正则表达式匹配以 ATG 开头、以指定终止密码子结尾且中间为 3 的倍数的 ORF [cite: 250, 251]
    # 注意：此处使用非贪婪匹配获取所有可能的 ORF，然后取最长的一个
    pattern = r'ATG(?:...)*?' + stop_codon
    found_orfs = re.findall(pattern, full_sequence)
    
    if found_orfs:
        # 选取最长的 ORF [cite: 253]
        longest_orf = max(found_orfs, key=len)
        # 去掉末尾的终止密码子 [cite: 254]
        coding_region = longest_orf[:-3]
        
        # 步进 3 个碱基统计密码子 [cite: 255, 257]
        for i in range(0, len(coding_region), 3):
            codon = coding_region[i:i+3]
            if len(codon) == 3:
                codon_counts[codon] = codon_counts.get(codon, 0) + 1

# 4. 输出结果并生成饼图 [cite: 263, 268]
if codon_counts:
    print(f"Codon counts upstream of: {stop_codon}")
    # 打印部分结果供参考
    for codon, count in sorted(codon_counts.items()):
        print(f"{codon}: {count}")

    # 绘制饼图 [cite: 273, 275]
    labels = list(codon_counts.keys())
    sizes = list(codon_counts.values())
    
    plt.figure(figsize=(12, 12)) # 设置较大的尺寸以容纳多个标签
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)
    plt.title(f"Distribution of in-frame codons upstream of {stop_codon}")
    
    # 保存饼图到文件 [cite: 280, 282]
    output_image = "count_codons.png"
    plt.savefig(output_image, dpi=300, bbox_inches="tight")
    print(f"\nPie chart saved as: {output_image}")
else:
    print(f"No matching ORFs found for {stop_codon}")
