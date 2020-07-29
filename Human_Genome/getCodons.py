from Bio import SeqIO
from Bio.Seq import Seq
import csv 

ProteinRecord = SeqIO.to_dict(SeqIO.parse("GRCh38_latest_protein.faa", "fasta"))
GeneRecord = SeqIO.to_dict(SeqIO.parse("GRCh38_latest_rna.fna", "fasta"))
with open('Result_tabulated.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        ProteinCode = row[0]
        GeneCode = row[1]
        colnames = ["Amino acid", "Amino acid position", "Codon"]
        Outputs = open("Proteins/" + ProteinCode + ".csv", "w",newline='')
        writer = csv.writer(Outputs)
        writer.writerow(colnames)
        for i in range(1,len(str(ProteinRecord[ProteinCode].seq))):
            acid = str(ProteinRecord[ProteinCode].seq)[i]
            position = i
            codon = str(GeneRecord[GeneCode].seq)[i:i+3]
            writer.writerow([acid, position, codon])