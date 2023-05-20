# séquence test : AUGAACUUCGCAGGAUGAUGA -> MNFAG STOP STOP
code = input("Introduisez votre séquence : ")
code = code.upper().strip()
for lettre in code:
    if lettre in "U":
        ADN = False
        print("La séquence introduite est une séquence d'ARN \n")
        break
    elif lettre in "T":
        ADN = True
        print("La séquence introduite est une séquence d'ADN \n")
        break
    else:
        continue


if ADN == False :
    choixADN = 0
    choixARN = input("Pour faire une rétrotranscription, entrez 1. Pour faire une traduction d'ARNm, entrez 2 : ")
    if choixARN == '1' :
        print("La séquence d'ADN correspondante est:")
        for lettre in code:
            if lettre in "U":
                print("T", end='')
            else:
                print(lettre, end='')
    else:
        print("")
        
else:
    choixARN = 0
    choixADN = input("Pour faire une transcription, entrez 1. Pour faire une transcription et une traduction, entrez 2 : ")
    if choixADN == '1':
        print("La séquence d'ARN correspondante est:")
        for lettre in code:
            if lettre in "T":
                print("U", end='')
            else:
                print(lettre, end='')
    else:
        code = code.replace("T","U")


## ---------------
#Détermination de la structure protéique primaire de la séquence introduite
if choixARN == '2' or choixADN == '2' : 
    from librarybioperso import CodontoAA
    nbcodon = int(len(code) // 3)
    seq = []
    print("La séquence entrée est composée de",nbcodon,"codons")
    print("La structure primaire de la protéine associée est : ")
    for i in range(0, len(code), 3):
        codon = code[i:i+3]
        if len(codon) == 3:
            aa = CodontoAA(codon)
            seq.append(aa)
    print(seq)

else :
    print("")

save_file = open("sequence-proteique.txt", "w") # Dans répertoire contenant le script
save_file.write("> Proteic sample. \n")
i = 0
for i in seq:
    save_file.write(str(i))
save_file.close()

## ---------------
# Comparaison
print("\n")
choixcomp = input("Souhaitez-vous comparer deux séquences ? Si oui, tapez 1, sinon tapez 2.")
if choixcomp =='1':  
    from librarybioperso import compare_sequences
    expected_sequence = input("Entrez la séquence référence théorique :")
    observed_sequence = input("Entra la séquence obtenue par le programme :")
    comparaison = compare_sequences(expected_sequence,observed_sequence)
    print(comparaison)
else:
    print("")
