# -*-coding:Latin-1 -*

caryotype = input("Entrez le nombre de chromosomes de l'individu:")
caryotype = int(caryotype)
if caryotype > 44 and caryotype <= 49:
    humanite = input("Le caryotype �tudi� est-il issus d'un �tre humain (Oui = 1 ; Non = 0)?")
    humanite = int(humanite)
    if caryotype == 46 and humanite == 1 :
        print("Le caryotype entr� est humain")
    elif caryotype != 46 and humanite == 1 :
        print("Le caryotype entr� est issus d'un individu au caryotype mut�")
    else:
        print("Le caryotype entr� n'est pas humain")    
else:
    print("Le caryotype entr� n'est pas humain")
    
