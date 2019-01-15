#-*- coding: utf-8 -*-
#
# 	Created on 05/03/2018.
#   Copyright © 2017 FELIX CHOI - KARL MONGOSSO - JORDY AJANOHOUN. 
#	All rights reserved.
#
#====================================================
#
#
#				Projet Pile ou Face:
#
#	 FELIX CHOI - KARL MONGOSSO - JORDY AJANOHOUN
#
#
#			-Fonctions de predictions-
#
#
#
#====================================================
#
#	Quelques modules :
from random import randint




#====================================================


#convert binary to decimal
def convert(binary):
	binary.reverse()
	#print(binary)
	decimal = 0
	for i in range(0,len(binary)) :
		decimal = decimal + (2**i)*binary[i]
	return decimal



def n_bits_pattern_basic(historic,turn,n):
	#initilization of memory, the table that will count each pattern in the historic
	memory= []
	for i in range(0,2**n):
		memory.append(0)

	if turn >= n : #turn must be higher than the pattern evaluation
		#evaluation of each pattern in historic
		for k in range(n-1,turn):
			#generate a binary number in a list
			binary = []
			for b in range(0,n):
				binary.append(historic[k-n+b])

			index= convert(binary)
			memory[index] = memory[index]+1
		binary = []
		print(binary)

		#evaluation of the last pattern wich the last number is to predict
		for b in range(0,n-1):
			binary.append(historic[turn-n+b+1])


		if memory[convert(binary)*2] > memory[convert(binary)*2 + 1] :
			return 0
		else :
			return 1
	else :
		return randint(0,1)



def n_bits_pattern_Memory(historic,turn,n,memory):
	#initilization of bitsTab, the table that will count each pattern in the historic
	bitsTab= []
	for i in range(0,2**n):
		bitsTab.append(0)

	if turn >= n : #turn must be higher than the pattern evaluation
		if (turn <= memory):
			#evaluation of each pattern in historic
			for k in range(n-1,turn):
				#generate a binary number in a list
				binary = []
				for b in range(0,n):
					binary.append(historic[k-n+b])

				index= convert(binary)
				bitsTab[index] = bitsTab[index]+1
			binary = []
			#print(binary)
		else:
			#evaluation of each pattern in historic
			for k in range(n-1,memory):
				#generate a binary number in a list
				binary = []
				for b in range(0,n):
					binary.append(historic[k-n+b])

				index= convert(binary)
				bitsTab[index] = bitsTab[index]+1
			binary = []
			#print(binary)
			for k in range(memory, turn):
				binary = []
				#generate a binary number in a list
				for b in range(0,n):
					binary.append(historic[k-memory+b])
				index= convert(binary)
				bitsTab[index] = bitsTab[index]-1
				binary = []
				#generate a binary number in a list
				for b in range(0,n):
					binary.append(historic[k-n+b])
				index= convert(binary)
				bitsTab[index] = bitsTab[index]+1


		#evaluation of the last pattern wich the last number is to predict
		binary = []
		for b in range(0,n-1):
			binary.append(historic[turn-n+b+1])


		if bitsTab[convert(binary)*2] > bitsTab[convert(binary)*2 + 1] :
			return 0
		else :
			return 1
	else :
		return randint(0,1)


"""def predi_generator(historic):
	predic =[]

	for i in range(0,len(historic)):
		pred.append(n_bits_pattern_Memory(historic,i,n,memory))

	return predic"""

def result(historic, prediction ):
	"""cette fonction renvoie le nombre de bonne predicion a partir d'une liste de predictions faite"""
	compteur = 0
	for i in range(0, len(prediction)):

		if prediction[i] == historic[i]:
			compteur += 1

	return compteur

def all_bits_pattern_Memory(historic,turn,memory):
	"""cette fonction renvoie une prediction 1 ou 0 en evaluant le meilleur pattern
	c'est l'extention de la fonction n_bits_pattern ppur tout les patterns"""

	########## test de tous les patterns (on prend pour l'instant que entre 2 et 10) #######
	list_of_predictions = []
	for n in range(2,5):
		prediction = []

		for i in range(0, turn):
			prediction.append(n_bits_pattern_Memory(historic,i,n,memory))
		list_of_predictions.append(prediction)

	

	########## traitement des simulations faites pour tous les patterns #########
	
	list_of_results = []

	for pred in list_of_predictions :
		list_of_results.append(result(historic, pred))

	########## selection deu meilleur resultat 
	
	result_max = 0
	index_max = 0
	for index in range(0, len(list_of_results) ):
		
		if list_of_results[index] > result_max :
			result_max = list_of_results[index]
			index_max = index
			

	index_max += 2 #les paterns on un decalage de 2 puisque on commence que au pattern de taille 2

	guess = n_bits_pattern_Memory(historic, turn, index_max, memory)

	return guess





def all_bits_pattern_Memory_optimised(historic,turn,memory,list_of_predictions):
	"""cette fonction renvoie une prediction 1 ou 0 en evaluant le meilleur pattern
	c'est l'extention de la fonction n_bits_pattern ppur tout les patterns"""

	"""optimisation: la majeur partie des calculs se faisaient dans la premiere boucle où l'on simulait chaque pattern, 
	pour chaque tour, et comparer ces simulations avec l'historic. Cela marchait mais n'etait pas du tout efficace, 
	dans cette version les simulations ne sont pas recalculées a chaque fois qu'on fait appel a la fonction. Elle sont enregistrées
	et mises en entrée/sortie"""

	########## test de tous les patterns (on prend pour l'instant que entre 2 et 10) et modif de list_of_predictions #######

	print(turn)

	for n in range(2,5):
		
		if len(list_of_predictions) < len(range(2,5)): #3 est temporaire pour le test,  il dependra d'un parametre futur qui sera la taille max des patterns etudiés
			list_of_predictions.append([n_bits_pattern_Memory(historic,turn,n,memory)])

		else:
			list_of_predictions[n-2].append(n_bits_pattern_Memory(historic,turn,n,memory))


	########## traitement des simulations faites pour tous les patterns #########

	list_of_results = []
	
	for pred in list_of_predictions:
		print("pred:")
		print(pred)
		print("historic:")
		print(historic)
		list_of_results.append(result(historic,pred))    #calcul les bonnes predictions des simulations
		print(list_of_results)

	########## selection deu meilleur resultat 
	
	result_max = 0
	index_max = 0

	for index in range(0, len(list_of_results) ):
		
		if list_of_results[index] > result_max :
			result_max = list_of_results[index]
			index_max = index
			

	index_max += 2 #les patterns ont un decalage de 2 puisque on commence que au pattern de taille 2
	guess = n_bits_pattern_Memory(historic, turn, index_max, memory)

	return guess, list_of_predictions
















