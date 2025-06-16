#Indentifying the eukaryotic sequence for DNA polymerase 
from Bio import SeqIO
import csv

# SETTINGS
blast_output_file = "/Users/selina/Downloads/Project foldernew/hits.tsv"
bacteria_fasta_file = "/Users/selina/Downloads/Project foldernew/uniprotkb_Enterobacteriaceae_bacterium_2025_05_04.fasta"
filtered_output_file = "/Users/selina/Downloads/Project foldernew/filtered_hits.tsv"
summary_output_file = "/Users/selina/Downloads/Project foldernew/hit_summary.tsv"
extracted_fasta_file = "/Users/selina/Downloads/Project foldernew/matched_bacterial_sequences.fasta"


# Thresholds
MIN_PERCENT_IDENTITY = 95.0
MIN_QUERY_COVERAGE = 0.90  # 90%

# Step 1: Load bacterial protein sequences into a dictionary
print("Loading bacterial protein sequences...")
bacteria_seqs = SeqIO.to_dict(SeqIO.parse(bacteria_fasta_file, "fasta"))

# Step 2: Parse BLASTP results and filter hits
print("Parsing BLASTP hits...")
filtered_hits = []
with open(blast_output_file, "r") as f_in:
    reader = csv.reader(f_in, delimiter="\t")
    for row in reader:
        print(f"Reading row: {row}")  # Debug: print each row being read from hits.tsv
        query_id = row[0]
        subject_id = row[1]
        percent_identity = float(row[2])  # Assuming column 3 has percent identity
        query_coverage = float(row[11])  # Assuming column 12 has query coverage
        
        # Example filter: Sequence identity > 95% and query coverage > 90%
        if percent_identity >= 95.0 and query_coverage >= 90.0:
            filtered_hits.append(row)

# Debug: Check how many hits passed the filtering criteria
print(f"Filtered hits: {len(filtered_hits)}")

# Step 3: Write the filtered results to a new file
with open(filtered_output_file, "w") as f_out:
    writer = csv.writer(f_out, delimiter="\t")
    writer.writerows(filtered_hits)
print(f"Filtered hits saved to {filtered_output_file}")

# Step 4: Extract matched bacterial sequences and write them to a FASTA file
print("Extracting matched bacterial sequences...")
with open(extracted_fasta_file, "w") as f_out:
    for hit in filtered_hits:
        subject_id = hit[1]
        if subject_id in bacteria_seqs:
            # Write the matched sequence to the FASTA file
            SeqIO.write(bacteria_seqs[subject_id], f_out, "fasta")

print(f"Extracted bacterial sequences saved to {extracted_fasta_file}")
