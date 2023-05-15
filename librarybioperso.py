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


def CodontoAA(codon):
    if codon in codon_table:
        aa = codon_table[codon]
        return aa
    else:
        raise ValueError("Codon invalide")


def compare_sequences(seq1, seq2):
    seq1 = seq1.strip()
    seq2 = seq2.strip()
    if seq1 == seq2:
        return "Les séquences sont identiques."
    else:
        return "Les séquences sont différentes."
