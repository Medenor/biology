def CodontoAA(codon):
    global X
    if codon == 'AUG':
        X = "M"
    elif codon == 'GCU' or codon == 'GCC' or codon == 'GCA' or codon == 'GCG':
        X = "A"
    elif codon == 'UGU' or codon == 'UGC':
        X ="C"
    elif codon == 'GAU' or codon == 'GAC':
        X ="D"
    elif codon == 'GAA' or codon == 'GAG':
        X ="E"
    elif codon == 'UUU' or codon =='UUC':
        X ="F"
    elif codon == 'GGU' or codon =='GGC' or codon =='GGA' or codon =='GGG':
        X ="G"
    elif codon == 'CAU' or codon =='CAC':
        X ="H"
    elif codon == 'AUU' or codon =='AUC' or codon =='AUA':
        X ="I"
    elif codon == 'AAA' or codon =='AAG':
        X ="K"
    elif codon == 'UUA' or codon =='UUG' or codon =='CUU' or codon =='CUC' or codon =='CUA' or codon =='CUG':
        X ="L"
    elif codon == 'AAU' or codon == 'AAC':
        X ="N"
    elif codon == 'CCU' or codon =='CCC' or codon =='CCA' or codon =='CCG':
        X ="P"
    elif codon == 'CAA' or codon =='CAG':
        X ="Q"
    elif codon == 'CGU' or codon =='CGC' or codon =='CGA' or codon =='CGG' or codon =='AGA' or codon =='AGG':
        X ="R"
    elif codon == 'UCU' or codon =='UCC' or codon =='UCA' or codon =='UCG' or codon =='AGU' or codon =='AGC':
        X ="S"
    elif codon == 'ACU' or codon =='ACC' or codon =='ACA' or codon =='ACG':
        X ="T"
    elif codon == 'GUU' or codon =='GUC' or codon =='GUA' or codon =='GUG':
        X ="V"
    elif codon == 'UGG':
        X ="W"
    elif codon == 'UAU' or codon == 'UAC':
        X ="Y"
    elif codon == 'UAA' or codon == 'UAG' or codon == 'UGA':
        X ="[STOP]"
    else:
        print("Erreur")

def comparaisonsequences(a,b):
    a = a.replace("\r","")
    a = a.replace("\n","")
    b = b.replace("\r","")
    b = b.replace("\n","")
    if a == b:
        print("Les séquences sont identiques.")
    else :
        print("Les séquences sont différentes.")
