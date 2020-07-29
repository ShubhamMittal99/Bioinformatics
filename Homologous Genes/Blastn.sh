makeblastdb -in YeastGenes.fasta -out yeast -dbtype nucl -title "Yeast genome" 
blastn -query HumanGenes.fna -db yeast -out BlastOutput.txt -max_target_seqs 1 -outfmt 6 -num_threads 4
#awk '{print $1 "," $2}' Result.txt | sort -u > Result_tabulated.csv