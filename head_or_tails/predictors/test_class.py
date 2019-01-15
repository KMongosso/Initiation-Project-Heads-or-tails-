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




class Predictor:
	"""cette oblet prédit un bit 1 ou 0 en fonction des données recuperées"""

	def __init__(self,Memory):
		
		self.memory   = Memory
		self.list_of_predictions = []
		self.recurentPattern = [[],0] #[0] is for the pattern and [1] is for the recurence number
		self.bitsTab = [[]]


	def __str__(self):
		memory = "memory = "+ str(self.memory) + "\n"
		#list_of_predictions = "list_of_predictions = " + str(self.list_of_predictions) + "\n"
		print(self.recurentPattern[0])
		maxpattern = "most recurent pattern : " +str(self.recurentPattern[0]) + "  occured " + str(self.recurentPattern[1])
		return memory+maxpattern


	#convert binary to decimal
	def convert(self,binary):
		binary.reverse()
		#print(binary)
		decimal = 0
		for i in range(0,len(binary)) :
			decimal = decimal + (2**i)*binary[i]
		return decimal

	def convertReverse(self, decimal, bitsTab, n):
		binary = []
		if decimal != 0:
			while decimal >= 1 :
				
				if (decimal % 2) == 0 :
					binary.append(0)
				else:
					binary.append(1)
					decimal = decimal -1
				decimal = decimal/2
				
		else:
			binary.append(0)

		reste = len(binary)		

		for i in range(0, n - reste) :
			binary.append(0)

		binary.reverse()
		return binary


	def maxpattern(self, bitsTab,n):

		for i in range(0,len(bitsTab)) :
			if bitsTab[i] > self.recurentPattern[1] :
				self.recurentPattern[0] = self.convertReverse(i, bitsTab, n) 
				self.recurentPattern[1] = bitsTab[i]



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

				index= self.convert(binary)
				memory[index] = memory[index]+1
			binary = []


			#evaluation of the last pattern wich the last number is to predict
			for b in range(0,n-1):
				binary.append(historic[turn-n+b+1])

			if memory[self.convert(binary)*2] > memory[self.convert(binary)*2 + 1] :
				return 0
			else :
				return 1
		else :
			return randint(0,1)



	def n_bits_pattern_Memory(self,historic,turn,n,memory,pattern):
		#initilization of bitsTab, the table that will count each pattern in the historic

		for i in range(0,2**n):
			self.bitsTab[n-2].append(0)

		if turn >= n : #turn must be higher than the pattern evaluation
			if (turn <= memory):
				#evaluation of the pattern just before turn (new pattern)
				#generate a binary number in a list
				binary = []
				for b in range(0,n):
					binary.append(historic[turn-1-n+b])

				index= self.convert(binary)
				self.bitsTab[n-2][index] = self.bitsTab[n-2][index]+1
				#print(binary)
			else:
				#evaluation of the pattern just before turn (new pattern)
				#generate a binary number in a list
					binary = []
					#generate a binary number in a list
					for b in range(0,n):
						binary.append(historic[turn-1-memory+b])
					index= self.convert(binary)
					self.bitsTab[n-2][index] = self.bitsTab[n-2][index]-1
					binary = []
					#generate a binary number in a list
					for b in range(0,n):
						binary.append(historic[turn-1-n+b])
					index= self.convert(binary)
					self.bitsTab[n-2][index] = self.bitsTab[n-2][index]+1


			if pattern == 1 :
				self.maxpattern(self.bitsTab[n-2],n)


			#evaluation of the last pattern wich the last number is to predict
			binary = []
			for b in range(0,n-1):
				binary.append(historic[turn-n+b+1])


			if self.bitsTab[n-2][self.convert(binary)*2] > self.bitsTab[n-2][self.convert(binary)*2 + 1] :
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

	def result(self,historic, prediction ):
		"""cette fonction renvoie le nombre de bonne predicion a partir d'une liste de predictions faite"""
		compteur = 0
		
		for i in range(0, len(prediction)):
			
			if prediction[i] == historic[i]:
				compteur += 1

		return compteur

	def all_bits_pattern_Memory(self,historic):
		"""cette fonction renvoie une prediction 1 ou 0 en evaluant le meilleur pattern
		c'est l'extention de la fonction n_bits_pattern ppur tout les patterns"""
		memory = self.memory
		turn = len(historic)-1

		########## test de tous les patterns (on prend pour l'instant que entre 2 et 10) #######
		list_of_predictions = []
		for n in range(2,5):
			prediction = []

			for i in range(0, turn):
				prediction.append(self.n_bits_pattern_Memory(historic,i,n,memory, 0))
			list_of_predictions.append(prediction)

		

		########## traitement des simulations faites pour tous les patterns #########
		
		list_of_results = []

		for pred in list_of_predictions :
			list_of_results.append(self.result(historic, pred))

		########## selection deu meilleur resultat 
		
		result_max = 0
		index_max = 0
		for index in range(0, len(list_of_results) ):
			
			if list_of_results[index] > result_max :
				result_max = list_of_results[index]
				index_max = index
				

		index_max += 2 #les paterns on un decalage de 2 puisque on commence que au pattern de taille 2

		guess = self.n_bits_pattern_Memory(historic, turn, index_max, memory, 1)

		return guess





	def all_bits_pattern_Memory_optimised(self,historic):
		"""cette fonction renvoie une prediction 1 ou 0 en evaluant le meilleur pattern
		c'est l'extention de la fonction n_bits_pattern ppur tout les patterns"""

		"""optimisation: la majeur partie des calculs se faisaient dans la premiere boucle où l'on simulait chaque pattern, 
		pour chaque tour, et comparer ces simulations avec l'historic. Cela marchait mais n'etait pas du tout efficace, 
		dans cette version les simulations ne sont pas recalculées a chaque fois qu'on fait appel a la fonction. Elle sont enregistrées
		et mises en entrée/sortie"""


		memory = self.memory
		turn = len(historic)-1 #les indices commences a 0 mais les tours a 1 (en tout cas ca marche paa sisnon)
		
		########## test de tous les patterns (on prend pour l'instant que entre 2 et 10) et modif de list_of_predictions #######
		pattern_interval = range(2,6)

		for n in pattern_interval:
			if len(self.bitsTab) < n :
				self.bitsTab.append([])
			
			if len(self.list_of_predictions) < len(pattern_interval): #3 est temporaire pour le test,  il dependra d'un parametre futur qui sera la taille max des patterns etudiés
				self.list_of_predictions.append([self.n_bits_pattern_Memory(historic,turn,n,memory, 0)])

			else:
				self.list_of_predictions[n-2].append(self.n_bits_pattern_Memory(historic,turn,n,memory, 0))


		########## traitement des simulations faites pour tous les patterns #########

		list_of_results = []
		
		for pred in self.list_of_predictions:

			list_of_results.append(self.result(historic,pred))    #calcul les bonnes predictions des simulations



		########## selection deu meilleur resultat 
		
		result_max = 0
		index_max = 0

		for index in range(0, len(list_of_results) ):
			
			if list_of_results[index] > result_max :
				result_max = list_of_results[index]
				index_max = index
				

		index_max += 2 #les patterns ont un decalage de 2 puisque on commence que au pattern de taille 2
		guess = self.n_bits_pattern_Memory(historic, turn, index_max, memory, 1)

		return guess


















