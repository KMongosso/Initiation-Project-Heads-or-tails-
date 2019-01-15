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

		self.n = 0
		self.guess = 0
		self.pattern_interval = range(2,10)
		self.memory   = []
		for i in range(2,len(self.pattern_interval)+3) :
			self.memory.append(Memory*i)
		
		self.list_of_predictions = []
		self.list_of_results = []
		self.recurentPattern = [[],0] #[0] is for the pattern and [1] is for the recurence number

		self.bitsTab = []
		for size in range(2,len(self.pattern_interval)+3):
			self.bitsTab.append([])
			for i in range(0,2**size):
				self.bitsTab[size-2].append(0)

		self.bitsError = self.bitsTab #ce qui va servir a detecter les changements brutaux de benchmark
		self.ZerosTabLoad = self.bitsTab #il est tard et je sais plus trop ce que je fais.. mais j'le fais et ca va marcher !
		self.pattern = 0 #conditon pour le pattern plus recurent: 1 au dernier element du benchmark, rien a voir avec le pattern enfait
		self.sizePattern = []
		


	def __str__(self):
		memory = "memory = "+ str(self.memory) + "\n"
		#list_of_predictions = "list_of_predictions = " + str(self.list_of_predictions) + "\n"
		print(self.recurentPattern[0])
		maxpattern = "most recurent pattern : " +str(self.recurentPattern[0]) + "  occured " + str(self.recurentPattern[1])
		bitsTab = "\n"+str(self.bitsTab)
		bitsError = "\n" + str(self.bitsError)
		return memory+maxpattern+str(self.sizePattern) + bitsTab + bitsError


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



	"""def changeMemory(self,turn):
		if turn <=150:
			self.memory = 10
			return
		elif turn <= 300:
			self.memory = 40 
			return
		elif turn <= 500:
			self.memory = 70

		elif turn <= 1000 :
			self.memory = 100

		elif turn <= 2000:
			self.memory = 150"""



	def maxpattern(self, bitsTab,n):

		for i in range(0,len(bitsTab)) :
			if bitsTab[i] > self.recurentPattern[1] :
				self.recurentPattern[0] = self.convertReverse(i, bitsTab, n) 
				self.recurentPattern[1] = bitsTab[i]



	def n_bits_pattern_basic(self, historic,n):
		#initilization of memory, the table that will count each pattern in the historic
		#self.bitsTab= []  # le memory ici ne correspond pas a la memoire prise de l'historic
		turn = len(historic)
		#for i in range(0,2**n):
			#self.bitsTab.append(0)

		if turn >= n : #turn must be higher than the pattern evaluation
			#evaluation of each pattern in historic
			for k in range(n-1,turn):
				#generate a binary number in a list
				binary = []
				for b in range(0,n):
					binary.append(historic[k-n+b])

				index= self.convert(binary)
				self.bitsTab[index] = self.bitsTab[index]+1
			binary = []


			#evaluation of the last pattern wich the last number is to predict
			for b in range(0,n-1):
				binary.append(historic[turn-n+b+1])

			if self.bitsTab[self.convert(binary)*2] > self.bitsTab[self.convert(binary)*2 + 1] :
				return 0
			else :
				return 1
		else :
			return randint(0,1)



	def n_bits_pattern_Memory(self,historic,n):
		#initilization of bitsTab, the table that will count each pattern in the historic
		turn = len(historic)
		#print("self =" + str(self.n))
		#print(n)
		
		if self.pattern == 2:
			memory = self.memory
		else :
			memory = self.memory[n-2]

		"""if len(self.bitsTab )== 0:
			for k in range(2,n+1):
				self.bitsTab.append([])
				self.bitsError.append([])
		if turn < 1:
			for i in range(0,2**n):
				self.bitsTab[n-2].append(0)
				self.bitsError[n-2].append(0)"""


		#BitsTab use pattern as binary number as index so we use n, the size of pattern but size begin at 2 so 2 must be substrated to n 

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
					if self.bitsTab[n-2][index] > 0:
						self.bitsTab[n-2][index] = self.bitsTab[n-2][index]-1
					binary = []
					#generate a binary number in a list
					for b in range(0,n):
						binary.append(historic[turn-1-n+b])
					index= self.convert(binary)
					self.bitsTab[n-2][index] = self.bitsTab[n-2][index]+1


			if self.pattern == 1 :
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
		
		for i in range(0, len(historic)):
			
			if prediction[i] == historic[i]:
				compteur += 1

		return compteur



	def all_bits_pattern_Memory(self,historic):
		"""cette fonction renvoie une prediction 1 ou 0 en evaluant le meilleur pattern
		c'est l'extention de la fonction n_bits_pattern ppur tout les patterns"""
		memory = self.memory
		turn = len(historic)

		########## test de tous les patterns (on prend pour l'instant que entre 2 et 10) #######
		
		list_of_predictions = []
		for n in pattern_interval:
			if len(self.bitsTab) < n :
				self.bitsTab.append([])
			prediction = []

			for i in range(0, turn):
				prediction.append(self.n_bits_pattern_Memory(historic,n))
			list_of_predictions.append(prediction)

		

		########## traitement des simulations faites pour tous les patterns #########
		
		list_of_results = [] #il y a autant de liste de resultats que de simulations des erreurs <voir ErrorDetector>

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

		guess = self.n_bits_pattern_Memory(historic, index_max)

		return guess


	def Error_detector(self,historic,ErrorFactor):
		"""fonction a utlisiser au tout debut de all_bit_pattern_oprtimised, pour la detection d'erreur consecutive, 
		elle se met au debut car elle va modifier BitsTab"""

		Bch_size = len(historic)-1
		if self.guess != historic[Bch_size]:
			binary = historic[Bch_size-self.n:Bch_size]
			index = self.convert(binary)
			n= self.n - 2
			self.bitsError[n][index] += 1
			if self.bitsError[n][index] >= ErrorFactor:
				self.bitsTab[n][index] = 0
				self.bitsError[n][index] = 0






	def all_bits_pattern_Memory_optimised(self,historic,ErrorFactor):
		"""cette fonction renvoie une prediction 1 ou 0 en evaluant le meilleur pattern
		c'est l'extention de la fonction n_bits_pattern ppur tout les patterns"""

		"""optimisation: la majeur partie des calculs se faisaient dans la premiere boucle où l'on simulait chaque pattern, 
		pour chaque tour, et comparer ces simulations avec l'historic. Cela marchait mais n'etait pas du tout efficace, 
		dans cette version les simulations ne sont pas recalculées a chaque fois qu'on fait appel a la fonction. Elle sont enregistrées
		et mises en entrée/sortie"""

		######## modif de BitTab lié aux erreurs ###########
		if len(historic) != 0 & ErrorFactor > 0:
			self.Error_detector(historic,ErrorFactor)
		####################################################

		#ErrorFactor -= 1

		memory = self.memory

		turn = len(historic) 
		
		########## test de tous les patterns (on prend pour l'instant que entre 2 et 10) et modif de list_of_predictions #######
		pattern_interval = self.pattern_interval



		for n in self.pattern_interval:
			if len(self.bitsTab) < n :
				self.bitsTab.append([])
				self.bitsError.append([])
			
			if len(self.list_of_predictions) < len(pattern_interval): #3 est temporaire pour le test,  il dependra d'un parametre futur qui sera la taille max des patterns etudiés
				self.list_of_predictions.append([self.n_bits_pattern_Memory(historic,n)])

			else:
				self.list_of_predictions[n-2].append(self.n_bits_pattern_Memory(historic,n))


		########## traitement des simulations faites pour tous les patterns #########

		self.list_of_results = [] #definir ErrorFactor a 0 si on utilise pas la detections d'erreurs
		
		for pred in self.list_of_predictions:

			self.list_of_results.append(self.result(historic,pred))    #calcul les bonnes predictions des simulations



		########## selection deu meilleur resultat 
		
		result_max = 0
		index_max = 0

		for index in range(0, len(self.list_of_results) ):
			
			if self.list_of_results[index] > result_max :
				result_max = self.list_of_results[index]
				index_max = index
				

		self.n = index_max + 2 #les patterns ont un decalage de 2 puisque on commence que au pattern de taille 2
		self.sizePattern.append(self.n)

		self.pattern = 1 #condition pour afficher le pattern le plus recurrent
		self.guess = self.n_bits_pattern_Memory(historic, self.n)

		return self.guess


	#def One_for_All(self,historic,ErrorFactor=0):
		"""cette fonction renvoie une prediction 1 ou 0 en evaluant le meilleur pattern
		c'est l'extention de la fonction n_bits_pattern ppur tout les patterns"""

		"""optimisation: la majeur partie des calculs se faisaient dans la premiere boucle où l'on simulait chaque pattern, 
		pour chaque tour, et comparer ces simulations avec l'historic. Cela marchait mais n'etait pas du tout efficace, 
		dans cette version les simulations ne sont pas recalculées a chaque fois qu'on fait appel a la fonction. Elle sont enregistrées
		et mises en entrée/sortie"""

		######## modif de BitTab lié aux erreurs ###########
		"""if len(historic) != 0 & ErrorFactor > 0:
			self.Error_detector(historic,ErrorFactor)
		####################################################

		#ErrorFactor -= 1

		memory = self.memory

		turn = len(historic) 
		
		########## test de tous les patterns (on prend pour l'instant que entre 2 et 10) et modif de list_of_predictions #######
		pattern_interval = self.pattern_interval
		memory_interval = range(1,400)


		for memo in memory_interval:
			if len(self.list_of_predictions) < len(memory_interval):
				self.list_of_predictions.append([])

			for n in self.pattern_interval:
				if len(self.bitsTab) < n :
					self.bitsTab.append([])
					self.bitsError.append([])
				
				if len(self.list_of_predictions[memo-1]) < len(pattern_interval): #3 est temporaire pour le test,  il dependra d'un parametre futur qui sera la taille max des patterns etudiés
					self.list_of_predictions[memo-1].append([self.n_bits_pattern_Memory(historic,n)])

				else:
					self.list_of_predictions[memo-1][n-2].append(self.n_bits_pattern_Memory(historic,n))


		########## traitement des simulations faites pour tous les patterns #########

		#self.list_of_results = [] #definir ErrorFactor a 0 si on utilise pas la detections d'erreurs
		result_max = 0
		index_max  = 0
		memory_max = 10
		result_mem = 0
		print(self.list_of_predictions)
		
		for k in memory_interval:
			self.list_of_results = [] #definir ErrorFactor a 0 si on utilise pas la detections d'erreurs
			
			for pred in self.list_of_predictions[k-1]:

				self.list_of_results.append(self.result(historic,pred))    #calcul les bonnes predictions des simulations

			########## selection deu meilleur resultat 
			
			for index in range(0, len(self.list_of_results) ):
				
				if self.list_of_results[index] > result_max :
					result_max = self.list_of_results[index]
					index_max = index

			if result_mem < result_max :
				result_mem = result_max
				memory_max = k

				

		self.n = index_max + 2 #les patterns ont un decalage de 2 puisque on commence que au pattern de taille 2
		self.sizePattern.append(self.n)
		self.memory = memory_max
		print(self.memory)
		print(self.n)

		self.pattern = 2 #condition pour afficher le pattern le plus recurrent, 2 pour une memory fixe
		self.guess = self.n_bits_pattern_Memory(historic, self.n)

		return self.guess""" #-> un echec


def surchMemory(historic):
	memory_interval = range(5,400)
	res_memory = 0
	success = 0 
	success_max =0
	res_L = []
	for memory in memory_interval :
		pred = Predictor(memory)
		for turn in range(0,len(historic)):
			res_L.append(pred.all_bits_pattern_Memory_optimised(historic[:turn],0))
		success = pred.result(historic,res_L)
		if success > success_max:
			success_max = success
			res_memory = memory
	return res_memory

def OneforAll(historic):
	predictor = Predictor(surchMemory(historic))
	return predictor.all_bits_pattern_Memory_optimised(historic,0)

	


	



		



















