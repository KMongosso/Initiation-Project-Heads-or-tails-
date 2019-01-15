#-*- coding: utf-8 -*-
from random import randint
from predictors_functions import *

#test :

########### oueverture de fichier #####
file = open("4.txt")
file = file.read()
file = file.split(" ")

##########################

####### initialisation de variables #####

#choisir le pattern


historic = []
memory = 400

#####################

####### on choisit la liste a prevoir ( 60000 c'est trop)
"""partie optionnelle en fonction de la taille du benchmark"""
for i in range(1,int(file[0])) :
	historic.append( int(file[i]) )


#####################


########### creation de la liste des predictions faites #######

pred = []
for i in range(0,len(historic)):
	
	pred.append(all_bits_pattern_Memory(historic,i,memory))

####################

######### traitement des resultats #######
result = []
compteur = 0
for i in range(0, len(pred)) :
	if pred[i] == historic[i]:
		result.append("V")
		compteur = compteur + 1
	else:
		result.append("F")

print(result,compteur)
print(compteur/float(file[0]))







