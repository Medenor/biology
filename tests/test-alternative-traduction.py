import testlib

code = input("Introduisez votre séquence : ")
code = code.upper()
i = 0
while i < (len(code)-2) :
    codon = testlib.CodontoAA(code[i],code[i+1],code[i+2])
    i += 3


# séquence test : AUGAACUUCGCAGGAUGAUGA -> MNFAG STOP STOP
