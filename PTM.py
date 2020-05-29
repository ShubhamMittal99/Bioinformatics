import urllib.request, urllib.parse, urllib.error
import requests
import ast
from requests.exceptions import ConnectionError
from Bio import SeqIO
import csv
import os
from datetime import datetime

#Adding column names
colnames = ["gene name", "amino acid position", "is.modified", "modification.type"]

#Output CSV file
Outputs = open("PTM.csv", "w",newline='')

# Writing to CSV file
writer = csv.writer(Outputs)
writer.writerow(colnames)

# Variables in the HTML text obtained from the YAAM search webpage that contain the positions of the modifications and the types
string_posit = "var posit"
string_modif = "var modi"


for seq_record in SeqIO.parse("orf_coding.fasta", "fasta"):
    # ID of the gene
    ID = str(seq_record.id)

    # Keeping a log of the progress 
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    print(ID)
    
    # URL to search for the protein formed from a given set of amino acids in the YAAM database
    URL = 'http://yaam.ifc.unam.mx/detalle_final.php?orf=' + ID

    #Checking that the website is valid
    try:
        request = requests.get(URL)
    except ConnectionError:
        print(' \n \n Web site does NOT exist: \n\n\n')
    else:
        print('Web site exists: \n')

        #Converting the HTML source code to a string and parsing it line-by-line
        fhand = urllib.request.urlopen(URL)
        for line in fhand:
            # Writing the required posit and modi variables in the output file
            if string_posit in str(line):
                req1 = (str(line).rstrip())
                req1 = req1[req1.find('['): req1.find(']') + 1]
                positions = ast.literal_eval(req1)
            if string_modif in str(line):
                req2 = (str(line).rstrip())
                req2 = req2[req2.find('['): req2.find(']') + 1]
                modifications = ast.literal_eval(req2)
                if modifications == []:
                    writer.writerow([ID, str(positions), 0, str(modifications)])
                else:
                    writer.writerow([ID, str(positions), 1, str(modifications)])
Outputs.close()
