from Bio import SeqIO
from Bio.Seq import Seq
import csv 

#Threshold for the maximum percentage of occurrence for rare codons
threshold = 0.5 

#Output file in CSV format
Out = open("Rare.csv", "w",newline='')

#Column names for the CSV file generated as output
colnames = ["gene name", "amino acid position", "is.rare.codon"]

#Writing to CSV file
writer = csv.writer(Out)
writer.writerow(colnames)

#Data to be given as output to the CSV file
Data = [[],[],[]]

#parsing the FASTA file containing the gene sequences
for seq_record in SeqIO.parse("orf_coding.fasta", "fasta"):

    #Dictionary to contain the rarity value(binary) of each codon 
    Rarity = {}

    #Dictionary to contain the genetic position, in each protein, for every codon as the key value
    Position = {}

    #Dictionary to contain ID of the gene
    GeneName = {}

    #Initializing the frequency of each codon as 0
    Freq = {}

    #Converting the parsed sequence to a string
    seq = str(seq_record.seq)
    
    #Discretizing the string into codons and looping through the array 
    for n in range(0,len(seq),3):
        codon = str(seq[n:n+3]) 

        #Increment the frequency of codons and logging the position of the amino acid formed after the translation of a given codon
        if codon in Position:
            Position[codon].append(int(n/3))
            Freq[codon] += 1
        else:
            Position[codon] = [int(n/3)]
            Freq[codon] = 1
    
    #Total number of codons in the gene        
    total = sum(Freq.values())

    for key in Freq:

        #Converting frequencies to percentage of occurrence
        Freq[key] = Freq[key]*100/total

        GeneName[key] = str(seq_record.id)

        #Identifying codons having a percentage less than or equal to the threshold, as rare(1)
        if Freq[key] <= threshold:
            Rarity[key] = 1
        else:
            Rarity[key] = 0

    #Merging the dictionaries
    for key in Position:
        writer.writerow([GeneName[key], str(Position[key]), Rarity[key]])
Out.close()