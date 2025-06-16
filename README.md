# Parsing and Analyzing DNA Sequences with BioPython

This Python script demonstrates how to parse DNA sequence data from a FASTA file using the `Bio.SeqIO` module from the Biopython library. It calculates and prints relevant statistics for each sequence, such as length, GC content, and sequence validity.

## Features

- Reads multiple DNA sequences from a FASTA file.
- Calculates sequence length and GC content.
- Checks whether each sequence is valid (composed of only A, T, C, and G).
- Outputs a summary of each sequence in a readable format.

## Requirements

- Python 3.x
- [Biopython](https://biopython.org/)

Install Biopython with pip:

```bash
pip install biopython
```

### How to Use
- Place your FASTA file in the same directory as the script.

- Edit the script to change the filename if needed (default is example.fasta).

- Run the script:
```
python from Bio import SeqIO.py
```
- View the printed sequence summaries in your terminal.
