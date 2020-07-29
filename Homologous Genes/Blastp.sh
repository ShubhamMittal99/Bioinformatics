makeblastdb -in GRCh38_latest_protein.faa -out human -dbtype prot -title "Human genome" 
blastp -query orf_trans.fasta -db human -out Homologous.txt -max_target_seqs 1 -outfmt 6 -num_threads 4
awk '{print $1 "," $2 "," $3}' Homologous.txt | sort -u > Homologous_tabulated.csv
sort -k1,1 -k3,3rn -t, Homologous_tabulated.csv | sort -uk1,1 -t, | awk -F"," '$3>80' > Homologous_sorted.csv