from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

sequence_data = open("test.fasta").read()
result_handle = NCBIWWW.qblast("blastp", "nr", sequence_data)
E_VALUE_THRESH = 1e-20

with open('results.xml', 'w') as save_file:
  blast_results = result_handle.read()
  save_file.write(blast_results)

print(sequence_data)
E_VALUE_THRESH = 1e-20
for record in NCBIXML.parse(open("results.xml")):
    if record.alignments:
       print("\n")
       print("query: %s" % record.query[:100])
       for align in record.alignments:
                print("match: %s " % align.title[:100])