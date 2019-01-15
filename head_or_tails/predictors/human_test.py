#-*- coding: utf-8 -*-
from random import randint
from predictors_functions import *

#test :


historic = []
turn = 0
memory = 400
compteur = 0

while turn >= 0:
	valeur = int(raw_input("choisissez 1 ou 0"))
	historic.append(valeur)
	guess = all_bits_pattern_Memory(historic,turn,memory)
	turn += 1
	if (guess == valeur) :
		compteur += 1
		print( "correctly guessed" )
	else :
		print( "uncorrectly guessed")

	print(compteur/float(turn)


#fin








