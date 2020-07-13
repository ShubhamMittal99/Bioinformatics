makeblastdb -in GRCh38_latest_rna.fna -out RNA -dbtype nucl -title "GrCH38 database of RNA" 
tblastn -query GRCh38_latest_protein.faa -db RNA -out Result.txt -max_target_seqs 1 -outfmt 6 -num_threads 4
awk '{print $1 "," $2}' Result.txt | sort -u > Result_tabulated.csv