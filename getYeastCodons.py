from Bio import SeqIO
from Bio.Seq import Seq
import csv 

GeneRecord = SeqIO.to_dict(SeqIO.parse("orf_coding.fasta", "fasta"))

for Protein in SeqIO.parse("orf_trans_noAsterix.fasta", "fasta"):
    ProteinCode = str(Protein.id)
    colnames = ["Amino acid", "Amino acid position", "Codon"]
    Outputs = open("Yeast_Proteins/" + ProteinCode + ".csv", "w",newline='')
    writer = csv.writer(Outputs)
    writer.writerow(colnames)
    for i in range(1,len(str(Protein.seq))):
        acid = str(Protein.seq)[i]
        position = i
        codon = str(GeneRecord[ProteinCode].seq)[i:i+3]
        writer.writerow([acid, position, codon])
