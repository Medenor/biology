# -*-coding:UTF-8 -*
#---------------------------------------
# Classification phénotypique d'organismes bactériens
#---------------------------------------
# Version actuelle : 1.0
#-------------------------------
#-----------------------
# Description 
#-----------------------
# Ce script en Python vous permet, sur base du phénotype bactérien, de classer un microorganisme dans la division auquel il appartient (selon la classification phylogénétique).
# Il ne prend pas en charge ni les Eucaryotes, ni les Archaea (cependant, ces dernières pourraient être incorporées dans une future version).
#-------------------------------
#-----------------------
# Changelog
#-----------------------
# {1.0}
# - Création du script original permettant la classification jusqu'à la division des Eubacteria
#-------------------------------
#-----------------------
# To do list
#-----------------------
# * Objectif : classification de bactéries sur base de questions phénotypiques, pour aller au moins jusqu'à la division
# * Objectif bonus : classification supervisée ???
#-------------------------------
#-----------------------
# Légende des variables
#-----------------------
# nucleus : présence ou non d'un nucleus (distinction Eu-/Procaryotes)
# mureincellwall : présence ou non de muréine dans la paroi cellulaire (distinction Eubacteria/Archaea)
#-----------------------------------------------------------------


print("Une série de questions phénotypiques vont vous être posées. Répondez-y par oui (Y) ou par non (N)")
nucleus = input("L'organisme étudié possède-t-il un nucleus ? ")
if nucleus == 'Y' :
	print("L'organisme étudié est un Eucaryote, et n'est donc pas traitable par ce script de classification.")
else:
	mureincellwall = input("Y a-t-il de la muréine dans la paroi cellulaire ?")
	if mureincellwall == 'N':
		print("L'organisme étudié est une Archée, et n'est donc pas traitable par ce script de classification.")
	else:



