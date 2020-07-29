import csv 
import os
import pandas as pd

colnames = ["Amino Acid", "Human Codons", "Yeast Codons"]

with open('Homologous_sorted.csv') as homologous:
    hom_reader = csv.reader(homologous, delimiter=',')
    next(hom_reader)
    Human_codons = {}
    Yeast_codons = {}
    for row in hom_reader:
        Yeast = str(row[0]) + ".csv" 
        Human = str(row[1]) + ".csv"
        with open('../Human_Genome/Proteins/'+Human) as human:
            hum_reader = csv.reader(human, delimiter=',')
            next(hum_reader)
            for row_hum in hum_reader:
                aa_hum = str(row_hum[0]) 
                codon = str(row_hum[2])
                if aa_hum in Human_codons:
                    Human_codons[aa_hum].append(codon) 
                else:
                    Human_codons[aa_hum] = [str(row_hum[2])]
        with open('../Yeast_Proteins/'+Yeast) as yeast:
            yes_reader = csv.reader(yeast, delimiter=',')
            next(yes_reader)
            for row_yes in yes_reader:
                aa_yes = str(row_yes[0])
                codon = str(row_yes[2])
                if aa_yes in Yeast_codons:
                    Yeast_codons[aa_yes].append(codon) 
                else:
                    Yeast_codons[aa_yes] = [codon]

        Outputs = open("Matched/Homologous-" + str(row[0]) + "-" + str(row[1]) + ".csv", "w",newline='')
        writer = csv.writer(Outputs)
        writer.writerow(colnames)

        for aa in Human_codons:
            if aa in Yeast_codons:
                writer.writerow([aa, Human_codons[aa], Yeast_codons[aa]])
