#-----------------------
# To do list
#-----------------------
# * Only start translation on Codon start AUG, and stop on Codon stop UAA,UGA,UAG
# * BLAST protein sequence using blastpy3: https://pypi.org/project/blastpy3/
#-----------------------------------------------------------------

# Test sequence : ATGGCTTCAAGTCCGCACTACGAATGGCAGCTTGAGGCTCCAGGTCGG -> AUGGCUUCAAGUCCGCACUACGAAUGGCAGCUUGAGGCUCCAGGUCGG -> MASSPHYEWQLEAPGR
# Test sequence for BLAST: gcgagcagcccgccgtatgaatggcagcaggaagcggtggaaccgggc -> ASSPPYEWQQEAVEPG -> https://www.ncbi.nlm.nih.gov/protein/WP_276301433.1?report=genbank&log$=protalign&blast_rank=1&RID=6HYUP7D5013 (ubiquinol-cytochrome c reductase iron-sulfur subunit [Halorussus)

# Ask for initial sequence, set nature booleans and identify input's nature
initial_sequence = input("Input the sequence to manipulate: ")
from librarybioperso import sequence_cleanup, initiate, sequence_identification
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
    from librarybioperso import transcription
    transcription(cleaned_sequence)
elif choice == "2":
    from librarybioperso import translation
    translation(cleaned_sequence)
elif choice == '3':
    from librarybioperso import retrotranscription
    retrotranscription(cleaned_sequence)
else:
    raise ValueError("Your choice is unvalid.")


# save_file = open("sequence-proteique.txt", "w") # Dans répertoire contenant le script
# save_file.write("> Proteic sample. \n")
# i = 0
# for i in seq:
#     save_file.write(str(i))
# save_file.close()
