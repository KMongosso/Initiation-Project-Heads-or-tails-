#-*- coding: utf-8 -*-
from random import randint
from class_Predictor import *

#test :

########### oueveture de fichier #####
file = open("4.txt")
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
for i in range(1,int(file[0]) ):
	historic.append( int(file[i]) )


#####################


########### creation de la liste des predictions faites #######
predictor = Predictor(memory)
pred = []

for i in range(1,len(historic)+1):

	prediction = predictor.all_bits_pattern_Memory_optimised(historic[:i])
	#prediction = all_bits_pattern_Memory(historic,i,memory)
	#print(predictor)
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
print(predictor)











