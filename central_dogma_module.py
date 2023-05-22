def initiate():
    global protein, DNA, RNA
    protein = False
    DNA = False
    RNA = False

def sequence_cleanup(seq):
    seq = seq.upper().strip()
    seq = seq.replace(" ", "")
    return seq

def translation(seq):
    seq = seq.replace("T","U") #Quick, by-default transcription to always apply function on RNA sequence
    seq_lenght = len(seq)
    codon_total = seq_lenght // 3
    print("Total number of codons in sequence is",codon_total)
    codon_table = {
    'AUG': 'M', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'UGU': 'C',
    'UGC': 'C', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'UUU': 'F',
    'UUC': 'F', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G', 'CAU': 'H',
    'CAC': 'H', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AAA': 'K', 'AAG': 'K',
    'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
    'AAU': 'N', 'AAC': 'N', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
    'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
    'AGA': 'R', 'AGG': 'R', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
    'AGU': 'S', 'AGC': 'S', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
    'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'UGG': 'W', 'UAU': 'Y',
    'UAC': 'Y', 'UAA': '[STOP]', 'UAG': '[STOP]', 'UGA': '[STOP]'
    }
    print("Primary sequence of proteins is: ")
    transcribed_seq = []
    for i in range(0, seq_lenght, 3):
        codon = seq[i:i+3]
        if codon in codon_table:
            aa = codon_table[codon]
            if aa == '[STOP]':
                break
            else:
                transcribed_seq.append(aa)
        else:
            raise ValueError("Invalid codon")
    str_transcribed_seq = ''.join(transcribed_seq) #FASTA conversion
    print(str_transcribed_seq)
    save_file = open("test.fasta", "w") # within same directory as main.py and current module
    save_file.write(str_transcribed_seq)
    save_file.close()


def compare_sequences(seq1, seq2):
    seq1 = seq1.strip()
    seq2 = seq2.strip()
    if seq1 == seq2:
        return "Les séquences sont identiques."
    else:
        return "Les séquences sont différentes."

def transcription(seq):
    seq = seq.replace("T","U")
    print("Transcribed sequence is ",seq)

def retrotranscription(seq):
    seq = seq.replace("U","T")
    print("Retrotranscribed sequence is ",seq)

def sequence_identification(seq):
    if 'M' in seq:
        print("Sequence is made of amino acids.")
        protein = True
    elif 'U' in seq:
        print("Sequence is made of RNA.")
        RNA = True
    elif 'T' in seq:
        print("Sequence is made of DNA.")
        DNA = True
    else:
        raise ValueError("Sequence is unknown. Please check your input.")
