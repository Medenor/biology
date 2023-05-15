import sys
sys.path.insert(0, 'C:/Users/Admin/Desktop/biopython-1.60/build/py3.3/Bio/Blast/')
import NCBIWWW

my_sequence = input("En+tre la séquence à BLASTer :")
print("Recherche en cours de",my_sequence)
result = NCBIWWW.qblast("blastp", "nr", my_sequence, format_type="Text")
print (result.read())

# http://www.dalkescientific.com/writings/NBN/blast_searching.html
# http://www.biotnet.org/sites/biotnet.org/files/documents/25/biopython_blast.pdf
# Séquence test : http://www.uniprot.org/uniprot/H9FX69.fasta

save_file = open("my_blast.txt", "w") # Das G:\Documents\SkyDrive\Scripts python\tests
save_file.write(result.read())
save_file.close()
result.close()
result = open("my_blast.txt")
