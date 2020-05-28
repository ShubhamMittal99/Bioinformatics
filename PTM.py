import urllib.request, urllib.parse, urllib.error
import requests
import ast
from requests.exceptions import ConnectionError
from Bio import SeqIO
import csv 
import os
from datetime import datetime


Output = open("PTM.csv", "w",newline='')

colnames = ["gene name", "amino acid position", "is.modified", "modification.type"]

#Writing to CSV file
writer = csv.writer(Output)
writer.writerow(colnames)

string_posit = "var posit"
string_modif = "var modif"

for seq_record in SeqIO.parse("orf_coding.fasta", "fasta"):
    ID = str(seq_record.id)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(current_time)
    print(ID)
    URL = 'http://yaam.ifc.unam.mx/detalle_final.php?orf=' + ID

    try:
        request = requests.get(URL)
    except ConnectionError:
        print(' \n \n Web site does NOT exist: \n\n\n')
    else:
        print('Web site exists: \n')
        fhand = urllib.request.urlopen(URL)
        for line in fhand:
            if string_posit in  str(line):
                req1 = (str(line).rstrip())
                req1 = req1[req1.find('[') : req1.find(']')+1]
                positions = ast.literal_eval(req1)
            if string_modif in str(line):
                req2 = (str(line).rstrip())
                req2 = req2[req2.find('[') : req2.find(']')+1]
                modifications = ast.literal_eval(req2)
                if modifications == []:
                    writer.writerow([ID,str(positions),0,str(modifications)])
                else:
                    writer.writerow([ID,str(positions),1,str(modifications)])

'''
temp.write(line.decode('utf-8').encode('cp850','replace').decode('cp850').strip() + "\n")

        req1 = str(search_string_in_file("temporary.txt", "var posit")) 
        req1 = req1[req1.find('[') : req1.find(']')+1]
        positions = ast.literal_eval(req1)

        req2 = str(search_string_in_file("temporary.txt", "var modi")) 
        req2 = req2[req2.find('[') : req2.find(']')+1]
        modifications = ast.literal_eval(req2)
'''
Output.close()