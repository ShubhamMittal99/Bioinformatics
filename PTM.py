import urllib.request, urllib.parse, urllib.error
import requests
import ast
from requests.exceptions import ConnectionError
from Bio import SeqIO
import csv 
import os


def search_string_in_file(file_name, string_to_search):
    line_number = 0
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            line_number += 1
            if string_to_search in line:
                # If yes, then add the line number & line as a tuple in the list
                result = (line_number, line.rstrip())
 
    # Return list of tuples containing line numbers and lines where string is found
    return result

Output = open("PTM.csv", "w",newline='')

colnames = ["gene name", "amino acid position", "is.modified", "modification.type"]

#Writing to CSV file
writer = csv.writer(Output)
writer.writerow(colnames)

for seq_record in SeqIO.parse("orf_coding.fasta", "fasta"):
    ID = str(seq_record.id)
    URL = 'http://yaam.ifc.unam.mx/detalle_final.php?orf=' + ID
    temp = open("temporary.txt","w")
    try:
        request = requests.get(URL)
    except ConnectionError:
        print('Web site does not exist:')
        print(ID + "\n")
    else:
        fhand = urllib.request.urlopen(URL)
        for line in fhand:
            temp.write(line.decode('utf-8').encode('cp850','replace').decode('cp850').strip() + "\n")

        req1 = str(search_string_in_file("temporary.txt", "var posit")) 
        req1 = req1[req1.find('[') : req1.find(']')+1]
        positions = ast.literal_eval(req1)

        req2 = str(search_string_in_file("temporary.txt", "var modi")) 
        req2 = req2[req2.find('[') : req2.find(']')+1]
        modifications = ast.literal_eval(req2)
        if positions == []:
            writer.writerow([ID,str(positions),0,str(modifications)])
        else:
            writer.writerow([ID,str(positions),1,str(modifications)])
    temp.close()
    os.remove("temporary.txt")
Output.close()