#!/usr/bin/env python
#-*- coding: utf-8 -*-
 
import os
import random
 
def makeBenchmarkFile(bch_L,bchName):
	bch_str=""
	for i in range(0,len(bch_L)-1):
		bch_str += str(bch_L[i]) + " "
  
	bch_str += str(bch_L[-1])
	os.chdir("files")
	bchFile = open(bchName,"w")
	bchFile.write(bch_str)
	bchFile.close()
	os.chdir("../")
 
def randomBenchmark(bch_L,bchName,size):
	bchName += ".txt"
	print("\nYou have chosen to make it randomly\n")
	for i in range(0,size):
		bch_L.append(random.randint(0,1))
 
	makeBenchmarkFile(bch_L,bchName)
      
def handMadeBenchmark(bch_L, bchName):
	print("\nYou have chosen to make it by hand\n")
	print("Please, you have to enter a succession of only 1 and 0 without spaces \n")
	bch_str = str(raw_input("Enter here : "))
	bch_str_new = ""
      
	for i in range(0,len(bch_str)):
		if (bch_str[i] =='1' or bch_str[i] == '0'):
			bch_L.append(int(bch_str[i]))
			bch_str_new += bch_str[i]+" "
      
	bchName += ".txt"
  
	os.chdir("files")
	bchFile = open(bchName,"w")
	bchFile.write(bch_str_new)
	bchFile.close()
	os.chdir("../")
  
def load_bch(bch_L,bchName):
	os.chdir("files")
	bchFile = open(bchName,"r")
	bch_str = bchFile.read()
	bchFile.close()
	os.chdir("..")

	for i in range(0,len(bch_str)):
		if (bch_str[i] == '0' or bch_str[i] =='1') :
			bch_L.append(int(bch_str[i]))

def error(text,list,element):
	new_element = element

	while new_element not in list:
		new_element = raw_input(text)		

	return int(new_element)

def convertor(list):
	for i in range(0,len(list)):
		list[i] = str(list[i])

	return list
		

def benchmarks(bch_L,bchName,size):
	bchName += ".txt"
        pattern = []
	patterns = []
	bit = convertor([0,1])					#Liste de caractere qui permettra de  determiner si le nombre saisi est bien un nombre binaire 
	length = convertor(range(0,size))			#Liste de caractere qui permettra de determiner si le nombre saisi est contenu dans la longueur de la sequence
	choice = convertor([1,2,3,4])				#Liste de caractere qui permettra de determiner si le choix selectionne est valide	
	sum_pattern = 0
	longest = 0


	pattern_nb = raw_input("How many patterns do you want to recognize ?")		#Nombre de patterns
	pattern_nb = error("ValueError! How many patterns do you want to recognize ?",length,pattern_nb)

	for i in range(0,pattern_nb):
		pattern_length = raw_input("How long is the pattern you want to recognize ?")         #Longueur des patterns
        	pattern_length = error("ValueError! How long is the pattern you want to recognize ?",length,pattern_length)
		
		pattern_choice = raw_input("Do you want a random pattern (1 or 2) or create your own (3 or 4)?")	#Ecriture du pattern
		pattern_choice = error("ValueError! Do you want a random pattern (1 or 2) or create your own (3 or 4)?",choice,pattern_choice)	
		
		pattern_nb_bis = raw_input("How many times do you want it to appear ?")          #Nombre d'apparition
        	pattern_nb_bis = error("ValueError! How many times do you want it to appear ?",length,pattern_nb_bis)
	
		sum_pattern = sum_pattern + pattern_nb_bis

		
		
		if pattern_length > longest:
			longest = pattern_length 	

		if sum_pattern*longest>size:
			print("ValueError! ")


		if pattern_choice == 1 or pattern_choice == 2:
			for i in range(0,pattern_length):		
				pattern = pattern + [random.randint(0,1)]
				
			patterns = patterns + [pattern] 
		

		elif pattern_choice == 3 or pattern_choice == 4:
			a = 0

			while a == 0:	
				b = 1
				pattern_str = raw_input("Type your pattern : ")
				pattern_str = list(pattern_str)
			
				if len(pattern_str)!=pattern_length:
					b = 0

				for i in pattern_str:	
					temp_pattern = str(error("ValueError! Wrong pattern enter 0",bit,i))
				
					print(temp_pattern)	
					if i != temp_pattern:
						b = 0
						break						

					else:
						pattern = pattern + [int(i)] 
					
				if b == 1:
					a = 1		
							
			patterns = patterns + [pattern]			

	space_choice = raw_input("Do you want a regular space (1 or 2) between each pattern or not (3 or 4)?")
	space_choice = error("ValueError! Do you want a regular space (1 or 2) between each pattern or not (3 or 4)?",choice,space_choice)

	space = []	#Liste qui contient la longueur de chacuns des espaces entre les patterns 
	
	space_choice_bis = raw_input("Do you want to set the patterns randomly in the sequence (1 or 2) or not (3 or 4)")
	space_choice_bis = error("ValueError! Do you want to set the patterns randomly in the sequence (1 or 2) or not (3 or 4) ?",choice,space_choice_bis)

	if space_choice == 1 or space_choice == 2:	
		space_length = raw_input("How long must be the space between the patterns ?")
		space_length = error("ValueError! How long must be the space between the patterns ?",length,space_length) 
		
		while space_length*sum_pattern>size:
			space_length = raw_input("ValueError! How long must be the space between the patterns ?")
			space_length = error("ValueError! How long must be the space between the patterns ?",length,space_length) 

			
		space = (size/(space_length+pattern_length))*[space_length]

	elif space_choice == 3 or space_choice == 4:		#Creation d'une liste avec des longueurs d'espaces aleatoires compris entre 0 et la taille a laquelle on soustrait la somme des espaces deja present dans la liste et la longueur du pattern
		sum_space = 0
		while sum_space < size-sum_space-sum_pattern*longest:	
			space_length = random.randint(0,size-sum_space-sum_pattern*longest)			
			sum_space += space_length
			space = space + [space_length]		
	
	space_pattern_choice  = raw_input("What do you want between patterns : 0000(1), 1111(2), 0101(3) or random (4)?")
	space_pattern_choice = error("ValueError! What do you want between patterns : 0000(1), 1111(2), 0101(3) or random (4)?",choice,space_pattern_choice)

	space_counter = 0		#Compte le nombre d'elements de l'espace insere dans la sequence  
	space_counter_bis = 0		#Compte le nombre d'elements de la liste space qui ont ete insere

	pattern_counter = 0
	pattern_counter_bis = 0

	

	while len(bch_L)<size:
		if space_counter_bis<len(space) and space_counter == space[space_counter_bis]:
			if space_choice_bis == 0:
				rand = random.randint(0,len(patterns)-1)
                        	for j in range(0,len(patterns[rand])):
                                	bch_L.append(patterns[rand][j])
			
			else :
				if pattern_counter_bis == space[0]/pattern_nb:
					pattern_counter +=1 
					pattern_counter_bis = 0
				
				if pattern_counter >=len(patterns):
					pattern_counter = 0
					
				for j in range(0,len(patterns[pattern_counter])):
					bch_L.append(patterns[pattern_counter][j])
			
			pattern_counter_bis += 1
			space_counter = 0
			space_counter_bis += 1
		
		else:
			if space_counter_bis>=len(space):	#Selection de la longueur de l'espace:si le compteur d'espace est superieur a la longueur de la liste contenant les espaces on va jusqu'u bout de la chaine sinon on prend l'espace suivant dans la liste space
				nb = size - len(bch_L)
			else:
				nb = space[space_counter_bis]				
			
			if space_pattern_choice == 1:		#0000...
				for j in range(0,nb):
					bch_L.append(0)
					space_counter += 1
			
			elif space_pattern_choice == 2:		#1111...
				for j in range(0,nb):
					bch_L.append(1)
					space_counter += 1
					
			elif space_pattern_choice == 3:		#1010...
				for j in range(0,nb):
					if j%2 == 0:
						bch_L.append(0)
					else:
						bch_L.append(1)
					space_counter += 1
				
			elif space_pattern_choice == 4:		#Random
                                for j in range(0,nb):
                                        bch_L.append(random.randint(0,1))
					space_counter += 1			
			
	while len(bch_L)!=size:
		bch_L.pop()

	makeBenchmarkFile(bch_L,bchName)





