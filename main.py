#-----------------------
# To do list
#-----------------------
# * Only start translation on Codon start AUG, and stop on Codon stop UAA,UGA,UAG
# * BLAST protein sequence using Biopython
#-----------------------------------------------------------------

# Test sequence : ATGGCTTCAAGTCCGCACTACGAATGGCAGCTTGAGGCTCCAGGTCGG -> AUGGCUUCAAGUCCGCACUACGAAUGGCAGCUUGAGGCUCCAGGUCGG -> MASSPHYEWQLEAPGR
# Test sequence for BLAST: gcgagcagcccgccgtatgaatggcagcaggaagcggtggaaccgggc -> ASSPPYEWQQEAVEPG -> https://www.ncbi.nlm.nih.gov/protein/WP_276301433.1?report=genbank&log$=protalign&blast_rank=1&RID=6HYUP7D5013 (ubiquinol-cytochrome c reductase iron-sulfur subunit [Halorussus)

# Ask for initial sequence, set nature booleans and identify input's nature after cleanup
initial_sequence = input("Input the sequence to manipulate: ")
from central_dogma_module import sequence_cleanup, initiate, sequence_identification
initiate()
cleaned_sequence = sequence_cleanup(initial_sequence)
sequence_identification(cleaned_sequence)

# Choice of operations to apply
print("""Current operations available to apply on sequence are:
[1] Transcription of DNA to RNA
[2] Translation of DNA/RNA to protein
[3] Retrotranscription of RNA to DNA""")

choice = input("Type operation's number to apply, without brackets: ")
if choice == '1':
    from central_dogma_module import transcription
    transcription(cleaned_sequence)
elif choice == "2":
    from central_dogma_module import translation
    translation(cleaned_sequence)
elif choice == '3':
    from central_dogma_module import retrotranscription
    retrotranscription(cleaned_sequence)
else:
    raise ValueError("Your choice is unvalid.")