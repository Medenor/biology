# -*-coding:UTF-8 -*
import librarybioperso

code = input("Introduisez votre séquence : ")
code = code.upper()
code = code.replace("\r","")
code = code.replace("\n","")
for lettre in code:
    if lettre in "U":
        ADN = False
        print("La séquence introduite est une séquence d'ARN")
        break
    elif lettre in "T":
        ADN = True
        print("La séquence introduite est une séquence d'ADN")
        break
    else:
        continue
print("\n")


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
if choixARN == '2' : 
    nbcodon = len(code) / 3
    print("La séquence entrée est composée de ",nbcodon,"codons")
    print("La structure primaire de la protéine associée est : ")
    i = 0
    while i < (len(code)-2) :
        codon = librarybioperso.CodontoAA(code[i:i+3])
        i+=3
        
elif choixADN == '2':
    nbcodon = len(code) / 3
    print("La séquence entrée est composée de ",nbcodon,"codons")
    print("La structure primaire de la protéine associée est : ")
    i = 0
    while i < (len(code)-2) :
        codon = librarybioperso.CodontoAA(code[i:i+3])
        i+=3
else :
    print("")

## ---------------
# Comparaison
print("\n")
choixcomp = input("Souhaitez-vous comparer deux séquences ? Si oui, tapez 1, sinon tapez 2.")
if choixcomp =='1':  
    sequencetheo = input("Entrez la séquence référence théorique :")
    sequenceobs = input("Entra la séquence obtenue par le programme :")
    comparaison = librarybioperso.comparaisonsequences(sequencetheo,sequenceobs)
else:
    print("")
# Faire en sorte de ne commencer qu'à un codon start AUG
# Appeler le script de comparaison avec la séquence de BDD (pour vérifier si la transcription s'est faite correctement)
