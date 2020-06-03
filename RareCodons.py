from Bio import SeqIO
from Bio.Seq import Seq
import csv 

#Output file in CSV format
Out = open("Rare.csv", "w",newline='')

#Column names for the CSV file generated as output
colnames = ["gene name", "amino acid position", "is.rare.codon"]

#Writing to CSV file
writer = csv.writer(Out)
writer.writerow(colnames)

#Data to be given as output to the CSV file
Data = [[],[],[]]

#Dictionary to contain the frequency of the codons in the entire genome 
OverallFreq={}

#parsing the FASTA file containing the gene sequences and getting the total number of occurrences of each codon
for seq_record in SeqIO.parse("orf_coding.fasta", "fasta"):
    seq = str(seq_record.seq)
    for n in range(0,len(seq),3):
        codon = str(seq[n:n+3])

        if codon in OverallFreq:
            OverallFreq[codon] += 1
        else:
            OverallFreq[codon] = 1

totalnum = sum(OverallFreq.values())
OverallFreq = {k: v*1000/totalnum for k, v in OverallFreq.items()}

#parsing the FASTA file containing the gene sequences and identifying rare codons
for seq_record in SeqIO.parse("orf_coding.fasta", "fasta"):

    #Dictionary to contain the rarity value(binary) of each codon 
    Rarity = {}

    #Dictionary to contain the genetic position, in each protein, for every codon as the key value
    Position = {}

    #Dictionary to contain ID of the gene
    GeneName = {}

    #Converting the parsed sequence to a string
    seq = str(seq_record.seq)
    
    #Discretizing the string into codons and looping through the array 
    for n in range(0,len(seq),3):
        codon = str(seq[n:n+3]) 

        #Increment the frequency of codons and logging the position of the amino acid formed after the translation of a given codon
        if codon in Position:
            Position[codon].append(int(n/3))
        else:
            Position[codon] = [int(n/3)]

    for key in Position:

        GeneName[key] = str(seq_record.id)

        #Identifying codons having a percentage less than or equal to 10% as rare
        if OverallFreq[key] <= 10:
            Rarity[key] = 1
        else:
            Rarity[key] = 0

    #Merging the dictionaries
    for key in Position:
        writer.writerow([GeneName[key], str(Position[key]), Rarity[key]])
Out.close()