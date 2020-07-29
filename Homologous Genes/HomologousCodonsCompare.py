import csv 
import os

colnames = ["Human Protein", "Human Codons", "Yeast Protein", "Yeast Codons"]
Outputs = open("Codons_Homologous.csv", "w",newline='')
writer = csv.writer(Outputs)
writer.writerow(colnames)

with open('Homologous_sorted.csv') as homologous:
    hom_reader = csv.reader(homologous, delimiter=',')
    Human_codons = {}
    Yeast_codons = {}
    for row in hom_reader:
        Yeast = str(row[0]) + ".csv" 
        Human = str(row[1]) + ".csv"
        with open('../Human_Genome/Proteins/'+Human) as human:
            hum_reader = csv.reader(human, delimiter=',')
            for row_hum in hum_reader:
                aa = str(row_hum[0]) 
                codon = str(row_hum[2])
                if aa in Human_codons:
                    Human_codons[aa].append(codon) 
                else:
                    Human_codons[aa] = [str(row_hum[2])]
        with open('../Yeast_Proteins/'+Yeast) as yeast:
            yes_reader = csv.reader(yeast, delimiter=',')
            for row_yes in yes_reader:
                aa = str(row_yes[0])
                codon = str(row_yes[2])
                if aa in Yeast_codons:
                    Yeast_codons[aa].append(codon) 
                else:
                    Yeast_codons[aa] = [codon]
    
        
