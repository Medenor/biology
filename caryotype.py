# -*-coding:Latin-1 -*

caryotype = input("Entrez le nombre de chromosomes de l'individu:")
caryotype = int(caryotype)
if caryotype > 44 and caryotype <= 49:
    humanite = input("Le caryotype étudié est-il issus d'un être humain (Oui = 1 ; Non = 0)?")
    humanite = int(humanite)
    if caryotype == 46 and humanite == 1 :
        print("Le caryotype entré est humain")
    elif caryotype != 46 and humanite == 1 :
        print("Le caryotype entré est issus d'un individu au caryotype muté")
    else:
        print("Le caryotype entré n'est pas humain")    
else:
    print("Le caryotype entré n'est pas humain")
    
