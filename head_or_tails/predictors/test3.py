#-*- coding: utf-8 -*-
from random import randint
from predictors_functions import *

#test :

########### oueverture de fichier #####
file = open("9.txt")
file = file.read()
file = file.split(" ")

##########################

####### initialisation de variables #####

#choisir le pattern

n=2
historic = []
memory = 400

#####################

####### on choisit la liste a prevoir ( 60000 c'est trop)
"""partie optionnelle en fonction de la taille du benchmark"""
for i in range(1,10 ):
	historic.append( int(file[i]) )


#####################


########### creation de la liste des predictions faites #######

pred = []
list_of_predictions = []
for i in range(0,len(historic)):
	prediction, list_of_predictions = all_bits_pattern_Memory_optimised(historic,i,memory,list_of_predictions)
	#prediction = all_bits_pattern_Memory(historic,i,memory)

	pred.append(prediction)


####################
#print(list_of_predictions)
#print(pred)


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
print(str(100*compteur/float(file[0]))+"%")






